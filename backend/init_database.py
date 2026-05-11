"""
Initialize RTB Document Planner Database
Creates tables and default admin user
"""
from database import engine, SessionLocal
import models

def init_database():
    print("Creating database tables...")
    models.Base.metadata.create_all(bind=engine)
    print("[OK] Tables created successfully")
    
    db = SessionLocal()
    try:
        # Check if admin exists
        admin = db.query(models.User).filter(models.User.phone == "+250789751597").first()
        if not admin:
            print("Creating default admin user...")
            admin = models.User(
                user_id="ADMIN_001",
                name="RTB Administrator",
                phone="+250789751597",
                email="admin@rtb.rw",
                institution="Rwanda Technical Board",
                password="admin123",
                role="admin"
            )
            db.add(admin)
            db.commit()
            print("[OK] Admin user created")
            print("\nAdmin Credentials:")
            print("  Phone: +250789751597")
            print("  Password: admin123")
        else:
            print("[OK] Admin user already exists")
        
        print("\n[SUCCESS] Database initialization complete!")
        print("\nYou can now start the backend server:")
        print("  cd backend")
        print("  uvicorn main:app --reload --port 5000")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_database()
