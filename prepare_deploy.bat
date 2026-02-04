@echo off
echo ========================================
echo RTB Document Planner - Deploy Prep
echo ========================================
echo.

set /p BACKEND_URL="Enter your Render backend URL (e.g., https://rtb-planner-backend.onrender.com): "

if "%BACKEND_URL%"=="" (
    echo ERROR: Backend URL is required
    pause
    exit /b 1
)

echo.
echo Updating frontend configuration...

REM Create production config
(
echo // API Configuration - PRODUCTION
echo const CONFIG = {
echo     API_URL: '%BACKEND_URL%',
echo };
echo.
echo if ^(typeof module !== 'undefined' ^&^& module.exports^) {
echo     module.exports = CONFIG;
echo }
) > frontend\config.js

echo [DONE] Frontend configured for production
echo.
echo Backend URL: %BACKEND_URL%
echo.
echo ========================================
echo Next Steps:
echo ========================================
echo 1. Commit changes: git add . ^&^& git commit -m "Production config"
echo 2. Push to GitHub: git push origin main
echo 3. Deploy frontend to Cloudflare Pages
echo.
echo Your frontend will now connect to: %BACKEND_URL%
echo.
pause
