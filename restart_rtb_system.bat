@echo off
echo ========================================
echo RTB Document Planner - System Restart
echo ========================================
echo.

echo 🔍 Checking system status...
echo.

REM Check multiple Python installations
python --version >nul 2>&1
if not errorlevel 1 (
    echo ✅ Python found: 
    python --version
    set PYTHON_CMD=python
    goto :python_found
)

python3 --version >nul 2>&1
if not errorlevel 1 (
    echo ✅ Python3 found:
    python3 --version
    set PYTHON_CMD=python3
    goto :python_found
)

py --version >nul 2>&1
if not errorlevel 1 (
    echo ✅ Python launcher found:
    py --version
    set PYTHON_CMD=py
    goto :python_found
)

echo ❌ Python not found in PATH
echo Trying to find Python installation...
where python >nul 2>&1
if not errorlevel 1 (
    echo Found Python at:
    where python
    set PYTHON_CMD=python
    goto :python_found
)

echo Please ensure Python is installed and added to PATH
echo Download from: https://www.python.org/downloads/
pause
exit /b 1

:python_found
echo.

REM Navigate to frontend directory
cd /d "%~dp0frontend"

echo 🌐 Starting frontend server for system check...
start "RTB Frontend" cmd /k "%PYTHON_CMD% -m http.server 5173"

REM Wait for server to start
timeout /t 3 /nobreak >nul

echo 📊 Opening system status check...
start http://localhost:5173/system-status-check.html

echo.
echo ========================================
echo 🎯 RTB Document Planner Status Check
echo ========================================
echo.
echo 📍 System Check: http://localhost:5173/system-status-check.html
echo 🌐 Main App: http://localhost:5173/index.html
echo 🔧 Backend: https://leonardus437.pythonanywhere.com
echo.
echo The system status page will show:
echo ✅ Backend connection (PythonAnywhere)
echo ✅ Frontend configuration
echo ✅ Authentication system
echo ✅ Document generation
echo.
echo If all checks pass, click "Launch RTB Planner"
echo.
echo To stop the frontend server:
echo - Close the frontend command window
echo - Or press Ctrl+C in the window
echo.
pause