"""
Scheduler for running rig count automation on Railway
Runs the automation script on a schedule (default: every Friday at 18:30 UTC / 12:30 PM CST)
"""
import os
import sys
import time
import logging
import schedule
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def validate_environment():
    """Validate required environment variables are set"""
    required_vars = ['EMAIL_ADDRESS', 'EMAIL_PASSWORD', 'TO_ADDRESS']
    missing = []
    
    logger.info("Checking environment variables...")
    for var in required_vars:
        value = os.getenv(var)
        if not value:
            missing.append(var)
            logger.error(f"  [MISSING] {var}")
        else:
            # Mask sensitive values
            if 'PASSWORD' in var:
                logger.info(f"  [OK] {var} = {'*' * len(value)}")
            else:
                logger.info(f"  [OK] {var} = {value}")
    
    if missing:
        logger.error("=" * 60)
        logger.error("CONFIGURATION ERROR: Missing environment variables!")
        logger.error(f"Missing: {', '.join(missing)}")
        logger.error("")
        logger.error("Please add these variables in Railway dashboard:")
        logger.error("  1. Go to your Railway project")
        logger.error("  2. Click on Variables tab")
        logger.error("  3. Add the missing variables")
        logger.error("=" * 60)
        return False
    
    return True


def run_rig_count_job():
    """Run the rig count automation script"""
    try:
        logger.info("=" * 60)
        logger.info("Starting Rig Count Automation Job")
        logger.info(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info("=" * 60)
        
        # Import and run the main script
        import rig_count_automation
        rig_count_automation.main()
        
        logger.info("Rig count job completed successfully")
        logger.info("=" * 60)
        return True
        
    except Exception as e:
        logger.error(f"Job failed: {e}", exc_info=True)
        logger.error("Job will retry at next scheduled time")
        logger.error("=" * 60)
        # Don't re-raise - let scheduler continue running
        return False


def main():
    """Main scheduler entry point"""
    logger.info("=" * 60)
    logger.info("Rig Count Scheduler Starting")
    logger.info("=" * 60)
    
    # Validate environment variables FIRST
    if not validate_environment():
        logger.error("Scheduler cannot start without required environment variables.")
        logger.error("Waiting for configuration... (scheduler will stay alive)")
        logger.error("")
        logger.error("Add these variables in Railway, then redeploy:")
        logger.error("  EMAIL_ADDRESS = your-email@gmail.com")
        logger.error("  EMAIL_PASSWORD = your-app-password")
        logger.error("  TO_ADDRESS = recipient@email.com")
        logger.error("")
        # Keep the container alive but don't run jobs
        # This prevents crash loops while user configures env vars
        while True:
            time.sleep(300)  # Check every 5 minutes
            if validate_environment():
                logger.info("Environment variables configured! Starting scheduler...")
                break
    
    # Get schedule settings
    schedule_time = os.getenv('SCHEDULE_TIME', '18:30')  # Default: 18:30 UTC = 12:30 PM CST
    run_on_startup = os.getenv('RUN_ON_STARTUP', 'true').lower() == 'true'
    
    logger.info(f"Schedule: Every Friday at {schedule_time} UTC (12:30 PM CST)")
    logger.info(f"Run on startup: {run_on_startup}")
    
    # Schedule the job - runs every Friday
    schedule.every().friday.at(schedule_time).do(run_rig_count_job)
    
    # Run immediately on startup if configured
    if run_on_startup:
        logger.info("Running initial job on startup...")
        run_rig_count_job()
    
    # Keep the scheduler running
    logger.info("Scheduler running. Waiting for scheduled jobs...")
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        logger.info("Scheduler stopped by user")
    except Exception as e:
        logger.error(f"Scheduler error: {e}", exc_info=True)
        # Don't crash - keep trying
        time.sleep(60)


if __name__ == '__main__':
    main()
