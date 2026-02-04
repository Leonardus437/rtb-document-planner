import sys
import os
sys.path.insert(0, 'backend')
os.chdir('backend')

from database import SessionLocal
from models import User

db = SessionLocal()

# Check if user exists
phone = "+250789751558"
user = db.query(User).filter(User.phone == phone).first()

if user:
    print(f"✅ User found: {user.name} ({user.phone})")
    print(f"   Role: {user.role}")
    print(f"   Password: {user.password}")
else:
    print(f"❌ User with phone {phone} NOT found")
    print("\n📋 Creating test user...")
    
    # Create test user
    test_user = User(
        user_id=f"USER_{phone}",
        name="Test Teacher",
        phone=phone,
        email="test@example.com",
        institution="Test School",
        password="test123",
        role="user"
    )
    db.add(test_user)
    db.commit()
    print(f"✅ Test user created!")
    print(f"   Phone: {phone}")
    print(f"   Password: test123")

print("\n📋 All users in database:")
all_users = db.query(User).all()
for u in all_users:
    print(f"   - {u.name} ({u.phone}) - Role: {u.role} - Password: {u.password}")

db.close()
