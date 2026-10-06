import os

from main import analyze_log

BASE = os.path.dirname(os.path.abspath(__file__))

def path(name):
    return os.path.join(BASE, name)

EMPTY_RESULT = {"total": 0, "by_level": {}, "by_user": {}, "last_error": None}

def test_normal():
    result = analyze_log(path("app.jsonl"))
    assert result["total"] == 5, result
    assert result["by_level"] == {"INFO": 3, "ERROR": 2}, result
    assert result["by_user"] == {"张三": 2, "李四": 2, "王五": 1}, result
    assert result["last_error"] == "超时", result


def test_not_exist():
    result = analyze_log(path("not_exist.jsonl"))
    assert result == EMPTY_RESULT, result

def test_empty_file():
    result = analyze_log(path("empty.jsonl"))
    assert result == EMPTY_RESULT, result

def test_bad_line():
    result = analyze_log(path("bad.jsonl"))
    assert result["total"] == 2, result
    assert result["by_level"] == {"INFO": 1, "ERROR": 1}, result
    assert result["by_user"] == {"张三": 1, "李四": 1}, result
    assert result["last_error"] == "失败", result

if __name__ == "__main__":
    test_normal()
    test_not_exist()
    test_empty_file()
    test_bad_line()
    print("All tests passed!")