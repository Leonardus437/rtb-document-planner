"""
Database reset endpoint - drops all tables and recreates them
"""
from fastapi import APIRouter, HTTPException
from database import engine, Base
import models

router = APIRouter()

@router.get("/reset-database")
def reset_database(secret_key: str):
    """Drop all tables and recreate them with new schema"""
    
    if secret_key != "RTB2024RESET":
        raise HTTPException(status_code=403, detail="Invalid secret key")
    
    try:
        # Drop all tables
        Base.metadata.drop_all(bind=engine)
        
        # Recreate all tables with new schema
        Base.metadata.create_all(bind=engine)
        
        return {
            "message": "Database reset successfully!",
            "note": "All tables dropped and recreated. Now call /init-production-db to add users."
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
