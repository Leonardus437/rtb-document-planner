@echo off
echo ========================================
echo RTB Document Planner - Docker Status
echo ========================================
echo.

REM Check if Docker is available
docker --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker is not installed
    echo Please install Docker Desktop from: https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)

echo ✅ Docker version:
docker --version

REM Check if Docker is running
docker info >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker is not running
    echo Please start Docker Desktop and try again
    pause
    exit /b 1
)

echo ✅ Docker is running

echo.
echo 📊 Container Status:
echo ========================================
docker-compose ps

echo.
echo 🔍 Service Health Check:
echo ========================================

REM Check backend
echo 🔧 Backend (http://localhost:8000):
curl -s http://localhost:8000/ >nul 2>&1
if errorlevel 1 (
    echo ❌ Backend not responding
) else (
    echo ✅ Backend is healthy
)

REM Check frontend
echo 🌐 Frontend (http://localhost:5173):
curl -s http://localhost:5173/ >nul 2>&1
if errorlevel 1 (
    echo ❌ Frontend not responding
) else (
    echo ✅ Frontend is healthy
)

REM Check database
echo 🗄️ Database (PostgreSQL):
docker-compose exec -T db pg_isready -U rtb_user >nul 2>&1
if errorlevel 1 (
    echo ❌ Database not ready
) else (
    echo ✅ Database is ready
)

echo.
echo 📋 Container Logs (last 10 lines):
echo ========================================
echo.
echo 🔧 Backend logs:
docker-compose logs --tail=5 backend

echo.
echo 🌐 Frontend logs:
docker-compose logs --tail=5 frontend

echo.
echo 🗄️ Database logs:
docker-compose logs --tail=5 db

echo.
echo 💡 Useful commands:
echo   - View live logs: docker-compose logs -f
echo   - Restart services: docker-compose restart
echo   - Stop all: docker-compose down
echo   - Rebuild: docker-compose up --build -d
echo.
pause