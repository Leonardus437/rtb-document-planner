@echo off
echo ========================================
echo RTB Document Planner - Smart Restart
echo ========================================
echo.

echo 🔍 Detecting system configuration...

REM Check if Docker is available
docker --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker not found - Using PythonAnywhere backend
    goto :no_docker
) else (
    echo ✅ Docker found
)

docker info >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker not running - Using PythonAnywhere backend
    goto :no_docker
) else (
    echo ✅ Docker is running
)

echo.
echo 🐳 Docker is available! Choose your option:
echo.
echo 1. Run with Docker (Full local system)
echo 2. Run without Docker (PythonAnywhere backend)
echo 3. System status check only
echo.
set /p choice="Enter your choice (1-3): "

if "%choice%"=="1" goto :docker_mode
if "%choice%"=="2" goto :no_docker
if "%choice%"=="3" goto :status_check
goto :no_docker

:docker_mode
echo.
echo 🐳 Starting Docker containers...
echo.

REM Copy Docker config for frontend
copy /Y "frontend\config-docker.js" "frontend\config.js" >nul

REM Stop existing containers
docker-compose down

REM Build and start containers
docker-compose up --build -d

echo ⏳ Waiting for containers to start...
timeout /t 15 /nobreak >nul

echo 📊 Container status:
docker-compose ps

echo.
echo ========================================
echo 🎉 Docker containers started!
echo ========================================
echo.
echo 🌐 Frontend: http://localhost:5173
echo 🔧 Backend: http://localhost:8000
echo 🗄️ Database: PostgreSQL (internal)
echo.
echo Opening application...
start http://localhost:5173
goto :end

:no_docker
echo.
echo 🌐 Using PythonAnywhere backend...
echo.

REM Copy production config for frontend
copy /Y "frontend\config-production.js" "frontend\config.js" >nul 2>nul
if errorlevel 1 (
    echo 📝 Using existing production config
) else (
    echo ✅ Production config applied
)

REM Navigate to frontend directory
cd /d "%~dp0frontend"

echo 🌐 Starting frontend server...
start "RTB Frontend" cmd /k "python -m http.server 5173"

timeout /t 3 /nobreak >nul

echo.
echo ========================================
echo 🎉 System started with PythonAnywhere!
echo ========================================
echo.
echo 🌐 Frontend: http://localhost:5173
echo 🔧 Backend: https://leonardus437.pythonanywhere.com
echo.
echo Opening system status check...
start http://localhost:5173/system-status-check.html
goto :end

:status_check
echo.
echo 📊 Opening system status check...
echo.

cd /d "%~dp0frontend"
start "RTB Frontend" cmd /k "python -m http.server 5173"
timeout /t 3 /nobreak >nul
start http://localhost:5173/system-status-check.html
goto :end

:end
echo.
echo 💡 Useful commands:
echo   - Docker logs: docker-compose logs -f
echo   - Stop Docker: docker-compose down
echo   - Restart: Run this script again
echo.
pause