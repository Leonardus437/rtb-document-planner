@echo off
echo ========================================
echo RTB - Final Install
echo ========================================
echo.

cd backend

echo Upgrading SQLAlchemy for Python 3.14...
python -m pip install --upgrade sqlalchemy

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
