import os
import json

def analyze_log(filepath: str) -> dict:
    result = {
        "total": 0,
        "by_level": {
            "INFO": 0,
            "ERROR": 0,
        },
        "by_user": {
            "张三": 0,
            "李四": 0,
            "王五": 0,
        },
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
            result["by_level"][obj["level"]] += 1
            result["by_user"][obj["user"]] += 1

            if obj["level"] == "ERROR":
                result["last_error"] = obj["message"]

    return result

    return results