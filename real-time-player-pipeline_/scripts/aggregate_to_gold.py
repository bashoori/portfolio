"""
Aggregate Silver -> Gold (daily KPIs).

Input : data/s3/silver/silver_YYYYMMDD.csv
Output: data/s3/gold/gold_agg_YYYYMMDD.csv

NOW SUPPORTS: --date YYYYMMDD (defaults to today UTC)
"""

import argparse, csv
from datetime import datetime, timezone
from utils import silver_path_for_date, gold_path_for_date, write_csv, ensure_dirs

def main(yyyymmdd:str|None):
    ensure_dirs()
    target = yyyymmdd or datetime.now(timezone.utc).strftime("%Y%m%d")
    silver = silver_path_for_date(target)
    gold = gold_path_for_date(target)

    if not silver.exists():
        print("[gold] no silver file.")
        return

    players=set(); events=0; purchases=0; revenue=0.0
    dt_val = f"{target[:4]}-{target[4:6]}-{target[6:8]}"

    with silver.open("r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            events += 1
            players.add(row["player_id"])
            if row["event"] == "purchase":
                try: revenue += float(row["price"]); purchases += 1
                except: pass

    rows = [{
        "dt": dt_val,
        "dau": len(players),
        "events": events,
        "purchases": purchases,
        "revenue": round(revenue, 2),
    }]

    write_csv(gold, fieldnames=["dt","dau","events","purchases","revenue"], rows=rows)
    print(f"[gold] wrote aggregates → {gold}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", type=str, default=None, help="YYYYMMDD (optional)")
    args = ap.parse_args()
    main(args.date)
