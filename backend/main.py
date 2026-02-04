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
    existing = db.query(models.User).filter(models.User.phone == user.phone).first()
    if existing:
        raise HTTPException(status_code=400, detail="Phone number already registered")
    
    db_user = models.User(
        user_id=f"USER_{datetime.now().strftime('%Y%m%d%H%M%S')}",
        name=user.name,
        phone=user.phone,
        email=user.email or "",
        institution=user.institution or "",
        password=user.password,
        role="user"
    )
    db.add(db_user)
    db.commit()
    return {"message": "User registered successfully"}

@app.post("/users/login")
def login(credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.phone == credentials.phone).first()
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
    total_users = db.query(models.User).count()
    total_plans = db.query(models.SessionPlan).count()
    total_schemes = db.query(models.SchemeOfWork).count()
    
    return {
        "total_users": total_users,
        "total_session_plans": total_plans,
        "total_schemes": total_schemes
    }

@app.delete("/user-limits/{phone}")
def remove_endpoint(phone: str):
    raise HTTPException(status_code=404, detail="Endpoint removed")

@app.put("/users/{user_id}/premium")
def remove_premium_endpoint(user_id: int):
    raise HTTPException(status_code=404, detail="Endpoint removed")