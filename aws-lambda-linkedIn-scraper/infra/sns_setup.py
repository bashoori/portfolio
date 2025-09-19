"""
Script: sns_setup.py
Purpose: One-time script to create an SNS topic and subscribe your email.
Author: Bita
"""

import boto3

# Config
TOPIC_NAME = "LinkedInJobAlerts"
EMAIL_ADDRESS = "you@example.com"  # <- Replace with your real email
REGION = "us-west-2"  # Change to your AWS region

# Create SNS client
sns = boto3.client("sns", region_name=REGION)

# Create the topic
response = sns.create_topic(Name=TOPIC_NAME)
topic_arn = response["TopicArn"]
print(f"✅ SNS Topic created: {topic_arn}")

# Subscribe an email address
sub = sns.subscribe(
    TopicArn=topic_arn,
    Protocol="email",
    Endpoint=EMAIL_ADDRESS
)

print(f"📧 Subscription pending. Check your inbox ({EMAIL_ADDRESS}) to confirm.")