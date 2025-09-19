"""
AWS Lambda: LinkedIn Data Engineer Job Scraper → S3 + DynamoDB + SNS  
Author: Bita

This AWS Lambda function performs the following tasks:
1. Scrapes Data Engineer job listings from LinkedIn's public search (Vancouver).
2. Filters jobs by title and location.
3. Saves job data into a CSV file.
4. Uploads the CSV to S3.
5. Logs metadata to DynamoDB.
6. Sends an SNS alert on success or failure.

Required AWS services:
- S3 (for CSV storage)
- DynamoDB (for logging job run)
- SNS (for notifications)

Libraries:
- boto3, requests, beautifulsoup4, csv, os, datetime
"""

import os
import json
import csv
import traceback
import urllib.parse
from datetime import datetime

import boto3
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load .env for local testing
load_dotenv()

# --- Validate Environment Variables ---
AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET = os.getenv("S3_BUCKET_NAME")
SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")
DYNAMODB_TABLE = os.getenv("DYNAMODB_TABLE")

if not AWS_REGION:
    raise ValueError("❌ AWS_REGION is not set in environment variables.")
if not S3_BUCKET:
    raise ValueError("❌ S3_BUCKET_NAME is not set.")
if not DYNAMODB_TABLE:
    raise ValueError("❌ DYNAMODB_TABLE is not set.")

# --- AWS Clients ---
s3 = boto3.client("s3", region_name=AWS_REGION)
dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
sns = boto3.client("sns", region_name=AWS_REGION)

# --- Search Parameters ---
SEARCH_TERM = "data engineer"
LOCATION = "Vancouver, British Columbia, Canada"
GEO_ID = "103366113"  # LinkedIn Geo ID for Vancouver

# --- SNS Helper ---
def send_alert(subject, message):
    if not SNS_TOPIC_ARN:
        print("⚠️ SNS_TOPIC_ARN not set. Skipping alert.")
        return
    try:
        sns.publish(TopicArn=SNS_TOPIC_ARN, Subject=subject, Message=message)
    except Exception as e:
        print(f"⚠️ Failed to send SNS alert: {e}")

# --- Lambda Handler ---
def lambda_handler(event=None, context=None):
    try:
        # --- Build URL ---
        base_url = (
            f"https://www.linkedin.com/jobs/search/?"
            f"geoId={GEO_ID}&keywords={urllib.parse.quote(SEARCH_TERM)}"
        )
        print("🔗 URL:", base_url)

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept-Language": "en-US,en;q=0.9",
        }

        #Fetching HTML with BeautifulSoup
        response = requests.get(base_url, headers=headers)
        print(f"🌐 HTTP Status: {response.status_code}")
        if response.status_code != 200:
            raise Exception("LinkedIn page fetch failed.")

        #Parsing HTML with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        with open("LinkedIn_debug.html", "w", encoding="utf-8") as f:
            f.write(soup.prettify())
        print("💾 HTML saved to LinkedIn_debug.html")


        #Job Extraction + Filtering
        job_cards = soup.find_all("li")
        print(f"🧾 Found {len(job_cards)} job cards.")
    
        
        filename = f"linkedin_jobs_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.csv"
        local_path = f"/tmp/{filename}"
        rows_to_add = []
        existing_titles = set()

        # --- Write CSV ---
        with open(local_path, mode="w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Title", "Company", "Location", "Link", "Timestamp"])

            for job in job_cards:
                title_tag = job.find("h3")
                company_tag = job.find("h4")
                location_tag = job.find("span", class_="job-search-card__location")
                link_tag = job.find("a", href=True)

                if title_tag and company_tag and location_tag and link_tag:
                    title = title_tag.get_text(strip=True)
                    company = company_tag.get_text(strip=True)
                    location = location_tag.get_text(strip=True)
                    link = "https://www.linkedin.com" + link_tag["href"]
                    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

                    '''
                    if "data" not in title.lower() or "engineer" not in title.lower():
                        continue
                    if "vancouver" not in location.lower():
                        continue
                        '''
                    if title in existing_titles:
                        print(f"⚠️ Duplicate: {title}")
                        continue
                        

                    existing_titles.add(title)
                    rows_to_add.append([title, company, location, link, timestamp])
                    writer.writerow([title, company, location, link, timestamp])
                    print(f"✅ {title} at {company} — {location}")

        # --- Upload to S3 ---
        s3.upload_file(local_path, S3_BUCKET, f"linkedin/{filename}")
        print(f"📤 Uploaded to s3://{S3_BUCKET}/linkedin/{filename}")

        # --- Log to DynamoDB ---
        table = dynamodb.Table(DYNAMODB_TABLE)
        table.put_item(Item={
            "id": filename,
            "timestamp": datetime.utcnow().isoformat(),
            "records": len(rows_to_add),
            "status": "uploaded"
        })

        # --- Success Notification ---
        send_alert("✅ LinkedIn Scraper Success", f"{filename} uploaded with {len(rows_to_add)} jobs.")
        return {"statusCode": 200, "body": json.dumps(f"Success: {filename}")}

    except Exception as e:
        print("❌ Error:", str(e))
        traceback.print_exc()
        send_alert("❌ LinkedIn Scraper Error", str(e))
        return {"statusCode": 500, "body": json.dumps(f"Error: {str(e)}")}
    
    # 🔹 Run manually for local testing
if __name__ == "__main__":
    lambda_handler()