@echo off
echo ========================================
echo RTB Document Planner - Minimal Install
echo ========================================
echo.

cd backend

echo Installing core dependencies...
python -m pip install fastapi==0.104.1
python -m pip install "uvicorn[standard]==0.24.0"
python -m pip install sqlalchemy==2.0.23
python -m pip install python-multipart==0.0.6
python -m pip install python-docx

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

cd ..
pause
