"""
Runs in Airflow container.
Simple DQ checks on Silver CSV; prints summary (could be sent to CloudWatch/SNS in prod).

Input : /opt/airflow/data/s3/silver/silver_YYYYMMDD.csv
"""

import csv
from datetime import datetime
from utils import silver_path_for_date, ensure_dirs

ALLOWED_PLATFORMS = {"pc","ps","xbox"}
ALLOWED_REGIONS = {"NA","EU","APAC"}

def main():
    ensure_dirs()
    today = datetime.utcnow().strftime("%Y%m%d")
    silver = silver_path_for_date(today)
    if not silver.exists():
        print("[dq] no silver file.")
        return

    total=bad_player=bad_price=bad_platform=bad_region=0
    with silver.open("r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            total += 1
            if not row["player_id"]:
                bad_player += 1
            try:
                if float(row["price"]) < 0:
                    bad_price += 1
            except Exception:
                bad_price += 1
            if row["platform"] not in ALLOWED_PLATFORMS:
                bad_platform += 1
            if row["region"] not in ALLOWED_REGIONS:
                bad_region += 1

    print(f"[dq] total={total} bad_player={bad_player} bad_price={bad_price} bad_platform={bad_platform} bad_region={bad_region}")

if __name__ == "__main__":
    main()
