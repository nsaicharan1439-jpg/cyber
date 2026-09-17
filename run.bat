@echo off
setlocal

echo ========================================================
echo   Launching SentinelChain AI Platform...
echo ========================================================

if not exist ".venv\Scripts\streamlit.exe" (
    echo [!] Virtual environment not initialized or streamlit missing.
    echo [*] Running setup_env.bat first...
    call setup_env.bat
)

echo [*] Starting Streamlit Server...
.\.venv\Scripts\streamlit.exe run app.py --server.port 8501 --theme.base "dark"
pause
