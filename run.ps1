# PowerShell Launcher for SentinelChain AI
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  Launching SentinelChain AI Platform..." -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan

if (-not (Test-Path ".\.venv\Scripts\streamlit.exe")) {
    Write-Host "[!] Virtual environment not detected. Running .\setup_env.ps1..." -ForegroundColor Yellow
    .\setup_env.ps1
}

Write-Host "[*] Starting Streamlit Server at http://localhost:8501" -ForegroundColor Green
.\.venv\Scripts\streamlit.exe run app.py --server.port 8501 --theme.base "dark"
