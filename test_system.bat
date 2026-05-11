@echo off
echo ========================================
echo RTB Document Planner - System Test
echo ========================================
echo.

REM Test 1: Python Installation
echo [1/8] Testing Python...
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [FAIL] Python not installed
    pause
    exit /b 1
)
python --version
echo [PASS] Python installed
echo.

REM Test 2: Backend Dependencies
echo [2/8] Testing Backend Dependencies...
cd backend
pip show fastapi >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [FAIL] Dependencies missing. Run install.bat
    cd ..
    pause
    exit /b 1
)
echo [PASS] Dependencies installed
cd ..
echo.

REM Test 3: Database
echo [3/8] Testing Database...
if not exist "backend\rtb_planner.db" (
    echo [WARN] Database not found. Creating...
    cd backend
    python init_database.py
    cd ..
)
if exist "backend\rtb_planner.db" (
    echo [PASS] Database exists
) else (
    echo [FAIL] Database creation failed
    pause
    exit /b 1
)
echo.

REM Test 4: Backend Files
echo [4/8] Testing Backend Files...
set BACKEND_OK=1
if not exist "backend\main.py" set BACKEND_OK=0
if not exist "backend\models.py" set BACKEND_OK=0
if not exist "backend\database.py" set BACKEND_OK=0
if not exist "backend\document_generator.py" set BACKEND_OK=0
if %BACKEND_OK%==0 (
    echo [FAIL] Backend files missing
    pause
    exit /b 1
)
echo [PASS] Backend files present
echo.

REM Test 5: Frontend Files
echo [5/8] Testing Frontend Files...
set FRONTEND_OK=1
if not exist "frontend\index.html" set FRONTEND_OK=0
if not exist "frontend\login.html" set FRONTEND_OK=0
if not exist "frontend\wizard.html" set FRONTEND_OK=0
if not exist "frontend\scheme-wizard.html" set FRONTEND_OK=0
if %FRONTEND_OK%==0 (
    echo [FAIL] Frontend files missing
    pause
    exit /b 1
)
echo [PASS] Frontend files present
echo.

REM Test 6: Start Backend
echo [6/8] Testing Backend Server...
cd backend
start /B python -m uvicorn main:app --port 5000 > nul 2>&1
timeout /t 5 /nobreak >nul
cd ..

REM Check if backend is running
curl -s http://localhost:5000/api >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [FAIL] Backend server not responding
    taskkill /F /IM python.exe >nul 2>&1
    pause
    exit /b 1
)
echo [PASS] Backend server running
echo.

REM Test 7: API Endpoints
echo [7/8] Testing API Endpoints...
curl -s http://localhost:5000/api | find "online" >nul
if %ERRORLEVEL% NEQ 0 (
    echo [FAIL] API not responding correctly
    taskkill /F /IM python.exe >nul 2>&1
    pause
    exit /b 1
)
echo [PASS] API endpoints working
echo.

REM Test 8: Cleanup
echo [8/8] Cleaning up...
taskkill /F /IM python.exe >nul 2>&1
timeout /t 2 /nobreak >nul
echo [PASS] Cleanup complete
echo.

echo ========================================
echo ALL TESTS PASSED!
echo ========================================
echo.
echo System is ready for deployment!
echo.
echo Next Steps:
echo 1. Deploy backend to Render
echo 2. Deploy frontend to Cloudflare Pages
echo 3. Update API URLs in frontend
echo.
pause
