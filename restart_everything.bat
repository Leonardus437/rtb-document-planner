@echo off
echo ========================================
echo RTB DOCUMENT PLANNER - COMPLETE RESTART
echo ========================================
echo.

echo [1/4] Stopping all Python processes...
taskkill /F /IM python.exe 2>nul
taskkill /F /IM pythonw.exe 2>nul
timeout /t 3 /nobreak >nul

echo [2/4] Cleaning up...
cd backend
if exist __pycache__ rmdir /s /q __pycache__
cd ..
timeout /t 1 /nobreak >nul

echo [3/4] Starting Backend Server...
cd backend
start "RTB Backend" cmd /k "python -m uvicorn main:app --reload --port 5000"
cd ..
echo Waiting for backend to initialize...
timeout /t 5 /nobreak >nul

echo [4/4] Starting Frontend Server...
cd frontend
start "RTB Frontend" cmd /k "python -m http.server 5173"
cd ..
echo Waiting for frontend to initialize...
timeout /t 3 /nobreak >nul

echo.
echo ========================================
echo SYSTEM RESTARTED SUCCESSFULLY!
echo ========================================
echo.
echo Backend API: http://localhost:5000
echo Frontend UI: http://localhost:5173
echo API Docs: http://localhost:5000/docs
echo.
echo Opening browser...
timeout /t 2 /nobreak >nul
start http://localhost:5173

echo.
echo Press any key to close this window...
pause >nul
