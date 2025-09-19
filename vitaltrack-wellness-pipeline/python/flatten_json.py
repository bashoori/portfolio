# 🐍 Python: flatten_json.py
# Goal: Flatten nested mobile activity logs into a flat dictionary

def flatten_activity_log(data):
    return {
        "user_id": data["user"]["id"],
        "user_name": data["user"]["name"],
        "steps": data["metrics"]["steps"],
        "sleep_hours": data["metrics"]["sleep"]["hours"],
        "sleep_quality": data["metrics"]["sleep"]["quality"],
        "timestamp": data["timestamp"]
    }

# Example usage
if __name__ == "__main__":
    sample = {
        "user": {"id": 101, "name": "Bita"},
        "metrics": {"steps": 8721, "sleep": {"hours": 7.5, "quality": "good"}},
        "timestamp": "2024-10-02T08:00:00"
    }

    flat = flatten_activity_log(sample)
    print(flat)
