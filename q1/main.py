import os
import json

def analyze_log(filepath: str) -> dict:
    result = {
        "total": 0,
        "by_level": {},
        "by_user": {},
        "last_error": None,
    }

    if not os.path.exists(filepath):
            return result

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue

            if not all(key in obj for key in ['timestamp', 'level', 'message', 'user']):
                continue

            result["total"] += 1
            result["by_level"][obj["level"]] = result["by_level"].get(obj["level"], 0) + 1
            result["by_user"][obj["user"]] = result["by_user"].get(obj["user"], 0) + 1

            if obj["level"] == "ERROR":
                result["last_error"] = obj["message"]

    return result