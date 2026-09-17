@echo off
setlocal enabledelayedexpansion

echo ========================================================
echo   SENTINELCHAIN AI: Environment Initialization Setup
echo   GenAI Platform for Automated Content Transformation
echo ========================================================
echo.

where uv >nul 2>nul
if %ERRORLEVEL% equ 0 (
    echo [*] Detected uv fast Python package manager.
    if not exist ".venv" (
        echo [*] Creating virtual environment (.venv) using uv...
        uv venv .venv --python 3.12
    )
    echo [*] Installing dependencies via uv pip...
    uv pip install -r requirements.txt --python .\.venv\Scripts\python.exe
) else (
    echo [*] uv not found, checking system Python...
    where python >nul 2>nul
    if %ERRORLEVEL% neq 0 (
        echo [!] Python is not found in PATH. Please install Python or uv.
        pause
        exit /b 1
    )
    if not exist ".venv" (
        echo [*] Creating virtual environment (.venv) with python -m venv...
        python -m venv .venv
    )
    echo [*] Installing dependencies via pip...
    .\.venv\Scripts\python.exe -m pip install --upgrade pip
    .\.venv\Scripts\python.exe -m pip install -r requirements.txt
)

if not exist ".env" (
    echo [*] Copying .env.example to .env...
    copy .env.example .env
)

if not exist "data" (
    mkdir data
)

echo.
echo [SUCCESS] Environment successfully prepared!
echo [*] Launch the platform anytime using 'run.bat' or 'run.ps1'.
echo ========================================================
pause
