@echo off
echo ========================================
echo ADD TEST USER TO DATABASE
echo ========================================
echo.

cd backend

python -c "from database import SessionLocal; from models import User; db = SessionLocal(); phone = '+250789751558'; user = db.query(User).filter(User.phone == phone).first(); print(f'User exists: {user.name}' if user else 'User not found'); db.close()" 2>nul

if %errorlevel% equ 0 (
    echo User already exists!
) else (
    echo Creating test user...
    python -c "from database import SessionLocal; from models import User; db = SessionLocal(); user = User(user_id='USER_TEST', name='Test Teacher', phone='+250789751558', email='test@test.com', institution='Test School', password='test123', role='user'); db.add(user); db.commit(); print('Test user created!'); print('Phone: +250789751558'); print('Password: test123'); db.close()"
)

echo.
echo ========================================
echo ALL USERS IN DATABASE:
echo ========================================
python -c "from database import SessionLocal; from models import User; db = SessionLocal(); users = db.query(User).all(); [print(f'{u.name} - {u.phone} - Password: {u.password} - Role: {u.role}') for u in users]; db.close()"

cd ..
echo.
pause
