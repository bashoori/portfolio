import boto3
import os

# Load from environment or manually set
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

bucket_name = "bashoori-s3"
object_key = "linkedin/linkedin_jobs_20250416_153022.csv"
local_file = "downloaded_jobs.csv"

s3.download_file(bucket_name, object_key, local_file)
print(f"✅ Downloaded: {local_file}")