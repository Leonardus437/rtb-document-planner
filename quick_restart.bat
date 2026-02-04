@echo off
echo Restarting RTB System...
echo.
echo Stopping any running processes...
taskkill /F /IM python.exe 2>nul
timeout /t 2 /nobreak >nul

echo Starting backend...
cd backend
start "RTB Backend" cmd /k "python -m uvicorn main:app --reload --port 5000"
timeout /t 3 /nobreak >nul

echo Starting frontend...
cd ..\frontend
start "RTB Frontend" cmd /k "python -m http.server 5173"
timeout /t 2 /nobreak >nul

echo.
echo System restarted!
echo Backend: http://localhost:5000
echo Frontend: http://localhost:5173
echo.
start http://localhost:5173
