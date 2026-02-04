@echo off
echo ========================================
echo RTB DOCUMENT PLANNER - DOCKER STARTUP
echo ========================================
echo.

:: Check if Docker is installed
echo [1/4] Checking Docker installation...
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Docker not found! Please install Docker Desktop:
    echo https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)
docker --version
echo [OK] Docker installed
echo.

:: Check if Docker is running
echo [2/4] Checking Docker status...
docker ps >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Docker is not running! Please start Docker Desktop.
    pause
    exit /b 1
)
echo [OK] Docker is running
echo.

:: Stop existing containers
echo [3/4] Stopping existing containers...
docker-compose down >nul 2>&1
echo [OK] Cleaned up
echo.

:: Start services
echo [4/4] Starting RTB Document Planner with Docker...
echo.
echo This will start:
echo - PostgreSQL Database (port 5432)
echo - Backend API (port 5000)
echo - Frontend (port 5173)
echo.
docker-compose up -d

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Failed to start services!
    echo.
    echo Troubleshooting:
    echo 1. Check if ports 5000, 5173, 5432 are available
    echo 2. Run: docker-compose logs
    echo 3. Check Docker Desktop for errors
    pause
    exit /b 1
)

echo.
echo ========================================
echo SERVICES STARTED SUCCESSFULLY!
echo ========================================
echo.
echo Waiting for services to be ready...
timeout /t 10 /nobreak >nul

:: Check service health
echo.
echo Checking service health...
docker-compose ps

echo.
echo ========================================
echo ACCESS YOUR APPLICATION:
echo ========================================
echo.
echo Frontend: http://localhost:5173
echo Backend API: http://localhost:5000
echo API Docs: http://localhost:5000/docs
echo PostgreSQL: localhost:5432
echo.
echo Admin Login:
echo Phone: +250789751597
echo Password: admin123
echo.
echo ========================================
echo USEFUL COMMANDS:
echo ========================================
echo.
echo View logs:        docker-compose logs -f
echo Stop services:    docker-compose down
echo Restart:          docker-compose restart
echo Check status:     docker-compose ps
echo.
echo Opening browser...
timeout /t 3 /nobreak >nul
start http://localhost:5173

echo.
echo Press any key to view logs (Ctrl+C to exit logs)...
pause >nul
docker-compose logs -f
