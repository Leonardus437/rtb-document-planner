from fastapi import FastAPI, HTTPException, Depends, File, UploadFile, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text
from pydantic import BaseModel
from typing import Optional, List
import os
import tempfile
import shutil
from datetime import datetime

# Import our models and database
from database import SessionLocal, engine, Base
from models import SessionPlan, SchemeOfWork, User, Notification
from document_generator import generate_session_plan_docx, generate_scheme_of_work_docx

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="RTB Document Planner API", version="1.0.0")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models
class SessionPlanCreate(BaseModel):
    sector: Optional[str] = None
    sub_sector: Optional[str] = None
    trade: Optional[str] = None
    qualification_title: Optional[str] = None
    rqf_level: Optional[str] = None
    module_code_title: Optional[str] = None
    term: Optional[str] = None
    week: Optional[str] = None
    date: Optional[str] = None
    trainer_name: Optional[str] = None
    class_name: Optional[str] = None
    number_of_trainees: Optional[str] = None
    learning_outcomes: Optional[str] = None
    indicative_contents: Optional[str] = None
    topic_of_session: Optional[str] = None
    duration: Optional[str] = None
    objectives: Optional[str] = None
    facilitation_techniques: Optional[str] = None
    learning_activities: Optional[str] = None
    resources: Optional[str] = None
    assessment_details: Optional[str] = None
    references: Optional[str] = None
    appendices: Optional[str] = None
    reflection: Optional[str] = None
    session_range: Optional[str] = None

class SchemeOfWorkCreate(BaseModel):
    province: Optional[str] = None
    district: Optional[str] = None
    sector: Optional[str] = None
    school: Optional[str] = None
    department_trade: Optional[str] = None
    qualification_title: Optional[str] = None
    rqf_level: Optional[str] = None
    module_code_title: Optional[str] = None
    school_year: Optional[str] = None
    term: Optional[str] = None
    module_learning_hours: Optional[str] = None
    number_of_classes: Optional[str] = None
    class_name: Optional[str] = None
    cohort_size: Optional[str] = None
    trainer_name: Optional[str] = None
    trainer_position: Optional[str] = None
    module_rationale: Optional[str] = None
    entry_requirements: Optional[str] = None
    competency_codes: Optional[str] = None
    indicative_scope: Optional[str] = None
    standards_alignment: Optional[str] = None
    cross_cutting_issues: Optional[str] = None
    key_skills: Optional[str] = None
    delivery_approach: Optional[str] = None
    formative_assessment: Optional[str] = None
    summative_assessment: Optional[str] = None
    resource_inventory: Optional[str] = None
    health_safety: Optional[str] = None
    terms: Optional[str] = None
    module_hours: Optional[str] = None
    term1_weeks: Optional[str] = None
    term1_learning_outcomes: Optional[str] = None
    term1_indicative_contents: Optional[str] = None
    term1_duration: Optional[str] = None
    term2_weeks: Optional[str] = None
    term2_learning_outcomes: Optional[str] = None
    term2_indicative_contents: Optional[str] = None
    term2_duration: Optional[str] = None
    term3_weeks: Optional[str] = None
    term3_learning_outcomes: Optional[str] = None
    term3_indicative_contents: Optional[str] = None
    term3_duration: Optional[str] = None
    dos_name: Optional[str] = None
    manager_name: Optional[str] = None

class UserCreate(BaseModel):
    user_id: str
    name: str
    phone: str
    email: Optional[str] = None
    institution: Optional[str] = None
    password: str

class UserLogin(BaseModel):
    phone: str
    password: str

class UserUpdate(BaseModel):
    is_premium: Optional[bool] = None
    session_plans_limit: Optional[int] = None
    schemes_limit: Optional[int] = None
    is_active: Optional[bool] = None

# Initialize admin user
def init_admin_user(db: Session):
    admin_phone = "+250789751597"
    admin = db.query(User).filter(User.phone == admin_phone).first()
    if not admin:
        admin = User(
            user_id="ADMIN_001",
            name="Administrator",
            phone=admin_phone,
            email="admin@rtb.rw",
            institution="RTB",
            password="admin123",
            role="admin",
            is_premium=True,
            session_plans_limit=999,
            schemes_limit=999
        )
        db.add(admin)
        db.commit()
        print(f"✅ Admin user created: {admin_phone}")

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    db = SessionLocal()
    try:
        init_admin_user(db)
    finally:
        db.close()

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "RTB Document Planner API",
        "status": "online",
        "version": "1.0.0",
        "endpoints": {
            "session_plans": "/session-plans/",
            "schemes": "/schemes/",
            "users": "/users/",
            "auth": "/users/login"
        }
    }

# User Management Endpoints
@app.post("/users/register")
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if phone already exists
    existing_user = db.query(User).filter(User.phone == user.phone).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Phone number already registered")
    
    # Create new user
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return {"message": "User registered successfully", "user_id": db_user.user_id}

@app.post("/users/login")
async def login_user(credentials: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.phone == credentials.phone).first()
    if not user or user.password != credentials.password:
        raise HTTPException(status_code=401, detail="Invalid phone number or password")
    
    return {
        "user_id": user.user_id,
        "name": user.name,
        "phone": user.phone,
        "email": user.email,
        "institution": user.institution,
        "role": user.role,
        "is_premium": user.is_premium,
        "session_plans_limit": user.session_plans_limit,
        "schemes_limit": user.schemes_limit
    }

@app.get("/users/")
async def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [
        {
            "user_id": user.user_id,
            "name": user.name,
            "phone": user.phone,
            "email": user.email,
            "institution": user.institution,
            "role": user.role,
            "is_premium": user.is_premium,
            "session_plans_limit": user.session_plans_limit,
            "schemes_limit": user.schemes_limit,
            "session_plans_downloaded": user.session_plans_downloaded,
            "schemes_downloaded": user.schemes_downloaded
        }
        for user in users
    ]

@app.get("/users/{phone}")
async def get_user(phone: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.phone == phone).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "user_id": user.user_id,
        "name": user.name,
        "phone": user.phone,
        "email": user.email,
        "institution": user.institution,
        "role": user.role,
        "is_premium": user.is_premium,
        "session_plans_limit": user.session_plans_limit,
        "schemes_limit": user.schemes_limit,
        "session_plans_downloaded": user.session_plans_downloaded,
        "schemes_downloaded": user.schemes_downloaded
    }

@app.put("/users/{phone}")
async def update_user(phone: str, user_update: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.phone == phone).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    for field, value in user_update.dict(exclude_unset=True).items():
        setattr(user, field, value)
    
    db.commit()
    return {"message": "User updated successfully"}

@app.get("/user-limits/{phone}")
async def get_user_limits(phone: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.phone == phone).first()
    if not user:
        return {
            "session_plans_limit": 2,
            "schemes_limit": 2,
            "session_plans_downloaded": 0,
            "schemes_downloaded": 0,
            "is_premium": False
        }
    
    return {
        "session_plans_limit": user.session_plans_limit,
        "schemes_limit": user.schemes_limit,
        "session_plans_downloaded": user.session_plans_downloaded,
        "schemes_downloaded": user.schemes_downloaded,
        "is_premium": user.is_premium,
        "session_plans_remaining": max(0, user.session_plans_limit - user.session_plans_downloaded) if not user.is_premium else 999,
        "schemes_remaining": max(0, user.schemes_limit - user.schemes_downloaded) if not user.is_premium else 999
    }

@app.get("/stats")
async def get_stats(db: Session = Depends(get_db)):
    total_users = db.query(User).count()
    premium_users = db.query(User).filter(User.is_premium == True).count()
    total_session_plans = db.query(SessionPlan).count()
    total_schemes = db.query(SchemeOfWork).count()
    
    return {
        "total_users": total_users,
        "premium_users": premium_users,
        "free_users": total_users - premium_users,
        "total_session_plans": total_session_plans,
        "total_schemes": total_schemes,
        "total_downloads": total_session_plans + total_schemes
    }

# Session Plan Endpoints
@app.post("/session-plans/")
async def create_session_plan(session_plan: SessionPlanCreate, db: Session = Depends(get_db)):
    db_session_plan = SessionPlan(**session_plan.dict())
    db.add(db_session_plan)
    db.commit()
    db.refresh(db_session_plan)
    return {"id": db_session_plan.id, "message": "Session plan created successfully"}

@app.get("/session-plans/")
async def get_session_plans(db: Session = Depends(get_db)):
    return db.query(SessionPlan).all()

@app.get("/session-plans/{plan_id}")
async def get_session_plan(plan_id: int, db: Session = Depends(get_db)):
    plan = db.query(SessionPlan).filter(SessionPlan.id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Session plan not found")
    return plan

@app.get("/session-plans/{plan_id}/download")
async def download_session_plan(plan_id: int, phone: Optional[str] = None, db: Session = Depends(get_db)):
    # Get the session plan
    plan = db.query(SessionPlan).filter(SessionPlan.id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Session plan not found")
    
    # Update download counter if phone provided
    if phone:
        user = db.query(User).filter(User.phone == phone).first()
        if user and not user.is_premium:
            user.session_plans_downloaded += 1
            db.commit()
    
    # Generate document
    try:
        doc_path = generate_session_plan_docx(plan)
        filename = f"session_plan_{plan.topic_of_session or 'document'}_{datetime.now().strftime('%Y%m%d')}.docx"
        
        return FileResponse(
            path=doc_path,
            filename=filename,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating document: {str(e)}")

# Scheme of Work Endpoints
@app.post("/schemes/")
async def create_scheme(scheme: SchemeOfWorkCreate, db: Session = Depends(get_db)):
    db_scheme = SchemeOfWork(**scheme.dict())
    db.add(db_scheme)
    db.commit()
    db.refresh(db_scheme)
    return {"id": db_scheme.id, "message": "Scheme of work created successfully"}

@app.get("/schemes/")
async def get_schemes(db: Session = Depends(get_db)):
    return db.query(SchemeOfWork).all()

@app.get("/schemes/{scheme_id}")
async def get_scheme(scheme_id: int, db: Session = Depends(get_db)):
    scheme = db.query(SchemeOfWork).filter(SchemeOfWork.id == scheme_id).first()
    if not scheme:
        raise HTTPException(status_code=404, detail="Scheme of work not found")
    return scheme

@app.get("/schemes/{scheme_id}/download")
async def download_scheme(scheme_id: int, phone: Optional[str] = None, db: Session = Depends(get_db)):
    # Get the scheme
    scheme = db.query(SchemeOfWork).filter(SchemeOfWork.id == scheme_id).first()
    if not scheme:
        raise HTTPException(status_code=404, detail="Scheme of work not found")
    
    # Update download counter if phone provided
    if phone:
        user = db.query(User).filter(User.phone == phone).first()
        if user and not user.is_premium:
            user.schemes_downloaded += 1
            db.commit()
    
    # Generate document
    try:
        doc_path = generate_scheme_of_work_docx(scheme)
        filename = f"scheme_of_work_{scheme.module_code_title or 'document'}_{datetime.now().strftime('%Y%m%d')}.docx"
        
        return FileResponse(
            path=doc_path,
            filename=filename,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating document: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting RTB Document Planner Backend...")
    print("📍 Backend running at: http://localhost:8000")
    print("🌐 Frontend should run at: http://localhost:5173")
    print("✅ CORS enabled for all origins")
    print("👤 Admin: +250789751597 / admin123")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)