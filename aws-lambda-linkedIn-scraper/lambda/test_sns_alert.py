import os
import boto3
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize SNS client using environment or IAM role (no hardcoded credentials!)
sns = boto3.client("sns", region_name=os.getenv("AWS_REGION"))

# Compose your test message
message = "✅ Test alert from LinkedIn Job Scraper pipeline!"
subject = "🚨 SNS Notification Test"

try:
    response = sns.publish(
        TopicArn=os.getenv("SNS_TOPIC_ARN"),
        Message=message,
        Subject=subject
    )
    print("✅ Notification sent! Message ID:", response["MessageId"])
except Exception as e:
    print("❌ Failed to send message:", e)
    