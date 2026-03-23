# ============================================================
# 18. Weather 날씨 (정답 예시)
# │  연습 스크립트 `18_weather_날씨.py` 상단 [수행 요구사항] Q1~Q10과 대응.
# ============================================================

import pandas as pd

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
df = pd.read_csv(f"{BASE}/weather/weather2.csv")
df["time"] = pd.to_datetime(df["time"])

# --- Q1: 행 개수 ---
print("Q1 시각(행) 개수:", len(df))

# --- Q2: 일별 이화동기온 평균 (앞 5일만 출력 예시) ---
daily_temp = df.groupby(df["time"].dt.date)["이화동기온"].mean()
print("\nQ2 일별 이화동기온 평균 (head):")
print(daily_temp.head())

# --- Q3: 월별 수영동강수 합 ---
monthly_rain = df.groupby(df["time"].dt.to_period("M"))["수영동강수"].sum()
print("\nQ3 월별 수영동강수 합 (head):")
print(monthly_rain.head())

# --- Q10: 두 지점 기온 상관 ---
print("\nQ10 이화동-수영동 기온 상관:", df["이화동기온"].corr(df["수영동기온"]))

# Q4~Q9는 연습 파일 TODO 참고.
