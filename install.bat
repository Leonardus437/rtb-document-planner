@echo off
echo ========================================
echo RTB Document Planner - Installation
echo ========================================
echo.

echo Checking Python installation...
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Python is not installed or not in PATH!
    echo.
    echo Please install Python 3.8+ from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)

echo Python found!
echo.
echo Installing dependencies...
cd backend
python -m pip install -r requirements.txt

if %ERRORLEVEL% EQU 0 (
    echo.
    echo Dependencies installed!
    echo.
    echo Initializing database...
    python init_database.py
    
    echo.
    echo ========================================
    echo Installation Complete!
    echo ========================================
    echo.
    echo Next: Run start_rtb_system.bat
    echo.
) else (
    echo.
    echo Installation failed!
    echo Try: python -m pip install --upgrade pip
    echo.
)

cd ..
pause
