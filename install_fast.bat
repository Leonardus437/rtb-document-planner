@echo off
echo ========================================
echo RTB Document Planner - Fast Install
echo ========================================
echo.

cd backend

echo Installing dependencies (this may take 2-3 minutes)...
echo.

python -m pip install --upgrade pip
python -m pip install fastapi==0.104.1
python -m pip install "uvicorn[standard]==0.24.0"
python -m pip install sqlalchemy==2.0.23
python -m pip install pydantic==2.5.0
python -m pip install python-multipart==0.0.6
python -m pip install python-docx==1.1.0
python -m pip install lxml==4.9.3

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
    echo.
)

cd ..
pause
