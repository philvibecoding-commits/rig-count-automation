# PowerShell script to initialize git repository for rig count automation
# Run this script to set up git and prepare for GitHub/Railway deployment

Write-Host "🚀 Setting up Git Repository for Rig Count Automation" -ForegroundColor Cyan
Write-Host "=" * 60 -ForegroundColor Cyan

# Check if git is installed
try {
    $gitVersion = git --version
    Write-Host "✅ Git found: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Git is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Git from https://git-scm.com/downloads" -ForegroundColor Yellow
    exit 1
}

# Check if already a git repository
if (Test-Path .git) {
    Write-Host "⚠️  Git repository already initialized" -ForegroundColor Yellow
    $continue = Read-Host "Continue anyway? (y/n)"
    if ($continue -ne "y") {
        exit 0
    }
} else {
    Write-Host "📦 Initializing git repository..." -ForegroundColor Cyan
    git init
}

# Add files
Write-Host "`n📝 Adding files to git..." -ForegroundColor Cyan
git add rig_count_automation.py
git add rig_count_scheduler.py
git add requirements.txt
git add railway.toml
git add .gitignore
git add README.md
git add RAILWAY_SETUP.md
git add env_template.txt
git add setup_git.ps1

# Check status
Write-Host "`n📊 Git status:" -ForegroundColor Cyan
git status

# Ask about commit
Write-Host "`n💾 Ready to commit?" -ForegroundColor Cyan
$commit = Read-Host "Enter commit message (or press Enter for default)"

if ([string]::IsNullOrWhiteSpace($commit)) {
    $commit = "Initial commit: Rig count automation for Railway"
}

git commit -m $commit

Write-Host "`n✅ Git repository initialized and committed!" -ForegroundColor Green
Write-Host "`n📋 Next steps:" -ForegroundColor Yellow
Write-Host "1. Create a GitHub repository at https://github.com/new" -ForegroundColor White
Write-Host "2. Run these commands:" -ForegroundColor White
Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/rig-count-automation.git" -ForegroundColor Gray
Write-Host "   git branch -M main" -ForegroundColor Gray
Write-Host "   git push -u origin main" -ForegroundColor Gray
Write-Host "3. Deploy to Railway from GitHub" -ForegroundColor White
Write-Host "`nSee RAILWAY_SETUP.md for detailed instructions!" -ForegroundColor Cyan

