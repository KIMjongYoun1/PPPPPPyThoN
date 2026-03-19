# ============================================================
# 13. 데이터 수집 (빅분기·실무)
# ============================================================
#
# [데이터 형태 — 정형·반정형·비정형]
# - 정형: 표 형태. CSV, Excel, DB 테이블. 행·열 구조가 고정.
# - 반정형: 구조는 있지만 표보다 유연. JSON, XML. 키-값, 중첩 구조.
# - 비정형: 자유 형식. 텍스트, 로그, SNS 글. 구조화하려면 전처리 필요.
#
# [실기에서 보는 것]
# - 정형: CSV/Excel 파일 읽기 (pd.read_csv, pd.read_excel)
# - 반정형: JSON 파싱 (json.loads, json.load), API 응답 → DataFrame 변환
# - 비정형: 텍스트 파일 읽기, 간단한 파싱
#
# [JSON이란]
# - {"키": "값", "리스트": [1,2,3]} 형태의 문자열 또는 파일.
# - API 응답이 대부분 JSON. 파이썬에서는 딕셔너리/리스트로 변환해서 씀.
# - json.loads(문자열) → 딕셔너리/리스트. json.load(파일객체) → 파일에서 읽기.
#
# [API 수집 흐름]
# 1) requests.get(URL) 로 HTTP 요청
# 2) 응답이 JSON이면 .json() 으로 딕셔너리/리스트 변환
# 3) pd.DataFrame(리스트) 로 표 형태로 만들어 분석
# 시험에서는 URL·API 키가 문제에 주어지므로, 그대로 넣어서 get 후 파싱하면 됨.
#
# [import — 각 모듈 역할]
# json: JSON 문자열 파싱(loads), JSON 파일 읽기(load). API 응답 파싱에 사용.
# os: 파일 경로 처리. os.path.join(폴더,파일명), os.path.dirname(__file__), os.path.exists(경로).
# pandas (pd): 리스트·딕셔너리 → DataFrame(표) 변환. pd.DataFrame(rows).
# requests (선택): HTTP 요청. r = requests.get(url), data = r.json(). pip install 필요.
# ============================================================

import json
import os

# ---------- 따라 칠 코드 (1): JSON 문자열 파싱 ----------
# API 응답이 문자열로 오면 json.loads() 로 딕셔너리/리스트로 변환
raw = '{"name": "철수", "scores": [80, 90]}'
data = json.loads(raw)
print(data["name"], data["scores"])

import json
import os

raw = '{"name": "chulsu", "scores": [90, 90], "name2": "young"}'
data = json.loads(raw)
print(data["name"],"+", data["name2"],"+", data["scores"])

# ---------- 따라 칠 코드 (2): JSON 파일 읽기 ----------
# 실전: 공개 데이터가 .json 파일로 제공되는 경우
sample_json = os.path.join(os.path.dirname(__file__), "sample_data.json")
if os.path.exists(sample_json):
    with open(sample_json, "r", encoding="utf-8") as f:
        loaded = json.load(f)
    print(loaded)
else:
    # 파일 없으면 메모리에서 연습
    d = [{"id": 1, "value": 10}, {"id": 2, "value": 20}]
    print("JSON 리스트 예:", d)


import json
import os
sample_json = os.path.join(os.path.dirname(__file__), "sample_data.json")
if os.path.exists(sample_json):
    with open(sample_json, "r", encoding="utf-8") as f:
        loaded = json.load(f)
    print(loaded)
else:
    d = [{"id":1, "value": 10}, {"id":2, "value": 20}]
    print("JsonList: ", d)

# ---------- 따라 칠 코드 (3): 리스트 딕셔너리 → DataFrame (표로 만들기) ----------

import pandas as pd
rows = [
    {"이름": "A", "점수": 85},
    {"이름": "B", "점수": 90},
]
df = pd.DataFrame(rows)
print(df)

import pandas as pd
row = [
    {"name": "a", "score": 99},
    {"name": "b", "score": 88},
]
df = pd.DataFrame(row)
print(df)

# ---------- 따라 칠 코드 (4): requests로 API 호출 (선택) ----------
# 실기·실무에서 "공개 데이터 수집" 시 URL 제공되는 경우 사용.
# pip install requests 필요. 네트워크 필요.
try:
    import requests
    # 예: 공개 API (실제 시험에서는 문제에 주어진 URL 사용)
    # r = requests.get("https://api.example.com/data", timeout=5)
    # data = r.json()
    # df = pd.DataFrame(data)
    print("requests 사용 가능. 시험 시 문제의 URL로 get 후 .json() → DataFrame 변환.")
except ImportError:
    print("requests 미설치. pip install requests 후 API 호출 연습 가능.")

try:
    import requests
    r = requests.get("https://api.example.com/data", timeout=5)
    data = r.json()
    df = pd.DataFrame(data)
    print("requests.get -> json -> DataFrame: ", df)
except ImportError:
    print("requeestx does not exist -> pip install requests -> api url get call")

# ---------- 예제 ----------
# 아래 문자열을 JSON으로 파싱한 뒤, "items" 안의 첫 번째 요소의 "name"을 출력하세요.

s = '{"items": [{"name": "사과", "price": 1000}, {"name": "바나나", "price": 500}]}'
parsed = json.loads(s)
print(parsed["items"][0]["name"])

import json
s = '{"items": [{"name": "apple", "price": 1000}, {"neme":"banana", "price": 2000}]}'
parsed = json.loads(s)
item1 = parsed["items"][0]
print(parsed["items"][0]["name"], ":",parsed["items"][0]["price"])
print(item1)
