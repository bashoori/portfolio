"""
extract.py

This script reads raw shipment data from a CSV file
and returns it as a Pandas DataFrame.

Author: Bita
Date: 2025-07
"""

import pandas as pd
import os

def extract_csv_data(file_path: str) -> pd.DataFrame:
    """
    Reads shipment data from a CSV file and returns a DataFrame.
    Args:
        file_path (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Data from the CSV as a DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"[INFO] Successfully extracted data from {file_path}")
        return df
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return pd.DataFrame()
    except Exception as e:
        print(f"[ERROR] Failed to read CSV: {e}")
        return pd.DataFrame()


# For testing directly
if __name__ == "__main__":
    csv_path = os.path.join( "data", "shipments.csv")
    df = extract_csv_data(csv_path)
    print(df.head())