# ✅ Railway Deployment Checklist

Use this checklist to ensure everything is ready for deployment.

## Pre-Deployment

### Code Preparation
- [ ] All files are in the project directory
- [ ] `rig_count_automation.py` is refactored and tested
- [ ] `rig_count_scheduler.py` is ready
- [ ] `requirements.txt` includes all dependencies
- [ ] `railway.toml` is configured correctly
- [ ] `.gitignore` excludes sensitive files

### Local Testing
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file created with test credentials
- [ ] `python test_local.py` passes all checks
- [ ] `python rig_count_automation.py` runs successfully
- [ ] Test email received with chart attachment

### Git Setup
- [ ] Git repository initialized (`git init`)
- [ ] All files added (`git add .`)
- [ ] Initial commit made (`git commit`)
- [ ] GitHub repository created
- [ ] Code pushed to GitHub (`git push`)

## Railway Deployment

### Project Setup
- [ ] Railway account created
- [ ] New project created in Railway
- [ ] GitHub repository connected
- [ ] Railway detected Python automatically

### Environment Variables
- [ ] `EMAIL_ADDRESS` set
- [ ] `EMAIL_PASSWORD` set (Gmail app password)
- [ ] `TO_ADDRESS` set
- [ ] `SCHEDULE_TIME` set (optional, default: 09:00)
- [ ] `RUN_ON_STARTUP` set (optional, default: true)

### Verification
- [ ] Deployment successful (green status)
- [ ] Logs show "Rig Count Scheduler initialized"
- [ ] Logs show "Running initial job on startup..."
- [ ] Logs show "Rig Count Automation Completed Successfully!"
- [ ] Email received with chart (if RUN_ON_STARTUP=true)
- [ ] No errors in Railway logs

## Post-Deployment

### Monitoring
- [ ] Check logs daily for first week
- [ ] Verify scheduled runs are working
- [ ] Confirm emails are being sent
- [ ] Monitor Railway usage/billing

### Maintenance
- [ ] Update code as needed
- [ ] Keep dependencies updated
- [ ] Monitor for API changes (Baker Hughes)
- [ ] Backup important data if needed

## Troubleshooting Checklist

If something goes wrong:

- [ ] Check Railway logs for errors
- [ ] Verify all environment variables are set
- [ ] Test email credentials locally
- [ ] Verify Gmail app password is correct
- [ ] Check Railway status page
- [ ] Review error messages in logs
- [ ] Test script locally to isolate issues

## Quick Commands Reference

```powershell
# Test locally
python test_local.py

# Run automation once
python rig_count_automation.py

# Run scheduler locally
python rig_count_scheduler.py

# Setup git (Windows)
.\setup_git.ps1

# Git commands
git add .
git commit -m "Your message"
git push
```

## Support Resources

- **Railway Docs**: [docs.railway.app](https://docs.railway.app)
- **Railway Status**: [status.railway.app](https://status.railway.app)
- **Project README**: See `README.md`
- **Detailed Setup**: See `RAILWAY_SETUP.md`
- **Quick Start**: See `QUICK_START.md`

---

**Last Updated**: January 2025

