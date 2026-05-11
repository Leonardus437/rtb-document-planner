"""
Add logo columns to schemes_of_work table
"""
import sqlite3

def migrate():
    conn = sqlite3.connect('rtb_planner.db')
    cursor = conn.cursor()
    
    try:
        # Add logo columns to schemes_of_work if they don't exist
        cursor.execute("PRAGMA table_info(schemes_of_work)")
        columns = [col[1] for col in cursor.fetchall()]
        
        if 'rtb_logo_path' not in columns:
            cursor.execute("ALTER TABLE schemes_of_work ADD COLUMN rtb_logo_path VARCHAR(500)")
            print("Added rtb_logo_path column to schemes_of_work")
        
        if 'school_logo_path' not in columns:
            cursor.execute("ALTER TABLE schemes_of_work ADD COLUMN school_logo_path VARCHAR(500)")
            print("Added school_logo_path column to schemes_of_work")
        
        conn.commit()
        print("Migration completed successfully!")
        
    except Exception as e:
        print(f"Migration error: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    migrate()
