# 📦 AWS Lambda: LinkedIn Data Engineer Job Scraper → S3 + DynamoDB + SNS

> Author: **Bita**  
> Repository: [`data-engineering-portfolio`](https://github.com/bashoori/data-engineering-portfolio)

This AWS Lambda project scrapes publicly available Data Engineer jobs from LinkedIn, saves them to a CSV file, and uploads the data to AWS services (S3, DynamoDB, SNS) — all within the **AWS Free Tier**.

---

## 🧠 What It Does

1. 🔍 Scrapes LinkedIn jobs for "Data Engineer" roles in **Vancouver, BC** using the guest search endpoint.
2. 🧽 Parses job data using **BeautifulSoup**, filtering only titles that include both `data` and `engineer`.
3. 📁 Writes the results into a CSV file.
4. ☁️ Uploads the file to **Amazon S3** (folder: `linkedin/`).
5. 📊 Logs run metadata to **DynamoDB** (job count, timestamp, filename).
6. 📣 Sends a success/failure alert via **SNS**.

---

## ⚙️ Stack & Tools

| Tool | Purpose |
|------|---------|
| `boto3` | AWS SDK for Python (S3, SNS, DynamoDB) |
| `requests` | HTTP requests for scraping |
| `beautifulsoup4` | HTML parsing |
| `csv` & `datetime` | CSV file creation and timestamping |

---

## 🔐 Required IAM Permissions

```yaml
- s3:PutObject
- dynamodb:PutItem
- sns:Publish
```

---

## 🔧 Environment Variables (via Lambda Console or .env)

```env
AWS_REGION=us-west-2
S3_BUCKET_NAME=bashoori-s3
DYNAMODB_TABLE=JobScraperLogs
SNS_TOPIC_ARN=arn:aws:sns:us-west-2:123456789012:LinkedInJobAlerts
```

---

## 📂 Folder Structure

```
lambda/
├── handler.py                  # 🧠 Lambda main script
├── .env                        # 🔐 Local environment secrets (ignored by Git)
├── LinkedIn_debug.html        # 🛠️ Saved HTML for debugging
├── linkedin_jobs_YYYYMMDD.csv # ✅ Uploaded CSV (saved to /tmp)
└── readme.md                   # 📘 You're here
```

---

## 🚀 How to Deploy

1. **Install dependencies locally**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Zip contents for Lambda** (not the folder, just files):
   ```bash
   zip lambda-package.zip handler.py requirements.txt
   ```

3. **Upload to AWS Lambda**:
   - Set handler to `handler.lambda_handler`
   - Configure environment variables
   - Add permissions (S3, SNS, DynamoDB)

4. *(Optional)*: Set up a CloudWatch EventBridge rule to trigger it daily or weekly

---

## 📈 Outputs

- ✅ CSV file saved in: `s3://bashoori-s3/linkedin/`
- 📊 DynamoDB table: `JobScraperLogs`
- 📣 SNS alert sent with status and job count

---

## 📌 Status Tracking (DynamoDB Log Schema)

| Column     | Description                     |
|------------|---------------------------------|
| `id`       | Filename (csv)                  |
| `timestamp`| UTC time of run                 |
| `records`  | Number of jobs scraped          |
| `status`   | `uploaded` or `error`           |

---

## ✨ Want to Extend This?

- Add CloudWatch metrics or dashboards
- Use Step Functions for chaining jobs
- Push records to BigQuery instead
- Convert it into a GitHub Actions workflow for CI/CD

---

## 🛡️ License

This project is licensed under the [MIT License](../../LICENSE).

---

## 🙌 Inspired by

This project is part of [@bashoori](https://github.com/bashoori)'s cloud portfolio showcasing real-world AWS pipelines.

---

## 📬 Contact

For collaboration or questions, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/bashoori/) or check the full [GitHub Portfolio](https://github.com/bashoori/data-engineering-portfolio).
