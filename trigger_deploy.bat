@echo off
echo ========================================
echo Trigger Railway Deployment
echo ========================================
echo.
echo Your Railway URL: web-production-df3e5.up.railway.app
echo.
echo Pushing to GitHub to trigger deployment...
echo.

git add .
git commit -m "Trigger Railway deployment - RTB Planner 2026"
git push origin main

echo.
echo ========================================
echo Deployment Triggered!
echo ========================================
echo.
echo Railway will auto-deploy in 2-3 minutes
echo.
echo Check status at:
echo https://railway.com/project/4f2bd0e5-4c93-4d3f-8970-f1c0c1a47dc8
echo.
echo Your backend URL:
echo https://web-production-df3e5.up.railway.app
echo.
pause
