@echo off
echo ========================================
echo RTB Document Planner - Simple Fix
echo ========================================
echo.

echo 🎯 Manual Steps to Fix CORS Issue:
echo.
echo 1. Open TWO command prompts
echo 2. In first prompt, run these commands:
echo.
echo    cd /d "%~dp0backend"
echo    copy ..\FIXED_PYTHONANYWHERE_BACKEND.py main.py
echo    py -m pip install flask flask-cors
echo    py main.py
echo.
echo 3. In second prompt, run these commands:
echo.
echo    cd /d "%~dp0frontend"
echo    copy config-local.js config.js
echo    py -m http.server 5173
echo.
echo 4. Open browser: http://localhost:5173
echo.
echo ========================================
echo 🚀 Quick Alternative - Use Docker
echo ========================================
echo.
echo If you have Docker installed:
echo    docker-compose up --build
echo.
echo Then open: http://localhost:5173
echo.
echo ========================================
echo 💡 Or Fix PythonAnywhere Backend
echo ========================================
echo.
echo 1. Go to: https://www.pythonanywhere.com/user/leonardus437/
echo 2. Replace main.py with FIXED_PYTHONANYWHERE_BACKEND.py
echo 3. Reload web app
echo 4. Use original config (PythonAnywhere backend)
echo.
pause

REM Try to open the directories for manual setup
start "" "%~dp0backend"
start "" "%~dp0frontend"