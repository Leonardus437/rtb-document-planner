@echo off
echo ========================================
echo RTB Document Planner - System Startup
echo ========================================
echo.

REM Check Python
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python not found!
    echo Install Python from: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Check database
if not exist "backend\rtb_planner.db" (
    echo Database not found. Initializing...
    cd backend
    python init_database.py
    cd ..
    echo.
)

echo Starting Backend...
start "RTB Backend" cmd /k "cd backend && python -m uvicorn main:app --reload --port 5000"

timeout /t 3 /nobreak >nul

echo Starting Frontend...
start "RTB Frontend" cmd /k "cd frontend && python -m http.server 5173"

timeout /t 2 /nobreak >nul

echo.
echo ========================================
echo System Started!
echo ========================================
echo.
echo Frontend: http://localhost:5173
echo Backend:  http://localhost:5000
echo.
echo Admin: +250789751597 / admin123
echo.
echo Opening browser...
timeout /t 2 /nobreak >nul
start http://localhost:5173

echo.
echo Press any key to stop servers...
pause >nul

taskkill /FI "WindowTitle eq RTB Backend*" /T /F >nul 2>&1
taskkill /FI "WindowTitle eq RTB Frontend*" /T /F >nul 2>&1

echo Servers stopped.
pause
