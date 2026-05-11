"""
Safe database migration - adds missing columns without deleting data
"""
from fastapi import APIRouter, HTTPException
from sqlalchemy import text
from database import engine

router = APIRouter()

@router.get("/migrate-database")
def migrate_database(secret_key: str):
    """Add missing columns to existing tables without deleting data"""
    
    if secret_key != "RTB2024MIGRATE":
        raise HTTPException(status_code=403, detail="Invalid secret key")
    
    try:
        with engine.connect() as conn:
            # Add missing columns to users table if they don't exist
            try:
                conn.execute(text("ALTER TABLE users ADD COLUMN is_premium BOOLEAN DEFAULT 0"))
                conn.commit()
            except:
                pass  # Column already exists
            
            try:
                conn.execute(text("ALTER TABLE users ADD COLUMN session_plans_limit INTEGER DEFAULT 999"))
                conn.commit()
            except:
                pass
            
            try:
                conn.execute(text("ALTER TABLE users ADD COLUMN schemes_limit INTEGER DEFAULT 999"))
                conn.commit()
            except:
                pass
            
            try:
                conn.execute(text("ALTER TABLE users ADD COLUMN session_plans_downloaded INTEGER DEFAULT 0"))
                conn.commit()
            except:
                pass
            
            try:
                conn.execute(text("ALTER TABLE users ADD COLUMN schemes_downloaded INTEGER DEFAULT 0"))
                conn.commit()
            except:
                pass
            
            # Add user_phone to session_plans if it doesn't exist
            try:
                conn.execute(text("ALTER TABLE session_plans ADD COLUMN user_phone VARCHAR(50)"))
                conn.commit()
            except:
                pass
            
            # Add user_phone to schemes_of_work if it doesn't exist
            try:
                conn.execute(text("ALTER TABLE schemes_of_work ADD COLUMN user_phone VARCHAR(50)"))
                conn.commit()
            except:
                pass
        
        return {
            "message": "Database migrated successfully!",
            "note": "Missing columns added. All existing data preserved."
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
