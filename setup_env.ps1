# PowerShell Environment Setup for SentinelChain AI
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  SENTINELCHAIN AI: Environment Initialization Setup" -ForegroundColor Cyan
Write-Host "  GenAI Platform for Automated Content Transformation" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""

$hasUv = Get-Command uv -ErrorAction SilentlyContinue

if ($hasUv) {
    Write-Host "[*] Found uv package manager." -ForegroundColor Green
    if (-not (Test-Path ".venv")) {
        Write-Host "[*] Creating virtual environment (.venv) using uv..." -ForegroundColor Yellow
        uv venv .venv --python 3.12
    }
    Write-Host "[*] Installing dependencies with uv pip..." -ForegroundColor Yellow
    uv pip install -r requirements.txt --python .\.venv\Scripts\python.exe
} else {
    Write-Host "[*] uv not detected, checking system Python..." -ForegroundColor Yellow
    $hasPython = Get-Command python -ErrorAction SilentlyContinue
    if (-not $hasPython) {
        Write-Error "[!] Neither uv nor python found in PATH. Please install Python or uv."
        exit 1
    }
    if (-not (Test-Path ".venv")) {
        Write-Host "[*] Creating virtual environment (.venv)..." -ForegroundColor Yellow
        python -m venv .venv
    }
    Write-Host "[*] Installing dependencies with pip..." -ForegroundColor Yellow
    .\.venv\Scripts\python.exe -m pip install -r requirements.txt
}

if (-not (Test-Path ".env")) {
    Write-Host "[*] Generating .env configuration from template..." -ForegroundColor Gray
    Copy-Item .env.example .env
}

if (-not (Test-Path "data")) {
    New-Item -ItemType Directory -Path "data" | Out-Null
}

Write-Host ""
Write-Host "[SUCCESS] Environment initialization complete!" -ForegroundColor Green
Write-Host "[*] Start the platform anytime by running: .\run.ps1" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan
