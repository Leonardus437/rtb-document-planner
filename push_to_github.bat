@echo off
echo ========================================
echo   RTB Document Planner - GitHub Push
echo ========================================
echo.

echo Checking Git status...
git status

echo.
echo Adding all files...
git add .

echo.
echo Committing changes...
git commit -m "Add logo upload feature for Session Plans and Schemes of Work"

echo.
echo Setting up remote (if not exists)...
git remote remove origin 2>nul
git remote add origin https://github.com/Leonardus437/rtb-document-planner.git

echo.
echo Pushing to GitHub...
git branch -M main
git push -u origin main --force

echo.
echo ========================================
echo   Push Complete!
echo ========================================
echo.
echo Your code is now on GitHub:
echo https://github.com/Leonardus437/rtb-document-planner
echo.
echo Next steps:
echo 1. Go to https://render.com
echo 2. Create new Web Service
echo 3. Connect your GitHub repository
echo 4. Deploy!
echo.
pause
