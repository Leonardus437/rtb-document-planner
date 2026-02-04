@echo off
echo ========================================
echo RTB DOCUMENT PLANNER
echo DEPLOYMENT PREPARATION
echo ========================================
echo.

echo This script will prepare your project for deployment to:
echo - Backend: Render (with PostgreSQL)
echo - Frontend: Cloudflare Pages
echo.
pause

:: Step 1: Test system
echo.
echo [Step 1/5] Testing local system...
call test_and_verify_system.bat
if %errorlevel% neq 0 (
    echo [ERROR] System test failed! Fix issues before deploying.
    pause
    exit /b 1
)

:: Step 2: Check Git
echo.
echo [Step 2/5] Checking Git repository...
git status >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] Not a Git repository. Initialize Git first:
    echo   git init
    echo   git add .
    echo   git commit -m "Initial commit"
    echo   git remote add origin YOUR_GITHUB_URL
    echo   git push -u origin main
    pause
) else (
    echo [OK] Git repository found
    echo.
    echo Current status:
    git status --short
)

:: Step 3: Create deployment files
echo.
echo [Step 3/5] Checking deployment files...
if exist "render.yaml" (
    echo [OK] render.yaml exists
) else (
    echo [ERROR] render.yaml not found!
    pause
    exit /b 1
)

if exist "frontend\_headers" (
    echo [OK] _headers exists
) else (
    echo [WARNING] _headers not found (optional)
)

if exist "frontend\_redirects" (
    echo [OK] _redirects exists
) else (
    echo [INFO] Creating _redirects file...
    echo /api/* https://rtb-planner-backend.onrender.com/:splat 200 > frontend\_redirects
    echo /* /index.html 200 >> frontend\_redirects
    echo [OK] _redirects created
)

:: Step 4: Backup database
echo.
echo [Step 4/5] Backing up local database...
if exist "backend\rtb_planner.db" (
    copy "backend\rtb_planner.db" "backend\rtb_planner_backup_%date:~-4,4%%date:~-10,2%%date:~-7,2%.db" >nul
    echo [OK] Database backed up
) else (
    echo [INFO] No local database to backup
)

:: Step 5: Summary
echo.
echo [Step 5/5] Deployment preparation complete!
echo.
echo ========================================
echo NEXT STEPS:
echo ========================================
echo.
echo 1. COMMIT TO GITHUB (if not done):
echo    git add .
echo    git commit -m "Ready for deployment"
echo    git push origin main
echo.
echo 2. DEPLOY BACKEND TO RENDER:
echo    - Go to https://render.com
echo    - Create PostgreSQL database
echo    - Create Web Service from GitHub
echo    - Follow DEPLOYMENT_GUIDE_COMPLETE.md
echo.
echo 3. DEPLOY FRONTEND TO CLOUDFLARE:
echo    - Update frontend/config.js with Render URL
echo    - Go to https://pages.cloudflare.com
echo    - Create project from GitHub
echo    - Deploy frontend/ directory
echo.
echo 4. TEST DEPLOYMENT:
echo    - Test backend API
echo    - Test frontend application
echo    - Create test documents
echo.
echo ========================================
echo.
echo Full guide: DEPLOYMENT_GUIDE_COMPLETE.md
echo.
pause
