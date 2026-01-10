# 🚀 Quick Start Guide

Get your rig count automation running on Railway in 5 minutes!

## Prerequisites Checklist

- [ ] Python 3.7+ installed
- [ ] Git installed ([download](https://git-scm.com/downloads))
- [ ] GitHub account
- [ ] Railway account ([sign up](https://railway.app))
- [ ] Gmail account with app password ready

## Step 1: Test Locally (2 minutes)

1. **Install dependencies:**
   ```powershell
   cd C:\Users\phill\OneDrive\Python
   pip install -r requirements.txt
   ```

2. **Create `.env` file:**
   - Copy `env_template.txt` to `.env`
   - Fill in your email credentials:
     ```
     EMAIL_ADDRESS=waldoautomationworks@gmail.com
     EMAIL_PASSWORD=jogb xaip pqdu jhdj
     TO_ADDRESS=phillip.t.flores@gmail.com
     ```

3. **Test the setup:**
   ```powershell
   python test_local.py
   ```

4. **Run a test:**
   ```powershell
   python rig_count_automation.py
   ```
   - Check your email for the chart!

## Step 2: Set Up Git Repository (1 minute)

**Option A: Use the helper script (recommended)**
```powershell
.\setup_git.ps1
```

**Option B: Manual setup**
```powershell
git init
git add rig_count_automation.py rig_count_scheduler.py requirements.txt railway.toml .gitignore README.md RAILWAY_SETUP.md env_template.txt setup_git.ps1 test_local.py QUICK_START.md
git commit -m "Initial commit: Rig count automation"
```

## Step 3: Push to GitHub (2 minutes)

1. **Create GitHub repository:**
   - Go to [github.com/new](https://github.com/new)
   - Name it: `rig-count-automation`
   - **Don't** initialize with README
   - Click "Create repository"

2. **Push your code:**
   ```powershell
   git remote add origin https://github.com/YOUR_USERNAME/rig-count-automation.git
   git branch -M main
   git push -u origin main
   ```
   *(Replace YOUR_USERNAME with your GitHub username)*

## Step 4: Deploy to Railway (2 minutes)

1. **Go to Railway:**
   - Visit [railway.app](https://railway.app)
   - Sign up/login (use GitHub for easy connection)

2. **Create new project:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Authorize Railway → Select your `rig-count-automation` repo

3. **Add environment variables:**
   - Click your project → "Variables" tab
   - Add these one by one:
     ```
     EMAIL_ADDRESS = waldoautomationworks@gmail.com
     EMAIL_PASSWORD = jogb xaip pqdu jhdj
     TO_ADDRESS = phillip.t.flores@gmail.com
     SCHEDULE_TIME = 09:00
     RUN_ON_STARTUP = true
     ```

4. **Verify deployment:**
   - Check "Deployments" → View logs
   - Look for: "Rig Count Automation Completed Successfully!"
   - Check your email for the chart!

## ✅ You're Done!

Your automation is now running on Railway and will:
- Run immediately (if `RUN_ON_STARTUP=true`)
- Run daily at the scheduled time (default: 9:00 AM UTC)
- Email you the Permian Basin rig count chart automatically

## Troubleshooting

### "Git is not recognized"
- Install Git from [git-scm.com](https://git-scm.com/downloads)
- Restart PowerShell after installation

### "Module not found" errors
- Run: `pip install -r requirements.txt`

### Email not sending
- Verify Gmail app password is correct
- Check Railway logs for errors
- Ensure 2-factor authentication is enabled on Gmail

### Need help?
- Check `RAILWAY_SETUP.md` for detailed instructions
- Check Railway logs in the dashboard
- Verify all environment variables are set

## Next Steps

- ✅ Monitor Railway logs to ensure it's working
- ✅ Adjust `SCHEDULE_TIME` if needed (UTC timezone)
- ✅ Set `RUN_ON_STARTUP=false` after first successful run (optional)

---

**Total time: ~5 minutes** ⏱️

