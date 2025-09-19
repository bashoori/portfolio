"""
📄 fhir_parser.py

This script processes bundled FHIR JSON files from Synthea. Each file contains a
FHIR "Bundle" with multiple resources. The script extracts only the Patient resource
from each bundle and saves it as a structured CSV.

This version includes DEBUG LOGGING for troubleshooting.

Author: Bita Ashoori
"""

import os
import json
import pandas as pd

# -------------------------------
# Configuration
# -------------------------------
INPUT_DIR = "../data/fhir"
OUTPUT_FILE = "../data/output/parsed_patients.csv"

# Ensure output directory exists
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

# Initialize a list to collect patient records
patient_records = []

# -------------------------------
# Read and Parse Bundled FHIR Files
# -------------------------------
for filename in os.listdir(INPUT_DIR):                        #Checks every .json file in your input folder. Assumes each one is a FHIR bundle.
    if filename.endswith(".json"):
        filepath = os.path.join(INPUT_DIR, filename)
        print(f"🔍 Reading file: {filename}")
        try:
            with open(filepath, "r") as f:                    #Reads the FHIR JSON file and loads it into a Python dictionary.
                bundle = json.load(f)

            # Confirm it's a FHIR bundle
            if bundle.get("resourceType") != "Bundle":        #Skips any file that isn’t a proper FHIR Bundle.
                print(f"⛔ Skipping non-bundle: {filename}")
                continue

            # Find the Patient resource inside "entry"
            patient_data = None
            for entry in bundle.get("entry", []):
                resource = entry.get("resource", {})
                if resource.get("resourceType") == "Patient":
                    print(f"✅ Found Patient in: {filename}")
                    patient_data = resource
                    break

            if not patient_data:
                print(f"⚠️ No Patient found in: {filename}")
                continue

            # Extract fields
            patient_id = patient_data.get("id", "")
            gender = patient_data.get("gender", "")
            birth_date = patient_data.get("birthDate", "")
            marital_status = patient_data.get("maritalStatus", {}).get("text", "")

            name_data = patient_data.get("name", [{}])[0]
            first_name = name_data.get("given", [""])[0]
            last_name = name_data.get("family", "")

            address_data = patient_data.get("address", [{}])[0]
            city = address_data.get("city", "")
            state = address_data.get("state", "")
            country = address_data.get("country", "")

            telecom_data = patient_data.get("telecom", [{}])
            contact_value = telecom_data[0].get("value", "") if telecom_data else ""

            identifier = patient_data.get("identifier", [{}])[0].get("value", "")

            language = ""
            if patient_data.get("communication"):
                language = patient_data["communication"][0].get("language", {}).get("text", "")

            # Append record
            patient_records.append([
                patient_id, first_name, last_name, gender, birth_date, marital_status,
                city, state, country, contact_value, identifier, language
            ])
        except Exception as e:
            print(f"❌ Error reading {filename}: {e}")

# -------------------------------
# Save to CSV
# -------------------------------
columns = [
    "Patient ID", "First Name", "Last Name", "Gender", "Birth Date", "Marital Status",
    "City", "State", "Country", "Contact", "Identifier", "Language"
]

df = pd.DataFrame(patient_records, columns=columns)
df.to_csv(OUTPUT_FILE, index=False)

# -------------------------------
# Completion Message
# -------------------------------
print(f"✅ Extracted {len(df)} patient records from FHIR bundles to: {OUTPUT_FILE}")
