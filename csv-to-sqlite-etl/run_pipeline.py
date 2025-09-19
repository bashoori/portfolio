"""
run_pipeline.py

Main orchestrator to run the full ETL pipeline:
Extract → Transform → Load → Read from SQLite

Author: Bita
Date: 2025-07
"""

from etl.extract import extract_csv_data
from etl.transform import clean_shipment_data
from etl.load import load_to_sqlite
#from read_from_db import read_from_sqlite
from etl.read_from_db import read_from_sqlite

import os
import logging
from datetime import datetime

# ───────────────────────────────────────
# Setup Logging
# ───────────────────────────────────────
os.makedirs("logs", exist_ok=True)
log_filename = os.path.join("logs", f"etl_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

logging.basicConfig(
    filename=log_filename,
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# ───────────────────────────────────────
# ETL Process
# ───────────────────────────────────────
def run_etl():
    logging.info("🚀 Starting ETL pipeline")
    print("🚀 Starting ETL pipeline")

    input_csv = os.path.join("data", "shipments.csv")
    output_db = os.path.join("output", "shipments.db")

    try:
        # Extract
        df_raw = extract_csv_data(input_csv)
        if df_raw.empty:
            logging.warning("No data extracted from CSV.")
            return

        # Transform
        df_clean = clean_shipment_data(df_raw)
        if df_clean.empty:
            logging.warning("Data cleaning resulted in empty DataFrame.")
            return

        # Load
        load_to_sqlite(df_clean, output_db)

        # Read back and show a preview
        df_preview = read_from_sqlite(output_db)
        logging.info("Preview of loaded data:")
        logging.info(df_preview.head().to_string())
        print("\n✅ Preview of loaded data:")
        print(df_preview.head())

        logging.info("✅ ETL pipeline completed successfully.")
        print("✅ ETL pipeline completed successfully.")

    except Exception as e:
        logging.error(f"ETL pipeline failed: {e}")
        print(f"[ERROR] ETL pipeline failed: {e}")

# ───────────────────────────────────────
# Run
# ───────────────────────────────────────
if __name__ == "__main__":
    run_etl()