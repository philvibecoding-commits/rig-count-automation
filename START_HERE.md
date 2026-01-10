# 🎯 START HERE - Rig Count Automation

Welcome! This guide will help you get started.

## 📚 Documentation Guide

Choose your path based on what you need:

### 🚀 **I want to deploy NOW** (5 minutes)
→ Read: **`QUICK_START.md`**

### 📖 **I want detailed instructions**
→ Read: **`RAILWAY_SETUP.md`**

### ✅ **I want a checklist to follow**
→ Read: **`DEPLOYMENT_CHECKLIST.md`**

### 📋 **I want an overview of everything**
→ Read: **`PROJECT_SUMMARY.md`**

### 📝 **I want full documentation**
→ Read: **`README.md`**

## 🎬 Quick Start (3 Steps)

### Step 1: Test Locally
```powershell
# Install dependencies
pip install -r requirements.txt

# Create .env file (copy from env_template.txt)
# Add your email credentials

# Test
python test_local.py
python rig_count_automation.py
```

### Step 2: Setup Git
```powershell
# Use helper script
.\setup_git.ps1

# Or manually
git init
git add .
git commit -m "Initial commit"
```

### Step 3: Deploy to Railway
1. Push to GitHub
2. Connect to Railway
3. Add environment variables
4. Done! ✅

## 📁 What's in This Project?

- ✅ **rig_count_automation.py** - Main automation script
- ✅ **rig_count_scheduler.py** - Scheduler for Railway
- ✅ **requirements.txt** - Python dependencies
- ✅ **railway.toml** - Railway config
- ✅ **Helper scripts** - Setup and testing tools
- ✅ **Documentation** - Complete guides

## ⚡ Fast Track

**Already know what you're doing?**

1. `pip install -r requirements.txt`
2. Create `.env` with your credentials
3. `python test_local.py` to verify
4. `.\setup_git.ps1` to setup git
5. Push to GitHub → Deploy to Railway

**Total time: ~10 minutes**

## 🆘 Need Help?

1. Check `DEPLOYMENT_CHECKLIST.md` troubleshooting section
2. Review Railway logs
3. Test locally first with `test_local.py`

---

**Ready?** Start with `QUICK_START.md` → 🚀

