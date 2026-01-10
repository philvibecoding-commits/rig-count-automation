# Railway Setup Guide - Rig Count Automation

## Quick Start Checklist

- [ ] Code is ready (all files committed)
- [ ] GitHub repository created
- [ ] Railway account created
- [ ] Environment variables configured
- [ ] Deployment successful

## Step-by-Step Railway Deployment

### Step 1: Prepare Your Code

1. **Ensure all files are ready:**
   - ✅ `rig_count_automation.py`
   - ✅ `rig_count_scheduler.py`
   - ✅ `requirements.txt`
   - ✅ `railway.toml`
   - ✅ `.gitignore`
   - ✅ `.env.example`

2. **Test locally first:**
   ```bash
   python rig_count_automation.py
   ```

### Step 2: Initialize Git Repository

```bash
# Navigate to project directory
cd C:\Users\phill\OneDrive\Python

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Rig count automation for Railway"
```

### Step 3: Create GitHub Repository

1. Go to [github.com](https://github.com) and sign in
2. Click "New repository"
3. Name it: `rig-count-automation` (or your preferred name)
4. **Don't** initialize with README (you already have one)
5. Click "Create repository"

### Step 4: Push to GitHub

```bash
# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/rig-count-automation.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 5: Deploy to Railway

1. **Go to Railway:**
   - Visit [railway.app](https://railway.app)
   - Sign up/login (can use GitHub account)

2. **Create New Project:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Authorize Railway to access your GitHub if needed
   - Select your `rig-count-automation` repository

3. **Railway will automatically:**
   - Detect Python
   - Install dependencies from `requirements.txt`
   - Start the service using `railway.toml` configuration

### Step 6: Configure Environment Variables

1. **In Railway Dashboard:**
   - Click on your project
   - Go to "Variables" tab
   - Click "New Variable"

2. **Add these variables one by one:**

   ```
   EMAIL_ADDRESS = waldoautomationworks@gmail.com
   EMAIL_PASSWORD = jogb xaip pqdu jhdj
   TO_ADDRESS = phillip.t.flores@gmail.com
   SCHEDULE_TIME = 09:00
   RUN_ON_STARTUP = true
   ```

3. **Save** - Railway will automatically redeploy

### Step 7: Verify Deployment

1. **Check Logs:**
   - In Railway dashboard, click "Deployments"
   - Click on the latest deployment
   - View logs to see if it's running successfully

2. **Look for:**
   - ✅ "Rig Count Scheduler initialized"
   - ✅ "Running initial job on startup..."
   - ✅ "Rig Count Automation Completed Successfully!"

3. **Check Email:**
   - You should receive an email with the chart if `RUN_ON_STARTUP=true`

## Railway Configuration Explained

### `railway.toml`
```toml
[build]
builder = "NIXPACKS"  # Railway's automatic builder

[deploy]
startCommand = "python rig_count_scheduler.py"  # What runs when service starts
restartPolicyType = "ON_FAILURE"  # Restart if it crashes
restartPolicyMaxRetries = 10  # Try 10 times before giving up
```

### How It Works

1. **Railway detects** Python project from `requirements.txt`
2. **Installs dependencies** automatically
3. **Runs** `rig_count_scheduler.py` which:
   - Runs the automation immediately (if `RUN_ON_STARTUP=true`)
   - Schedules daily runs at `SCHEDULE_TIME`
   - Keeps the service running continuously

## Monitoring & Maintenance

### View Logs
- Railway Dashboard → Your Project → Deployments → View Logs
- Or use Railway CLI: `railway logs`

### Update Code
```bash
# Make changes locally
git add .
git commit -m "Update: description of changes"
git push

# Railway automatically redeploys!
```

### Manual Trigger (if needed)
- Railway Dashboard → Your Project → Deployments → "Redeploy"

## Troubleshooting

### Service Keeps Restarting
- Check logs for errors
- Verify environment variables are set correctly
- Ensure email credentials are valid

### No Email Received
- Check Railway logs for email sending errors
- Verify Gmail app password is correct
- Check spam folder

### Schedule Not Working
- Verify `SCHEDULE_TIME` is in correct format (HH:MM)
- Check timezone (Railway uses UTC)
- Ensure scheduler is running (check logs)

## Cost

Railway offers:
- **Free tier**: $5/month credit
- **Hobby plan**: $5/month (if you exceed free tier)
- This project should stay within free tier limits

## Next Steps

- ✅ Set up monitoring/alerting if needed
- ✅ Consider adding error notifications
- ✅ Set up backup email service (optional)
- ✅ Add more charts/analysis (optional)

## Support

If you encounter issues:
1. Check Railway logs first
2. Verify environment variables
3. Test locally to isolate issues
4. Check Railway status page: [status.railway.app](https://status.railway.app)

