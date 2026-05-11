"""
RTB Document Planner - System Test
Tests all major functionality
"""
import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    try:
        import fastapi
        import uvicorn
        import sqlalchemy
        import pydantic
        from docx import Document
        print("✓ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Run: pip install -r backend/requirements.txt")
        return False

def test_database():
    """Test database connection"""
    print("\nTesting database...")
    try:
        sys.path.insert(0, 'backend')
        from database import engine, SessionLocal
        import models
        
        # Try to create tables
        models.Base.metadata.create_all(bind=engine)
        
        # Try to query
        db = SessionLocal()
        user_count = db.query(models.User).count()
        db.close()
        
        print(f"✓ Database working ({user_count} users)")
        return True
    except Exception as e:
        print(f"❌ Database error: {e}")
        return False

def test_document_generation():
    """Test DOCX generation"""
    print("\nTesting document generation...")
    try:
        sys.path.insert(0, 'backend')
        from document_generator import generate_smart_objectives
        
        objectives = generate_smart_objectives(
            "Variables and Data Types",
            "Identify and use different data types",
            "Basic to advanced concepts",
            "Integer, Float, String, Boolean"
        )
        
        if objectives and len(objectives) > 50:
            print("✓ Document generation working")
            return True
        else:
            print("❌ Document generation failed")
            return False
    except Exception as e:
        print(f"❌ Document generation error: {e}")
        return False

def test_api_structure():
    """Test API structure"""
    print("\nTesting API structure...")
    try:
        sys.path.insert(0, 'backend')
        import main
        
        # Check if FastAPI app exists
        if hasattr(main, 'app'):
            print("✓ FastAPI app found")
            return True
        else:
            print("❌ FastAPI app not found")
            return False
    except Exception as e:
        print(f"❌ API structure error: {e}")
        return False

def main():
    print("=" * 50)
    print("RTB Document Planner - System Test")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_database,
        test_document_generation,
        test_api_structure
    ]
    
    results = [test() for test in tests]
    
    print("\n" + "=" * 50)
    print("Test Results")
    print("=" * 50)
    
    passed = sum(results)
    total = len(results)
    
    print(f"\nPassed: {passed}/{total}")
    
    if passed == total:
        print("\n✅ All tests passed! System is ready.")
        print("\nNext steps:")
        print("1. Run: start_rtb_system.bat")
        print("2. Open: http://localhost:5173")
    else:
        print("\n⚠️ Some tests failed. Please fix the issues above.")
        print("\nCommon fixes:")
        print("- Run: pip install -r backend/requirements.txt")
        print("- Run: python backend/init_database.py")

if __name__ == "__main__":
    main()
