"""
Rig Count Automation - Main Script
Scrapes Baker Hughes rig count data, generates Permian Basin chart, and emails it.
"""
import os
import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for Railway
import matplotlib.pyplot as plt
import smtplib
from email.message import EmailMessage
from datetime import datetime
import warnings
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Suppress openpyxl warnings
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")


def scrape_rig_count_excel():
    """Scrape and download the rig count Excel file from Baker Hughes"""
    logger.info("Scraping rig count data from Baker Hughes...")
    
    base_url = "https://rigcount.bakerhughes.com"
    page_url = base_url + "/na-rig-count"
    
    try:
        response = requests.get(page_url, timeout=30)
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Failed to fetch rig count page: {e}")
        raise
    
    soup = BeautifulSoup(response.content, "html.parser")
    
    download_url = None
    for link in soup.find_all("a", href=True):
        if "North America Rig Count Report - New Report" in link.text:
            download_url = base_url + link["href"]
            break
    
    if not download_url:
        raise Exception("Could not find the rig count Excel download link.")
    
    logger.info(f"Found download URL: {download_url}")
    
    # Save Excel file locally
    script_dir = os.path.dirname(os.path.abspath(__file__))
    excel_path = os.path.join(script_dir, "data", "NA Rig Count Report Automated.xlsx")
    
    # Create data directory if it doesn't exist
    os.makedirs(os.path.dirname(excel_path), exist_ok=True)
    
    try:
        excel_response = requests.get(download_url, timeout=60)
        excel_response.raise_for_status()
        with open(excel_path, "wb") as f:
            f.write(excel_response.content)
        logger.info(f"Excel file saved to: {excel_path}")
    except requests.RequestException as e:
        logger.error(f"Failed to download Excel file: {e}")
        raise
    
    return excel_path


def generate_permian_chart(excel_path):
    """Generate Permian Basin rig count chart from Excel data"""
    logger.info("Generating Permian Basin chart...")
    
    try:
        df = pd.read_excel(excel_path, sheet_name="NAM Weekly", header=10)
        df_permian = df[df["Basin"].str.contains("Permian", na=False)]
        
        if df_permian.empty:
            raise Exception("No Permian Basin data found in Excel file")
        
        summary = df_permian.groupby("US_PublishDate")["Rig Count Value"].sum().reset_index()
        summary["US_PublishDate"] = pd.to_datetime(summary["US_PublishDate"])
        summary = summary.sort_values("US_PublishDate")
        
        logger.info(f"Processed {len(summary)} data points for Permian Basin")
        
        # Plot chart
        plt.figure(figsize=(12, 6))
        plt.plot(summary["US_PublishDate"], summary["Rig Count Value"], marker='o', linestyle='-')
        plt.title("Permian Basin Rig Count Over Time")
        plt.xlabel("Date")
        plt.ylabel("Rig Count")
        plt.grid(True)
        plt.tight_layout()
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        chart_path = os.path.join(script_dir, "data", "permian_rig_chart.png")
        os.makedirs(os.path.dirname(chart_path), exist_ok=True)
        
        plt.savefig(chart_path, dpi=150)
        plt.close()
        
        logger.info(f"Chart saved to: {chart_path}")
        return chart_path
        
    except Exception as e:
        logger.error(f"Error generating chart: {e}")
        raise


def send_email_with_chart(chart_path):
    """Send email with rig count chart attachment"""
    logger.info("Preparing email...")
    
    # Get email credentials from environment variables
    EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    TO_ADDRESS = os.getenv('TO_ADDRESS')
    
    if not EMAIL_ADDRESS or not EMAIL_PASSWORD or not TO_ADDRESS:
        raise ValueError(
            "Missing required environment variables: EMAIL_ADDRESS, EMAIL_PASSWORD, TO_ADDRESS"
        )
    
    msg = EmailMessage()
    msg["Subject"] = f"Automated Permian Rig Count Chart - {datetime.now().strftime('%Y-%m-%d')}"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = TO_ADDRESS
    msg.set_content("Attached is the latest Permian Basin rig count chart.")
    
    # Attach the image
    try:
        with open(chart_path, "rb") as img:
            msg.add_attachment(
                img.read(), 
                maintype="image", 
                subtype="png", 
                filename="permian_rig_chart.png"
            )
        logger.info("Chart attached to email")
    except Exception as e:
        logger.error(f"Error attaching chart: {e}")
        raise
    
    # Send email
    try:
        logger.info(f"Sending email to {TO_ADDRESS}...")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        logger.info("Email sent successfully!")
    except Exception as e:
        logger.error(f"Error sending email: {e}")
        raise


def main():
    """Main function to run the rig count automation"""
    try:
        logger.info("=" * 60)
        logger.info("Rig Count Automation Started")
        logger.info(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info("=" * 60)
        
        # Step 1: Scrape Excel file
        excel_path = scrape_rig_count_excel()
        
        # Step 2: Generate chart
        chart_path = generate_permian_chart(excel_path)
        
        # Step 3: Send email
        send_email_with_chart(chart_path)
        
        logger.info("=" * 60)
        logger.info("Rig Count Automation Completed Successfully!")
        logger.info("=" * 60)
        
    except Exception as e:
        logger.error(f"Rig count automation failed: {e}", exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    main()

