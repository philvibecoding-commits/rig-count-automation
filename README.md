# Rig Count Automation

Automated system that scrapes Baker Hughes rig count data, generates Permian Basin charts, and emails them on a schedule.

## Features

- 🔄 **Automated Scraping**: Downloads the latest North America Rig Count Report from Baker Hughes
- 📊 **Chart Generation**: Creates Permian Basin rig count visualization
- 📧 **Email Delivery**: Automatically emails the chart on schedule
- ⏰ **Scheduled Runs**: Configurable daily schedule via Railway

## Project Structure

```
.
├── rig_count_automation.py  # Main automation script
├── rig_count_scheduler.py   # Scheduler for Railway
├── requirements.txt         # Python dependencies
├── railway.toml             # Railway configuration
├── .gitignore              # Git ignore rules
├── env_template.txt        # Environment variables template
├── setup_git.ps1           # Git setup helper script
├── test_local.py           # Local testing script
├── README.md               # This file
├── QUICK_START.md          # Quick start guide (5 minutes)
└── RAILWAY_SETUP.md        # Detailed Railway setup guide
```

## Setup Instructions

### 1. Local Development

1. **Clone or navigate to the repository**
   ```bash
   cd C:\Users\phill\OneDrive\Python
   ```

2. **Create virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy the example file
   copy .env.example .env
   
   # Edit .env and add your credentials:
   # EMAIL_ADDRESS=your-email@gmail.com
   # EMAIL_PASSWORD=your-app-password
   # TO_ADDRESS=recipient@example.com
   ```

5. **Run locally**
   ```bash
   # One-time run
   python rig_count_automation.py
   
   # Or with scheduler
   python rig_count_scheduler.py
   ```

### 2. Railway Deployment

#### Prerequisites
- Railway account (sign up at [railway.app](https://railway.app))
- GitHub account (for connecting repository)

#### Steps

1. **Initialize Git Repository** (if not already done)
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Rig count automation"
   ```

2. **Create GitHub Repository**
   - Go to GitHub and create a new repository
   - Push your code:
     ```bash
     git remote add origin https://github.com/yourusername/rig-count-automation.git
     git branch -M main
     git push -u origin main
     ```

3. **Deploy to Railway**
   - Go to [railway.app](https://railway.app)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will automatically detect Python and install dependencies

4. **Configure Environment Variables**
   - In Railway dashboard, go to your project → Variables
   - Add these variables:
     ```
     EMAIL_ADDRESS=waldoautomationworks@gmail.com
     EMAIL_PASSWORD=jogb xaip pqdu jhdj
     TO_ADDRESS=phillip.t.flores@gmail.com
     SCHEDULE_TIME=09:00
     RUN_ON_STARTUP=true
     ```

5. **Deploy**
   - Railway will automatically deploy when you push to GitHub
   - Check logs to verify it's running

## Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `EMAIL_ADDRESS` | Gmail address to send from | Yes | - |
| `EMAIL_PASSWORD` | Gmail app password | Yes | - |
| `TO_ADDRESS` | Recipient email address | Yes | - |
| `SCHEDULE_TIME` | Daily run time (HH:MM UTC) | No | `09:00` |
| `RUN_ON_STARTUP` | Run immediately on startup | No | `true` |

### Gmail App Password Setup

Since Gmail requires app passwords for SMTP:

1. Go to [Google Account Settings](https://myaccount.google.com/)
2. Security → 2-Step Verification (enable if not already)
3. App Passwords → Generate new app password
4. Use this password in `EMAIL_PASSWORD` variable

## Usage

### One-Time Run
```bash
python rig_count_automation.py
```

### Scheduled Run (Local)
```bash
python rig_count_scheduler.py
```

### Railway
- Runs automatically based on `SCHEDULE_TIME` environment variable
- Default: Daily at 9:00 AM UTC
- Runs immediately on startup if `RUN_ON_STARTUP=true`

## Troubleshooting

### Email Not Sending
- Verify Gmail app password is correct
- Check that 2-factor authentication is enabled
- Ensure environment variables are set correctly

### Chart Not Generating
- Check that Excel file downloaded successfully
- Verify sheet name "NAM Weekly" exists
- Check logs for specific errors

### Railway Deployment Issues
- Check Railway logs for errors
- Verify all environment variables are set
- Ensure `requirements.txt` includes all dependencies

## License

Personal use project.

## Author

Phillip Flores

