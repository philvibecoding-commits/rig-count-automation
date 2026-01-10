"""
Scheduler for running rig count automation on Railway
Runs the automation script on a schedule (default: daily at 9 AM UTC)
"""
import os
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
        
    except Exception as e:
        logger.error(f"Error running rig count job: {e}", exc_info=True)
        raise


def main():
    """Main scheduler entry point"""
    # Get schedule interval from environment (default: daily at 9 AM UTC)
    schedule_time = os.getenv('SCHEDULE_TIME', '09:00')
    run_on_startup = os.getenv('RUN_ON_STARTUP', 'true').lower() == 'true'
    
    logger.info(f"Rig Count Scheduler initialized")
    logger.info(f"Schedule: Daily at {schedule_time} UTC")
    logger.info(f"Run on startup: {run_on_startup}")
    
    # Schedule the job
    schedule.every().day.at(schedule_time).do(run_rig_count_job)
    
    # Run immediately on startup if configured
    if run_on_startup:
        logger.info("Running initial job on startup...")
        run_rig_count_job()
    
    # Keep the scheduler running
    logger.info("Scheduler running. Waiting for scheduled jobs...")
    logger.info("Press Ctrl+C to stop")
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        logger.info("Scheduler stopped by user")
    except Exception as e:
        logger.error(f"Scheduler error: {e}", exc_info=True)
        raise


if __name__ == '__main__':
    main()
