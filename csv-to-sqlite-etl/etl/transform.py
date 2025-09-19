"""
transform.py

This script cleans and standardizes the extracted shipment data.

Author: Bita
Date: 2025-07
"""

import pandas as pd

def clean_shipment_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and standardize the shipment DataFrame.

    Args:
        df (pd.DataFrame): Raw shipment data

    Returns:
        pd.DataFrame: Cleaned and formatted data
    """

    if df.empty:
        print("[WARNING] Input DataFrame is empty. Skipping transform.")
        return df

    # 1. Drop rows with missing shipment_id or destination
    df = df.dropna(subset=["shipment_id", "destination"])

    # 2. Fill missing status with 'Unknown'
    df["status"] = df["status"].fillna("Unknown")

    # 3. Convert date columns to datetime (standard format)
    date_cols = ["departure_date", "arrival_date"]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors="coerce").dt.date

    # 4. Remove rows where both departure and arrival are missing
    df = df.dropna(subset=["departure_date", "arrival_date"], how="all")

    print(f"[INFO] Data cleaned: {len(df)} rows remaining.")
    return df

# For testing
if __name__ == "__main__":
    from extract import extract_csv_data
    import os

    path = os.path.join("data", "shipments.csv")
    raw_df = extract_csv_data(path)
    cleaned_df = clean_shipment_data(raw_df)
    print(cleaned_df.head())