@echo off
echo Checking Python installation...
echo.

python --version 2>nul
if %ERRORLEVEL% EQU 0 (
    echo [OK] Python is installed
    python --version
) else (
    echo [ERROR] Python is NOT installed or not in PATH
    echo.
    echo Please install Python 3.8+ from:
    echo https://www.python.org/downloads/
    echo.
    echo IMPORTANT: Check "Add Python to PATH" during installation!
    goto :end
)

echo.
echo Checking pip...
python -m pip --version 2>nul
if %ERRORLEVEL% EQU 0 (
    echo [OK] pip is available
) else (
    echo [ERROR] pip is not available
    goto :end
)

echo.
echo ========================================
echo Your system is ready!
echo ========================================
echo.
echo Next step: Run install.bat
echo.

:end
pause
