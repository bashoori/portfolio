# 📦 AWS Lambda LinkedIn Job Scraper

Scrapes Data Engineer job listings from LinkedIn, filters results, stores data in S3, logs metadata to DynamoDB, and sends alerts using Amazon SNS.

---

## 🚀 Project Overview

**Title**: AWS Lambda: LinkedIn Data Engineer Job Scraper → S3 + DynamoDB + SNS  
**Author**: Bita Ashoori  
**Category**: Cloud-Based ETL Pipeline  

### 🔍 What it Does

This Lambda function performs the following:

1. Scrapes **public LinkedIn job listings** from the guest search endpoint (no login required).
2. Filters listings for those with **"Data Engineer"** in the title and **"Vancouver"** in the location.
3. Saves job metadata (title, company, location, link, timestamp) into a **CSV file**.
4. Uploads the file to a structured folder in **Amazon S3**.
5. Logs job run details (filename, timestamp, record count) into a **DynamoDB table**.
6. Sends **success or error notifications** via **SNS (Amazon Simple Notification Service)**.

---

## 🧪 Technologies Used

| Tech | Purpose |
|------|---------|
| **AWS Lambda** | Run the scraper code without managing servers |
| **S3** | Store output CSVs in `linkedin/` folder |
| **DynamoDB** | Log each run for history and monitoring |
| **SNS** | Alert via email on success/failure |
| **BeautifulSoup** | Parse LinkedIn HTML |
| **boto3** | Interact with AWS services |
| **requests** | Perform HTTP calls to LinkedIn guest API |

---

## ⚙️ Environment Variables

Set these in Lambda console or use `.env` locally:

```bash
AWS_REGION=us-west-2
S3_BUCKET_NAME=bashoori-s3
DYNAMODB_TABLE=JobScraperLogs
SNS_TOPIC_ARN=arn:aws:sns:us-west-2:xxxxxxx:LinkedInJobAlerts
```

---

## 🔐 Required IAM Permissions

```json
{
  "Effect": "Allow",
  "Action": [
    "s3:PutObject",
    "dynamodb:PutItem",
    "sns:Publish"
  ],
  "Resource": "*"
}
```

---

## 📄 Output Example (CSV)

```
Title,Company,Location,Link,Timestamp
Data Engineer,Amazon,Vancouver,https://www.linkedin.com/jobs/view/...,2025-04-18 12:01:30
```

---

## 🛠 Deployment Steps

1. Clone this repo and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Zip `lambda/` folder including dependencies for Lambda:
   ```bash
   zip -r linkedin_scraper_lambda.zip lambda/
   ```
3. Upload to AWS Lambda console or deploy via GitHub Actions.
4. Set the environment variables.
5. (Optional) Schedule it via **EventBridge** to run daily.

---

## ✅ Status

- [x] Successfully tested with Vancouver job listings
- [x] CSV uploaded to S3
- [x] Logs saved to DynamoDB
- [x] SNS alerts enabled and functional

---

## 📬 Fork & Customize

Feel free to fork this repo, update it with your own search terms or regions, and make it part of your own data engineering portfolio. ⭐

---
