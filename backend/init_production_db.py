"""
Initialize RTB Planner Database with Demo Users for Production
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import sys
import os

# Add backend to path
sys.path.insert(0, os.path.dirname(__file__))

from models import Base, User
from database import engine

def init_production_db():
    """Initialize database with demo users for Rwanda teachers"""
    
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    
    try:
        # Check if admin exists
        admin = db.query(User).filter(User.phone == "+250789751597").first()
        if not admin:
            print("Creating admin account...")
            admin = User(
                user_id=f"ADMIN_{datetime.now().strftime('%Y%m%d%H%M%S')}",
                name="RTB Administrator",
                phone="+250789751597",
                email="admin@rtb.gov.rw",
                institution="Rwanda Technical Board",
                password="admin123",
                role="admin"
            )
            db.add(admin)
            print("Admin created: +250789751597 / admin123")
        else:
            print("Admin already exists")
        
        # Create demo teacher accounts for different institutions
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
            existing = db.query(User).filter(User.phone == teacher_data["phone"]).first()
            if not existing:
                teacher = User(
                    user_id=f"USER_{datetime.now().strftime('%Y%m%d%H%M%S')}_{teacher_data['phone'][-4:]}",
                    name=teacher_data["name"],
                    phone=teacher_data["phone"],
                    email=teacher_data["email"],
                    institution=teacher_data["institution"],
                    password=teacher_data["password"],
                    role="user"
                )
                db.add(teacher)
                print(f"Created teacher: {teacher_data['name']} ({teacher_data['phone']})")
        
        db.commit()
        print("\n" + "="*60)
        print("DATABASE INITIALIZED SUCCESSFULLY!")
        print("="*60)
        print("\nADMIN CREDENTIALS:")
        print("  Phone: +250789751597")
        print("  Password: admin123")
        print("\nDEMO TEACHER CREDENTIALS:")
        print("  Phone: +250788123456 (or any demo number)")
        print("  Password: teacher123")
        print("\nAll teachers can also register their own accounts!")
        print("="*60)
        
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_production_db()
