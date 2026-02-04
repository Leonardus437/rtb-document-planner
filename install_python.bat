@echo off
echo ========================================
echo Python Auto-Installer
echo ========================================
echo.

echo Downloading Python 3.11.9...
curl -o python-installer.exe https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Download failed! Please install manually from:
    echo https://www.python.org/downloads/
    pause
    exit /b 1
)

echo.
echo Installing Python...
echo IMPORTANT: This will install Python with PATH enabled
echo.

python-installer.exe /quiet InstallAllUsers=0 PrependPath=1 Include_test=0

echo.
echo Waiting for installation to complete...
timeout /t 30 /nobreak

echo.
echo Cleaning up...
del python-installer.exe

echo.
echo ========================================
echo Python Installation Complete!
echo ========================================
echo.
echo Please CLOSE this window and open a NEW Command Prompt
echo Then run: check_python.bat
echo.
pause
