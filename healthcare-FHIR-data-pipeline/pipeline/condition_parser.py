"""
📄 condition_parser.py

This script extracts Condition resources from Synthea-generated FHIR bundles.
Each JSON file contains a bundle of resources including Patient, Condition, etc.

Author: Bita Ashoori
"""

import os
import json
import pandas as pd

# -------------------------------
# Configuration
# -------------------------------
INPUT_DIR = "../data/fhir"
OUTPUT_FILE = "../data/output/parsed_conditions.csv"

# Ensure output directory exists
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

# Initialize list to store extracted condition data
condition_records = []

# -------------------------------
# Read and Parse FHIR Bundle Files
# -------------------------------
for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".json"):
        filepath = os.path.join(INPUT_DIR, filename)
        try:
            with open(filepath, "r") as f:
                bundle = json.load(f)

            if bundle.get("resourceType") != "Bundle":
                continue

            for entry in bundle.get("entry", []):
                resource = entry.get("resource", {})
                if resource.get("resourceType") == "Condition":
                    condition_id = resource.get("id", "")
                    subject_ref = resource.get("subject", {}).get("reference", "")
                    clinical_status = resource.get("clinicalStatus", {}).get("text", "")
                    verification_status = resource.get("verificationStatus", {}).get("text", "")
                    code_text = resource.get("code", {}).get("text", "")
                    onset_date = resource.get("onsetDateTime", "")

                    condition_records.append([
                        condition_id, subject_ref, clinical_status,
                        verification_status, code_text, onset_date
                    ])
        except Exception as e:
            print(f"❌ Error reading {filename}: {e}")

# -------------------------------
# Save to CSV
# -------------------------------
columns = [
    "Condition ID", "Subject Reference", "Clinical Status",
    "Verification Status", "Condition", "Onset Date"
]

df = pd.DataFrame(condition_records, columns=columns)
df.to_csv(OUTPUT_FILE, index=False)

print(f"✅ Extracted {len(df)} conditions to: {OUTPUT_FILE}")

