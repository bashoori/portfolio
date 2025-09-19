"""
Script: dynamodb_setup.py
Purpose: One-time setup script to create a DynamoDB table for logging LinkedIn scraper results.
Author: Bita
"""

import boto3

# Configuration
TABLE_NAME = "JobScraperLogs"
REGION = "us-west-2"  # Change to your region

dynamodb = boto3.client("dynamodb", region_name=REGION)

# Create the table
try:
    response = dynamodb.create_table(
        TableName=TABLE_NAME,
        KeySchema=[
            {"AttributeName": "id", "KeyType": "HASH"},  # Partition key
        ],
        AttributeDefinitions=[
            {"AttributeName": "id", "AttributeType": "S"},
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        }
    )
    print(f"✅ Table '{TABLE_NAME}' is being created. Status: {response['TableDescription']['TableStatus']}")
except dynamodb.exceptions.ResourceInUseException:
    print(f"⚠️ Table '{TABLE_NAME}' already exists.")
