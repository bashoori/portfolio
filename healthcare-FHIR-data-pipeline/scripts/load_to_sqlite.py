"""
📄 load_to_sqlite.py

This script loads cleaned CSVs from the FHIR data pipeline into a local SQLite database.
It creates tables for patients, conditions, encounters, and observations.

Author: Bita Ashoori
"""

import sqlite3
import pandas as pd
import os

# -------------------------------
# Config
# -------------------------------
DB_FILE = "../data/output/fhir_data.db"
CSV_DIR = "../data/output"

CSV_TABLE_MAP = {
    "parsed_patients.csv": "patients",
    "parsed_conditions.csv": "conditions",
    "parsed_encounters.csv": "encounters",
    "parsed_observations.csv": "observations"
}

# -------------------------------
# Load each CSV into a SQLite table
# -------------------------------
conn = sqlite3.connect(DB_FILE)
print(f"🛠️ Connecting to database: {DB_FILE}")

for csv_file, table_name in CSV_TABLE_MAP.items():
    csv_path = os.path.join(CSV_DIR, csv_file)
    if os.path.exists(csv_path):
        print(f"📥 Loading: {csv_file} → Table: {table_name}")
        df = pd.read_csv(csv_path)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
    else:
        print(f"⚠️ Skipping missing file: {csv_file}")

conn.commit()
conn.close()
print("✅ All available data loaded into SQLite!")
