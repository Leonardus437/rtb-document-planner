@echo off
echo Searching for Python installation...
echo.

REM Check common Python locations
set PYTHON_PATH=

if exist "C:\Python311\python.exe" set PYTHON_PATH=C:\Python311
if exist "C:\Python312\python.exe" set PYTHON_PATH=C:\Python312
if exist "C:\Python310\python.exe" set PYTHON_PATH=C:\Python310
if exist "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" set PYTHON_PATH=%LOCALAPPDATA%\Programs\Python\Python311
if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" set PYTHON_PATH=%LOCALAPPDATA%\Programs\Python\Python312
if exist "%LOCALAPPDATA%\Programs\Python\Python310\python.exe" set PYTHON_PATH=%LOCALAPPDATA%\Programs\Python\Python310
if exist "C:\Program Files\Python311\python.exe" set PYTHON_PATH=C:\Program Files\Python311
if exist "C:\Program Files\Python312\python.exe" set PYTHON_PATH=C:\Program Files\Python312

if "%PYTHON_PATH%"=="" (
    echo Python not found in common locations.
    echo.
    echo Please find python.exe manually and note the folder path.
    echo Then run: setx PATH "%%PATH%%;C:\YourPythonPath"
    pause
    exit /b 1
)

echo Found Python at: %PYTHON_PATH%
echo.
echo Adding to PATH...

setx PATH "%PATH%;%PYTHON_PATH%;%PYTHON_PATH%\Scripts"

echo.
echo ========================================
echo PATH Updated!
echo ========================================
echo.
echo IMPORTANT: Close this window and open a NEW Command Prompt
echo Then run: check_python.bat
echo.
pause
