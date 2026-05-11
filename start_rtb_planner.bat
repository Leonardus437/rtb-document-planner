@echo off
echo ========================================
echo RTB Document Planner - Quick Start
echo ========================================
echo.

echo 🔧 Setting up environment...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.8+ and try again
    pause
    exit /b 1
)

echo ✅ Python found

REM Navigate to backend directory
cd /d "%~dp0backend"

echo 📦 Installing backend dependencies...
pip install -r requirements.txt

echo 🗄️ Initializing database...
python -c "from database import engine, Base; from models import *; Base.metadata.create_all(bind=engine); print('Database initialized')"

echo 🚀 Starting backend server...
start "RTB Backend" cmd /k "python main_complete.py"

REM Wait a moment for backend to start
timeout /t 3 /nobreak >nul

echo 🌐 Starting frontend server...
cd /d "%~dp0frontend"
start "RTB Frontend" cmd /k "python -m http.server 5173"

echo.
echo ========================================
echo 🎉 RTB Document Planner is starting!
echo ========================================
echo.
echo 📍 Backend API: http://localhost:8000
echo 🌐 Frontend: http://localhost:5173
echo 👤 Admin Login: +250789751597 / admin123
echo.
echo Press any key to open the application...
pause >nul

REM Open the application in default browser
start http://localhost:5173

echo.
echo ✅ Application opened in browser
echo.
echo To stop the servers:
echo - Close the backend and frontend command windows
echo - Or press Ctrl+C in each window
echo.
pause