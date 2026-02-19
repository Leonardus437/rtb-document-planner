from fastapi import FastAPI, HTTPException, Depends, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from datetime import datetime
import os
import shutil
from database import SessionLocal, engine
import models
import schemas
from document_generator import generate_session_plan_docx, generate_scheme_of_work_docx, generate_assessment_plan_docx, generate_trainer_assessment_report_docx

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="RTB Document Planner API")

# Startup event to ensure admin exists
@app.on_event("startup")
def startup_event():
    """Ensure admin user exists on startup"""
    db = SessionLocal()
    try:
        # Check if any users exist
        user_count = db.query(models.User).count()
        if user_count == 0:
            # Create admin user
            admin = models.User(
                user_id=f"ADMIN_{datetime.now().strftime('%Y%m%d%H%M%S')}",
                name="RTB Administrator",
                phone="+250789751597",
                email="admin@rtb.gov.rw",
                institution="Rwanda Technical Board",
                password="admin123",
                role="admin",
                is_premium=True,
                session_plans_limit=999,
                schemes_limit=999
            )
            db.add(admin)
            db.commit()
            print("✅ Admin user created automatically")
        else:
            print(f"✅ Database has {user_count} users - data is persistent")
    except Exception as e:
        print(f"❌ Startup error: {e}")
    finally:
        db.close()

# Import init endpoint
from init_endpoint import router as init_router
app.include_router(init_router)

# Import migrate endpoint
from migrate_endpoint import router as migrate_router
app.include_router(migrate_router)

# Mount static files for frontend
if os.path.exists("../frontend"):
    app.mount("/static", StaticFiles(directory="../frontend"), name="static")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for deployment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    """Serve the main frontend page"""
    if os.path.exists("../frontend/index.html"):
        with open("../frontend/index.html", "r", encoding="utf-8") as f:
            content = f.read()
        return HTMLResponse(content=content)
    return {
        "message": "RTB Document Planner API",
        "status": "online",
        "version": "3.0",
        "endpoints": ["register", "login", "session-plans", "schemes"]
    }

@app.get("/api")
def api_info():
    return {
        "message": "RTB Document Planner API",
        "status": "online",
        "version": "3.0",
        "endpoints": ["register", "login", "session-plans", "schemes"]
    }

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    """Health check with database user count"""
    try:
        user_count = db.query(models.User).count()
        return {
            "status": "healthy",
            "database": "connected",
            "total_users": user_count,
            "message": f"Database has {user_count} users - data is persistent"
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "error",
            "error": str(e)
        }

@app.post("/users/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    print(f"📝 Registration attempt for email: {user.email}")
    # Check if email already exists
    existing_email = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_email:
        print(f"❌ Email already exists: {user.email}")
        raise HTTPException(status_code=400, detail="Email already registered")
    
    db_user = models.User(
        user_id=f"USER_{datetime.now().strftime('%Y%m%d%H%M%S')}",
        name=user.name,
        phone=None,  # No phone for teachers
        email=user.email,
        institution=user.institution or "",
        password=user.password,
        role="user"
    )
    db.add(db_user)
    db.commit()
    print(f"✅ User registered successfully: {user.email}")
    return {"message": "User registered successfully"}

@app.post("/users/login")
def login(credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    # Try to find user by email first (for teachers)
    user = db.query(models.User).filter(models.User.email == credentials.email).first()
    
    # If not found by email, try phone (for admin)
    if not user:
        user = db.query(models.User).filter(models.User.phone == credentials.email).first()
    
    if not user or user.password != credentials.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {
        "user_id": user.user_id,
        "name": user.name,
        "phone": user.phone,
        "email": user.email,
        "institution": user.institution,
        "role": user.role
    }

@app.get("/user-limits/{phone}")
def user_limits(phone: str, db: Session = Depends(get_db)):
    return {
        "unlimited": True,
        "message": "System is completely free - create unlimited documents!"
    }

@app.post("/upload-logo")
async def upload_logo(file: UploadFile = File(...)):
    """Upload logo image"""
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)
    
    file_path = os.path.join(upload_dir, f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}")
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {"path": file_path}

@app.post("/session-plans/")
def create_session_plan(plan: schemas.SessionPlanCreate, db: Session = Depends(get_db)):
    try:
        db_plan = models.SessionPlan(**plan.dict())
        db.add(db_plan)
        db.commit()
        db.refresh(db_plan)
        return {"id": db_plan.id, "message": "Session plan created successfully"}
    except Exception as e:
        print(f"Error creating session plan: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/session-plans/{plan_id}/download")
def download_session_plan(plan_id: int, db: Session = Depends(get_db)):
    plan = db.query(models.SessionPlan).filter(models.SessionPlan.id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Session plan not found")
    
    docx_path = generate_session_plan_docx(plan)
    return FileResponse(
        docx_path,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename=f"RTB_Session_Plan_{plan_id}.docx"
    )

@app.post("/schemes/")
def create_scheme(scheme: schemas.SchemeCreate, db: Session = Depends(get_db)):
    db_scheme = models.SchemeOfWork(**scheme.dict())
    db.add(db_scheme)
    db.commit()
    db.refresh(db_scheme)
    return {"id": db_scheme.id, "message": "Scheme of work created successfully"}

@app.get("/schemes/{scheme_id}/download")
def download_scheme(scheme_id: int, db: Session = Depends(get_db)):
    scheme = db.query(models.SchemeOfWork).filter(models.SchemeOfWork.id == scheme_id).first()
    if not scheme:
        raise HTTPException(status_code=404, detail="Scheme not found")
    
    docx_path = generate_scheme_of_work_docx(scheme)
    return FileResponse(
        docx_path,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename=f"RTB_Scheme_of_Work_{scheme_id}.docx"
    )

@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@app.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    total_users = db.query(models.User).filter(models.User.role == "user").count()
    premium_users = db.query(models.User).filter(models.User.is_premium == True).count()
    total_plans = db.query(models.SessionPlan).count()
    total_schemes = db.query(models.SchemeOfWork).count()
    
    return {
        "total_users": total_users,
        "premium_users": premium_users,
        "total_session_plans": total_plans,
        "total_schemes": total_schemes,
        "total_downloads": total_plans + total_schemes
    }

@app.get("/admin/recent-activity")
def get_recent_activity(limit: int = 10, db: Session = Depends(get_db)):
    plans = db.query(models.SessionPlan).order_by(models.SessionPlan.created_at.desc()).limit(limit).all()
    schemes = db.query(models.SchemeOfWork).order_by(models.SchemeOfWork.created_at.desc()).limit(limit).all()
    
    activities = []
    for plan in plans:
        activities.append({
            "type": "session_plan",
            "user_phone": plan.user_phone,
            "title": plan.topic,
            "created_at": plan.created_at.isoformat() if plan.created_at else None
        })
    for scheme in schemes:
        activities.append({
            "type": "scheme",
            "user_phone": scheme.user_phone,
            "title": scheme.module_name,
            "created_at": scheme.created_at.isoformat() if scheme.created_at else None
        })
    
    activities.sort(key=lambda x: x["created_at"] or "", reverse=True)
    return activities[:limit]

@app.get("/admin/user-documents/{identifier}")
def get_user_documents(identifier: str, db: Session = Depends(get_db)):
    # Try to find by email first, then phone
    plans = db.query(models.SessionPlan).filter(
        (models.SessionPlan.user_phone == identifier) | (models.SessionPlan.user_phone.like(f"%{identifier}%"))
    ).all()
    schemes = db.query(models.SchemeOfWork).filter(
        (models.SchemeOfWork.user_phone == identifier) | (models.SchemeOfWork.user_phone.like(f"%{identifier}%"))
    ).all()
    
    # Also try to match by user email
    user = db.query(models.User).filter(
        (models.User.email == identifier) | (models.User.phone == identifier)
    ).first()
    
    if user:
        # Get documents by user's phone or email
        plans = db.query(models.SessionPlan).filter(
            (models.SessionPlan.user_phone == user.phone) | (models.SessionPlan.user_phone == user.email)
        ).all()
        schemes = db.query(models.SchemeOfWork).filter(
            (models.SchemeOfWork.user_phone == user.phone) | (models.SchemeOfWork.user_phone == user.email)
        ).all()
    
    return {
        "session_plans": len(plans),
        "schemes": len(schemes),
        "total": len(plans) + len(schemes)
    }

@app.delete("/user-limits/{phone}")
def remove_endpoint(phone: str):
    raise HTTPException(status_code=404, detail="Endpoint removed")

@app.put("/users/{identifier}")
def update_user(identifier: str, update: dict, db: Session = Depends(get_db)):
    # Try to find by email or phone
    user = db.query(models.User).filter(
        (models.User.email == identifier) | (models.User.phone == identifier)
    ).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    for key, value in update.items():
        if hasattr(user, key):
            setattr(user, key, value)
    
    db.commit()
    return {"message": "User updated successfully"}

@app.delete("/users/{identifier}")
def delete_user(identifier: str, db: Session = Depends(get_db)):
    # Try to find by email or phone
    user = db.query(models.User).filter(
        (models.User.email == identifier) | (models.User.phone == identifier)
    ).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.role == "admin":
        raise HTTPException(status_code=403, detail="Cannot delete admin user")
    
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

@app.post("/assessment-plans/")
def create_assessment_plan(plan: schemas.AssessmentPlanCreate, db: Session = Depends(get_db)):
    db_plan = models.AssessmentPlan(**plan.dict())
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return {"id": db_plan.id, "message": "Assessment plan created successfully"}

@app.get("/assessment-plans/{plan_id}/download")
def download_assessment_plan(plan_id: int, db: Session = Depends(get_db)):
    plan = db.query(models.AssessmentPlan).filter(models.AssessmentPlan.id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Assessment plan not found")
    
    docx_path = generate_assessment_plan_docx(plan)
    return FileResponse(
        docx_path,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename=f"RTB_Assessment_Plan_{plan_id}.docx"
    )

@app.post("/trainer-reports/")
def create_trainer_report(report: schemas.TrainerAssessmentReportCreate, db: Session = Depends(get_db)):
    db_report = models.TrainerAssessmentReport(**report.dict())
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return {"id": db_report.id, "message": "Trainer assessment report created successfully"}

@app.post("/parse-marks-file/")
async def parse_marks_file(file: UploadFile = File(...)):
    """AI-Powered preview: Shows how marks will be parsed and normalized"""
    try:
        import pandas as pd
        import io
        import re
        
        content = await file.read()
        
        if file.filename.endswith('.csv'):
            df = pd.read_csv(io.BytesIO(content))
        else:
            df = pd.read_excel(io.BytesIO(content), engine='openpyxl')
        
        df = df.dropna(how='all')
        
        # Find name column
        name_col = None
        name_col_idx = 0
        for idx, col in enumerate(df.columns):
            if any(word in str(col).lower() for word in ['name', 'student', 'trainee', 'learner', 'names']):
                name_col = col
                name_col_idx = idx
                break
        if not name_col:
            name_col = df.columns[0]
        
        # Analyze marks columns
        marks_columns = []
        for col in df.columns[name_col_idx + 1:]:
            col_str = str(col)
            max_score = None
            match = re.search(r'/(\d+)', col_str)
            if match:
                max_score = float(match.group(1))
            
            try:
                numeric_data = pd.to_numeric(df[col], errors='coerce')
                if numeric_data.notna().sum() > 0:
                    marks_columns.append({
                        'name': col,
                        'max_score': max_score or 100,
                        'is_formative': any(word in col_str.lower() for word in ['assessment', 'quiz', 'test', 'formative', 'lo']),
                        'is_practical': 'practical' in col_str.lower(),
                        'is_written': any(word in col_str.lower() for word in ['written', 'theory', 'exam'])
                    })
            except:
                pass
        
        # Classify columns
        formative_cols = []
        summative_practical = None
        summative_written = None
        
        for col_info in marks_columns:
            if col_info['is_practical'] and not summative_practical:
                summative_practical = col_info
            elif col_info['is_written'] and not summative_written:
                summative_written = col_info
        
        for col_info in marks_columns:
            if col_info != summative_practical and col_info != summative_written:
                if len(formative_cols) < 3:
                    formative_cols.append(col_info)
        
        if not summative_practical or not summative_written:
            remaining = [c for c in marks_columns if c not in formative_cols]
            if len(remaining) >= 2:
                summative_practical = remaining[-2]
                summative_written = remaining[-1]
        
        # Process students
        trainees = []
        for idx, row in df.iterrows():
            name = str(row[name_col]).strip()
            if not name or name.lower() in ['nan', 'none', '', 'null'] or name.startswith('Unnamed'):
                continue
            
            formative_marks = []
            for col_info in formative_cols[:3]:
                try:
                    raw = float(row[col_info['name']]) if pd.notna(row[col_info['name']]) else 0
                    pct = (raw / col_info['max_score']) * 100
                    formative_marks.append(pct)
                except:
                    formative_marks.append(0.0)
            
            while len(formative_marks) < 3:
                formative_marks.append(0.0)
            
            formative_total = sum(formative_marks) / 3.0
            
            try:
                prac_raw = float(row[summative_practical['name']]) if pd.notna(row[summative_practical['name']]) else 0
                prac_pct = (prac_raw / summative_practical['max_score']) * 100
            except:
                prac_pct = 0.0
            
            try:
                writ_raw = float(row[summative_written['name']]) if pd.notna(row[summative_written['name']]) else 0
                writ_pct = (writ_raw / summative_written['max_score']) * 100
            except:
                writ_pct = 0.0
            
            summative_avg = (prac_pct + writ_pct) / 2.0
            final_total = (formative_total * 0.4) + (summative_avg * 0.6)
            
            trainees.append({
                'name': name,
                'formative_lo1': round(formative_marks[0], 1),
                'formative_lo2': round(formative_marks[1], 1),
                'formative_lo3': round(formative_marks[2], 1),
                'formative_total': round(formative_total, 1),
                'summative_practical': round(prac_pct, 1),
                'summative_written': round(writ_pct, 1),
                'final_total': round(final_total, 1),
                'decision': 'Pass' if final_total >= 50 else 'Fail'
            })
        
        return {
            "success": True,
            "trainees": trainees,
            "count": len(trainees),
            "column_mapping": {
                "formative_lo1": formative_cols[0]['name'] if len(formative_cols) > 0 else None,
                "formative_lo2": formative_cols[1]['name'] if len(formative_cols) > 1 else None,
                "formative_lo3": formative_cols[2]['name'] if len(formative_cols) > 2 else None,
                "summative_practical": summative_practical['name'] if summative_practical else None,
                "summative_written": summative_written['name'] if summative_written else None
            },
            "message": f"Parsed {len(trainees)} students. All marks normalized to percentages."
        }
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.post("/generate-report-from-file/")
async def generate_report_from_file(
    file: UploadFile = File(...),
    sector: str = '',
    trade: str = '',
    level: str = '',
    module_code_name: str = '',
    competence: str = '',
    qualification_title: str = '',
    learning_hours: str = '',
    trainer_name: str = '',
    user_phone: str = ''
):
    """AI-Powered parser: Intelligently extracts and normalizes marks from any Excel format"""
    try:
        import pandas as pd
        import io
        import json
        import re
        
        content = await file.read()
        
        if file.filename.endswith('.csv'):
            df = pd.read_csv(io.BytesIO(content))
        else:
            df = pd.read_excel(io.BytesIO(content), engine='openpyxl')
        
        df = df.dropna(how='all')
        
        # STEP 1: Find name column
        name_col = None
        name_col_idx = 0
        for idx, col in enumerate(df.columns):
            col_str = str(col).lower()
            if any(word in col_str for word in ['name', 'student', 'trainee', 'learner', 'names']):
                name_col = col
                name_col_idx = idx
                break
        
        if not name_col:
            name_col = df.columns[0]
            name_col_idx = 0
        
        # STEP 2: Analyze all columns after name to identify marks columns
        marks_columns = []
        for col in df.columns[name_col_idx + 1:]:
            col_str = str(col)
            
            # Extract max score from column name (e.g., "Assessment1/50" → 50)
            max_score = None
            match = re.search(r'/(\d+)', col_str)
            if match:
                max_score = float(match.group(1))
            
            # Check if column has numeric data
            try:
                numeric_data = pd.to_numeric(df[col], errors='coerce')
                if numeric_data.notna().sum() > 0:  # Has at least one valid number
                    marks_columns.append({
                        'name': col,
                        'max_score': max_score or 100,  # Default to 100 if not specified
                        'is_formative': any(word in col_str.lower() for word in ['assessment', 'quiz', 'test', 'formative', 'lo']),
                        'is_practical': 'practical' in col_str.lower(),
                        'is_written': any(word in col_str.lower() for word in ['written', 'theory', 'exam'])
                    })
            except:
                pass
        
        if len(marks_columns) < 5:
            raise HTTPException(status_code=400, detail=f"Need at least 5 marks columns. Found only {len(marks_columns)}. Please ensure your Excel has: 3 formative assessments + 1 practical + 1 written.")
        
        # STEP 3: Classify columns intelligently
        formative_cols = []
        summative_practical = None
        summative_written = None
        
        # First, identify practical and written
        for col_info in marks_columns:
            if col_info['is_practical'] and not summative_practical:
                summative_practical = col_info
            elif col_info['is_written'] and not summative_written:
                summative_written = col_info
        
        # Then get formative columns (first 3 non-summative columns)
        for col_info in marks_columns:
            if col_info != summative_practical and col_info != summative_written:
                if len(formative_cols) < 3:
                    formative_cols.append(col_info)
        
        # If we don't have practical/written explicitly, use last 2 columns
        if not summative_practical or not summative_written:
            remaining = [c for c in marks_columns if c not in formative_cols]
            if len(remaining) >= 2:
                summative_practical = remaining[-2]
                summative_written = remaining[-1]
            elif len(remaining) == 1:
                summative_practical = remaining[0]
                summative_written = remaining[0]
        
        # Ensure we have exactly 3 formative
        while len(formative_cols) < 3 and len(marks_columns) > len(formative_cols):
            for col_info in marks_columns:
                if col_info not in formative_cols and col_info != summative_practical and col_info != summative_written:
                    formative_cols.append(col_info)
                    break
        
        # STEP 4: Process each student
        trainees = []
        for idx, row in df.iterrows():
            name = str(row[name_col]).strip()
            if not name or name.lower() in ['nan', 'none', '', 'null'] or name.startswith('Unnamed'):
                continue
            
            # Extract and normalize formative marks (convert to percentage)
            formative_marks = []
            for col_info in formative_cols[:3]:
                try:
                    raw_mark = float(row[col_info['name']]) if pd.notna(row[col_info['name']]) else 0
                    percentage = (raw_mark / col_info['max_score']) * 100
                    formative_marks.append(percentage)
                except:
                    formative_marks.append(0.0)
            
            # Ensure exactly 3 formative marks
            while len(formative_marks) < 3:
                formative_marks.append(0.0)
            
            formative_lo1 = formative_marks[0]
            formative_lo2 = formative_marks[1]
            formative_lo3 = formative_marks[2]
            formative_total = (formative_lo1 + formative_lo2 + formative_lo3) / 3.0
            
            # Extract and normalize summative marks
            try:
                practical_raw = float(row[summative_practical['name']]) if pd.notna(row[summative_practical['name']]) else 0
                summative_practical_pct = (practical_raw / summative_practical['max_score']) * 100
            except:
                summative_practical_pct = 0.0
            
            try:
                written_raw = float(row[summative_written['name']]) if pd.notna(row[summative_written['name']]) else 0
                summative_written_pct = (written_raw / summative_written['max_score']) * 100
            except:
                summative_written_pct = 0.0
            
            summative_avg = (summative_practical_pct + summative_written_pct) / 2.0
            
            # RTB Formula: 40% formative + 60% summative
            final_total = (formative_total * 0.4) + (summative_avg * 0.6)
            decision = 'Pass' if final_total >= 50 else 'Fail'
            
            trainees.append({
                'name': name,
                'formative_lo1': str(round(formative_lo1, 1)),
                'formative_lo2': str(round(formative_lo2, 1)),
                'formative_lo3': str(round(formative_lo3, 1)),
                'formative_total': str(round(formative_total, 1)),
                'summative_practical': str(round(summative_practical_pct, 1)),
                'summative_written': str(round(summative_written_pct, 1)),
                'final_total': str(round(final_total, 1)),
                'decision': decision
            })
        
        if not trainees:
            raise HTTPException(status_code=400, detail="No valid student data found. Please check your Excel file format.")
        
        # Create report
        class ReportData:
            pass
        
        report = ReportData()
        report.sector = sector
        report.trade = trade
        report.level = level
        report.module_code_name = module_code_name
        report.competence = competence
        report.qualification_title = qualification_title
        report.learning_hours = learning_hours
        report.trainer_name = trainer_name
        report.trainees_data = json.dumps(trainees)
        
        docx_path = generate_trainer_assessment_report_docx(report)
        return FileResponse(
            docx_path,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            filename="RTB_Trainer_Assessment_Report.docx"
        )
        
    except HTTPException:
        raise
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/trainer-reports/{report_id}/download")
def download_trainer_report(report_id: int, db: Session = Depends(get_db)):
    report = db.query(models.TrainerAssessmentReport).filter(models.TrainerAssessmentReport.id == report_id).first()
    if not report:
        raise HTTPException(status_code=404, detail="Trainer report not found")
    
    docx_path = generate_trainer_assessment_report_docx(report)
    return FileResponse(
        docx_path,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename=f"RTB_Trainer_Assessment_Report_{report_id}.docx"
    )