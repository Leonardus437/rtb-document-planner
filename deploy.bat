@echo off
cls
echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║                                                            ║
echo ║        RTB DOCUMENT PLANNER - DEPLOY TO PRODUCTION        ║
echo ║                                                            ║
echo ╚════════════════════════════════════════════════════════════╝
echo.
echo.

echo [STEP 1] Testing system locally...
echo.
call test_system.bat
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ Tests failed! Fix issues before deploying.
    pause
    exit /b 1
)

echo.
echo ✅ All tests passed!
echo.
echo.

echo [STEP 2] Preparing Git repository...
echo.

if not exist ".git" (
    git init
    echo ✅ Git initialized
) else (
    echo ✅ Git already initialized
)

git add .
git commit -m "RTB Document Planner - Production Ready 2026"

echo.
echo ✅ Files committed
echo.
echo.

echo ╔════════════════════════════════════════════════════════════╗
echo ║                    NEXT STEPS                              ║
echo ╚════════════════════════════════════════════════════════════╝
echo.
echo 1. CREATE GITHUB REPOSITORY
echo    - Go to: https://github.com/new
echo    - Name: rtb-planner
echo    - Click: Create repository
echo.
echo 2. PUSH TO GITHUB
echo    Run these commands:
echo.
echo    git remote add origin https://github.com/YOUR_USERNAME/rtb-planner.git
echo    git push -u origin main
echo.
echo 3. DEPLOY BACKEND (Railway)
echo    - Go to: https://railway.app
echo    - New Project ^> Deploy from GitHub repo
echo    - Select your repo
echo    - Add PostgreSQL database
echo    - Click Deploy
echo.
echo 4. DEPLOY FRONTEND (Cloudflare)
echo    - Go to: https://dash.cloudflare.com
echo    - Workers ^& Pages ^> Create ^> Pages
echo    - Connect repo
echo    - Build output: frontend
echo.
echo 5. CONFIGURE
echo    - Run: prepare_deploy.bat
echo    - Enter your Railway backend URL
echo    - Push changes again
echo.
echo.
echo 📖 Full guide: DEPLOY_NOW.md
echo ✅ Checklist: DEPLOYMENT_CHECKLIST.txt
echo.
pause
