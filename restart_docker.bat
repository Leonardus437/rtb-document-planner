@echo off
echo ========================================
echo RTB Document Planner - Docker Restart
echo ========================================
echo.

echo 🐳 Checking Docker installation...

REM Check if Docker is installed
docker --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker is not installed or not running
    echo Please install Docker Desktop and make sure it's running
    echo Download from: https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)

echo ✅ Docker found

REM Check if Docker is running
docker info >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker is not running
    echo Please start Docker Desktop and try again
    pause
    exit /b 1
)

echo ✅ Docker is running

REM Navigate to project directory
cd /d "%~dp0"

echo 🛑 Stopping existing containers...
docker-compose down

echo 🧹 Cleaning up old containers and images...
docker system prune -f

echo 🔨 Building and starting containers...
docker-compose up --build -d

echo ⏳ Waiting for services to start...
timeout /t 10 /nobreak >nul

echo 📊 Checking container status...
docker-compose ps

echo.
echo ========================================
echo 🎉 RTB Document Planner Docker Started
echo ========================================
echo.
echo 🌐 Frontend: http://localhost:5173
echo 🔧 Backend API: http://localhost:8000
echo 🗄️ Database: PostgreSQL on port 5433
echo.
echo 📋 Container Status:
docker-compose ps
echo.
echo 🔍 To check logs:
echo   docker-compose logs -f
echo.
echo 🛑 To stop:
echo   docker-compose down
echo.
echo Opening application in browser...
timeout /t 3 /nobreak >nul
start http://localhost:5173

pause