"""
load.py

This script loads cleaned shipment data into a SQLite database.

Author: Bita
Date: 2025-07
"""

import sqlite3
import os
import pandas as pd

def load_to_sqlite(df: pd.DataFrame, db_path: str, table_name: str = "shipments"):
    """
    Loads DataFrame into a SQLite database.

    Args:
        df (pd.DataFrame): Cleaned shipment data
        db_path (str): Path to the SQLite database file
        table_name (str): Name of the table to create/replace
    """
    if df.empty:
        print("[WARNING] No data to load.")
        return

    try:
        conn = sqlite3.connect(db_path)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        conn.close()
        print(f"[INFO] Successfully loaded data into SQLite DB: {db_path}")
    except Exception as e:
        print(f"[ERROR] Failed to load data to SQLite: {e}")

# For testing
if __name__ == "__main__":
    from transform import clean_shipment_data
    from extract import extract_csv_data

    # Set paths
    csv_path = os.path.join("data", "shipments.csv")
    db_path = os.path.join("output", "shipments.db")

    # Run full pipeline
    df_raw = extract_csv_data(csv_path)
    df_clean = clean_shipment_data(df_raw)
    load_to_sqlite(df_clean, db_path)