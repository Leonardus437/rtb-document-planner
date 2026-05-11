@echo off
echo Resetting database to remove premium features...
echo.

cd backend

echo Deleting old database...
if exist rtb_planner.db del rtb_planner.db

echo Creating new database...
python init_database.py

echo.
echo Database reset complete!
echo System is now completely free - unlimited documents for everyone!
echo.

cd ..
pause
