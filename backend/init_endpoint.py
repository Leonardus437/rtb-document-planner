"""
One-time database initialization endpoint for production
"""
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from database import get_database
import models

router = APIRouter()

@router.post("/init-production-db")
def initialize_production_database(secret_key: str, db: Session = Depends(get_database)):
    """Initialize production database with admin and demo accounts"""
    
    # Simple security check
    if secret_key != "RTB2024INIT":
        raise HTTPException(status_code=403, detail="Invalid secret key")
    
    try:
        # Check if admin already exists
        admin = db.query(models.User).filter(models.User.phone == "+250789751597").first()
        if admin:
            return {"message": "Database already initialized", "admin_exists": True}
        
        # Create admin
        admin = models.User(
            user_id=f"ADMIN_{datetime.now().strftime('%Y%m%d%H%M%S')}",
            name="RTB Administrator",
            phone="+250789751597",
            email="admin@rtb.gov.rw",
            institution="Rwanda Technical Board",
            password="admin123",
            role="admin"
        )
        db.add(admin)
        
        # Create demo teachers
        demo_teachers = [
            {
                "name": "Jean MUGABO",
                "phone": "+250788123456",
                "email": "j.mugabo@iprc.ac.rw",
                "institution": "IPRC Kigali",
                "password": "teacher123"
            },
            {
                "name": "Marie UWASE",
                "phone": "+250788234567",
                "email": "m.uwase@iprc.ac.rw",
                "institution": "IPRC Huye",
                "password": "teacher123"
            },
            {
                "name": "Patrick NIYONZIMA",
                "phone": "+250788345678",
                "email": "p.niyonzima@tvet.rw",
                "institution": "IPRC Musanze",
                "password": "teacher123"
            },
            {
                "name": "Grace MUKAMANA",
                "phone": "+250788456789",
                "email": "g.mukamana@tvet.rw",
                "institution": "IPRC Tumba",
                "password": "teacher123"
            },
            {
                "name": "Emmanuel HABIMANA",
                "phone": "+250788567890",
                "email": "e.habimana@tvet.rw",
                "institution": "IPRC Gishari",
                "password": "teacher123"
            }
        ]
        
        for teacher_data in demo_teachers:
            teacher = models.User(
                user_id=f"USER_{datetime.now().strftime('%Y%m%d%H%M%S')}_{teacher_data['phone'][-4:]}",
                name=teacher_data["name"],
                phone=teacher_data["phone"],
                email=teacher_data["email"],
                institution=teacher_data["institution"],
                password=teacher_data["password"],
                role="user"
            )
            db.add(teacher)
        
        db.commit()
        
        return {
            "message": "Production database initialized successfully!",
            "admin_created": True,
            "demo_teachers_created": 5,
            "admin_credentials": {
                "phone": "+250789751597",
                "password": "admin123"
            },
            "demo_credentials": {
                "phone": "+250788123456",
                "password": "teacher123"
            }
        }
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
