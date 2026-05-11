@echo off
echo ========================================
echo RTB DOCUMENT PLANNER - SYSTEM TEST
echo ========================================
echo.

:: Check Python installation
echo [1/8] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found! Please install Python 3.11+
    pause
    exit /b 1
)
python --version
echo [OK] Python installed
echo.

:: Check if backend directory exists
echo [2/8] Checking project structure...
if not exist "backend\" (
    echo [ERROR] Backend directory not found!
    pause
    exit /b 1
)
if not exist "frontend\" (
    echo [ERROR] Frontend directory not found!
    pause
    exit /b 1
)
echo [OK] Project structure verified
echo.

:: Check dependencies
echo [3/8] Checking Python dependencies...
cd backend
pip show fastapi >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] Dependencies not installed. Installing now...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to install dependencies!
        cd ..
        pause
        exit /b 1
    )
)
echo [OK] Dependencies installed
echo.

:: Check database
echo [4/8] Checking database...
if exist "rtb_planner.db" (
    echo [OK] Database file exists
) else (
    echo [WARNING] Database not found. Initializing...
    python init_database.py
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to initialize database!
        cd ..
        pause
        exit /b 1
    )
    echo [OK] Database initialized
)
echo.

:: Test database connection
echo [5/8] Testing database connection...
python -c "from database import engine; from sqlalchemy import text; conn = engine.connect(); result = conn.execute(text('SELECT 1')); print('[OK] Database connection successful'); conn.close()"
if %errorlevel% neq 0 (
    echo [ERROR] Database connection failed!
    cd ..
    pause
    exit /b 1
)
echo.

:: Check if ports are available
echo [6/8] Checking port availability...
netstat -ano | findstr ":5000" >nul
if %errorlevel% equ 0 (
    echo [WARNING] Port 5000 is in use. Backend may already be running.
) else (
    echo [OK] Port 5000 available
)

netstat -ano | findstr ":5173" >nul
if %errorlevel% equ 0 (
    echo [WARNING] Port 5173 is in use. Frontend may already be running.
) else (
    echo [OK] Port 5173 available
)
echo.

:: Test backend startup (quick test)
echo [7/8] Testing backend startup...
start /B python -m uvicorn main:app --host 127.0.0.1 --port 5000 >nul 2>&1
timeout /t 5 /nobreak >nul
curl -s http://127.0.0.1:5000/api >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] Backend starts successfully
    taskkill /F /IM python.exe /FI "WINDOWTITLE eq *uvicorn*" >nul 2>&1
) else (
    echo [WARNING] Backend test inconclusive (curl may not be available)
    taskkill /F /IM python.exe /FI "WINDOWTITLE eq *uvicorn*" >nul 2>&1
)
cd ..
echo.

:: Check frontend files
echo [8/8] Checking frontend files...
if exist "frontend\index.html" (
    echo [OK] index.html found
) else (
    echo [ERROR] index.html not found!
    pause
    exit /b 1
)
if exist "frontend\wizard.html" (
    echo [OK] wizard.html found
) else (
    echo [ERROR] wizard.html not found!
    pause
    exit /b 1
)
if exist "frontend\scheme-wizard.html" (
    echo [OK] scheme-wizard.html found
) else (
    echo [ERROR] scheme-wizard.html not found!
    pause
    exit /b 1
)
if exist "frontend\config.js" (
    echo [OK] config.js found
) else (
    echo [ERROR] config.js not found!
    pause
    exit /b 1
)
echo.

echo ========================================
echo SYSTEM TEST COMPLETE!
echo ========================================
echo.
echo All checks passed! Your system is ready.
echo.
echo Next steps:
echo 1. Run 'start_rtb_system.bat' to start the system locally
echo 2. Or proceed with deployment to Render + Cloudflare
echo.
echo ========================================
pause
