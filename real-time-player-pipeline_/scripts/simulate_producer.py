"""
Simulated event producer (acts like a Kinesis writer).

- OUTSIDE Docker: writes to ./data/kinesis_stream
- INSIDE  Docker: paths are /opt/airflow/data/kinesis_stream

NOW SUPPORTS: --date YYYYMMDD to generate data for any day (for backfills)
Example:
  python scripts/simulate_producer.py --count 80 --date 20250918

If --date is omitted, uses today's UTC date.
"""

import argparse, json, random, time
from datetime import datetime, timezone
from pathlib import Path
from utils import STREAM_DIR, STREAM_BASENAME, ensure_dirs, utc_now_iso

EVENT_TYPES = ["login","logout","match_start","match_end","purchase"]
SKUS = ["skin_emerald","skin_ruby","boost_x2","starter_pack"]
PLATFORMS = ["pc","ps","xbox"]
REGIONS = ["NA","EU","APAC"]

def make_event():
    ev = random.choice(EVENT_TYPES)
    base = {
        "ts": utc_now_iso(),  # timestamp is now; the "date" we store is controlled by file naming & downstream dt
        "player_id": f"p{random.randint(1,1000)}",
        "event": ev,
        "platform": random.choice(PLATFORMS),
        "region": random.choice(REGIONS),
        "session_id": f"s{random.randint(1,10000)}",
    }
    if ev == "purchase":
        base.update({"sku": random.choice(SKUS), "price": round(random.uniform(0.99,19.99),2), "currency":"USD"})
    return base

def main(count:int, interval:float, yyyymmdd:str|None):
    ensure_dirs()
    # determine target date for file naming
    target = yyyymmdd or datetime.now(timezone.utc).strftime("%Y%m%d")
    out_path = STREAM_DIR / f"{STREAM_BASENAME}_{target}.jsonl"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    produced = 0
    with out_path.open("a", encoding="utf-8") as f:
        while True:
            f.write(json.dumps(make_event()) + "\n")
            produced += 1
            if count and produced >= count:
                break
            if interval > 0:
                time.sleep(interval)

    print(f"[producer] wrote {produced} events → {out_path}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=20, help="0 = infinite")
    ap.add_argument("--interval", type=float, default=0.0)
    ap.add_argument("--date", type=str, default=None, help="YYYYMMDD (optional)")
    args = ap.parse_args()
    main(args.count, args.interval, args.date)
