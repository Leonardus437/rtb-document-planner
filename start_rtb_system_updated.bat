@echo off
echo ========================================
echo    RTB Document Planner - UPDATED
echo    Starting Complete System...
echo ========================================

echo.
echo [1/3] Starting Backend Server...
start "RTB Backend" cmd /k "cd /d %~dp0backend && python -m uvicorn main:app --reload --port 5000"

echo.
echo [2/3] Waiting for backend to initialize...
timeout /t 3 /nobreak >nul

echo.
echo [3/3] Starting Frontend Server...
start "RTB Frontend" cmd /k "cd /d %~dp0frontend && python -m http.server 5173"

echo.
echo [4/4] Opening RTB System in Browser...
timeout /t 2 /nobreak >nul
start http://localhost:5173

echo.
echo ========================================
echo    RTB SYSTEM FULLY OPERATIONAL!
echo ========================================
echo.
echo Frontend: http://localhost:5173
echo Backend:  http://localhost:5000
echo API Docs: http://localhost:5000/docs
echo.
echo Admin Login:
echo Phone: +250789751597
echo Password: admin123
echo.
echo ALL IMPROVEMENTS ACTIVE:
echo - Shield word removal
echo - Tick bullet objectives
echo - 1.5 line spacing
echo - Enhanced facilitation techniques
echo - Optimized table structure
echo.
echo Press any key to exit...
pause >nul