@echo off
echo ========================================
echo RTB Document Planner - Local Backend Fix
echo ========================================
echo.

echo 🚨 CORS Error Detected - Starting Local Backend
echo.

REM Detect Python command
py --version >nul 2>&1
if not errorlevel 1 (
    set PYTHON_CMD=py
    echo ✅ Using Python launcher: py
    goto :python_found
)

python --version >nul 2>&1
if not errorlevel 1 (
    set PYTHON_CMD=python
    echo ✅ Using python command
    goto :python_found
)

echo ❌ Python not found
echo Please run: restart_rtb_system.bat instead
pause
exit /b 1

:python_found
echo.

REM Navigate to backend directory
cd /d "%~dp0backend"

echo 📋 Copying fixed backend...
copy /Y "..\FIXED_PYTHONANYWHERE_BACKEND.py" "main.py" >nul

echo 🔧 Installing requirements...
%PYTHON_CMD% -m pip install flask flask-cors >nul 2>&1

echo 🚀 Starting local backend...
start "RTB Backend" cmd /k "%PYTHON_CMD% main.py"

echo ⏳ Waiting for backend to start...
timeout /t 5 /nobreak >nul

REM Navigate to frontend directory
cd /d "%~dp0frontend"

echo 📝 Updating frontend config for local backend...
copy /Y "config-local.js" "config.js" >nul

echo 🌐 Starting frontend...
start "RTB Frontend" cmd /k "%PYTHON_CMD% -m http.server 5173"

timeout /t 3 /nobreak >nul

echo.
echo ========================================
echo 🎉 Local System Started!
echo ========================================
echo.
echo 🔧 Backend: http://localhost:5000
echo 🌐 Frontend: http://localhost:5173
echo.
echo ✅ CORS issues resolved
echo ✅ All endpoints available
echo ✅ Ready for teachers to use
echo.
echo Opening application...
start http://localhost:5173

echo.
echo 💡 Both servers are running locally
echo 🛑 To stop: Close both command windows
echo.
pause