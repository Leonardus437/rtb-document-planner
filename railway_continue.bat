@echo off
echo ========================================
echo Railway Project Already Exists!
echo ========================================
echo.
echo Your Railway project:
echo https://railway.com/project/4f2bd0e5-4c93-4d3f-8970-f1c0c1a47dc8
echo.
echo ========================================
echo NEXT STEPS:
echo ========================================
echo.
echo 1. GET BACKEND URL
echo    - Go to Railway project
echo    - Settings -^> Domains
echo    - Generate Domain (if needed)
echo    - Copy the URL
echo.
echo 2. UPDATE FRONTEND
echo    - Run: prepare_deploy.bat
echo    - Enter your Railway URL
echo.
echo 3. PUSH TO GITHUB
echo    - git add .
echo    - git commit -m "Update for Railway"
echo    - git push origin main
echo.
echo 4. DEPLOY FRONTEND
echo    - Go to: https://dash.cloudflare.com
echo    - Deploy frontend from GitHub
echo.
echo Full guide: RAILWAY_EXISTING.md
echo.
pause
