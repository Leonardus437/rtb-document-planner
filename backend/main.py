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
from document_generator import generate_session_plan_docx, generate_scheme_of_work_docx

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="RTB Document Planner API")

# Import init endpoint
from init_endpoint import router as init_router
app.include_router(init_router)

# Import reset endpoint
from reset_endpoint import router as reset_router
app.include_router(reset_router)

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

@app.post("/users/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    existing_email = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    db_user = models.User(
        user_id=f"USER_{datetime.now().strftime('%Y%m%d%H%M%S')}",
        name=user.name,
        phone="",  # Empty phone
        email=user.email,
        institution=user.institution or "",
        password=user.password,
        role="user"
    )
    db.add(db_user)
    db.commit()
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