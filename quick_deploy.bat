@echo off
echo ========================================
echo RTB Document Planner - Quick Deploy
echo ========================================
echo.

echo Step 1: Initialize Git Repository
echo ========================================
if not exist ".git" (
    git init
    echo Git repository initialized
) else (
    echo Git repository already exists
)
echo.

echo Step 2: Add all files
echo ========================================
git add .
echo.

echo Step 3: Commit changes
echo ========================================
git commit -m "RTB Document Planner - Production Ready - 2026"
echo.

echo ========================================
echo DEPLOYMENT INSTRUCTIONS
echo ========================================
echo.
echo BACKEND (Render):
echo 1. Push to GitHub: git remote add origin YOUR_REPO_URL
echo 2. Push: git push -u origin main
echo 3. Go to: https://render.com
echo 4. New ^> Blueprint
echo 5. Connect your repo
echo 6. Deploy automatically!
echo.
echo FRONTEND (Cloudflare Pages):
echo 1. Go to: https://dash.cloudflare.com
echo 2. Workers ^& Pages ^> Create ^> Pages
echo 3. Connect GitHub repo
echo 4. Build output: frontend
echo 5. Deploy!
echo.
echo After backend deploys:
echo - Run: prepare_deploy.bat
echo - Enter your Render backend URL
echo - Commit and push again
echo.
pause
