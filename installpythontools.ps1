Write-Host "Running D:\Dropbox\Projects\BEE\venvit\Install.ps1..." -ForegroundColor Yellow
pip install --upgrade --force --no-cache-dir black
pip install --upgrade --force --no-cache-dir flake8
pip install --upgrade --force --no-cache-dir pre-commit
pre-commit install
pre-commit autoupdate
if (Test-Path -Path $env:PROJECT_DIR\pyproject.toml) { pip install --no-cache-dir -e .[dev] }
