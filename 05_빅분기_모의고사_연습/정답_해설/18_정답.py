# ============================================================
# 18. Weather 날씨 (정답) — typeone.html Weather Q 참고
# ============================================================

import pandas as pd

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
df = pd.read_csv(f"{BASE}/weather/weather2.csv")

# 예시: 날짜 컬럼이 있으면 시계열 집계
if "date" in df.columns or len(df.columns) > 0:
    df_temp = df.copy()
    # 첫 번째 datetime 컬럼으로 요일/월별 집계
    for c in df_temp.columns:
        if "date" in c.lower() or "time" in c.lower():
            df_temp[c] = pd.to_datetime(df_temp[c])
            break
    print("데이터 shape:", df.shape)
    print(df.head())

# typeone.html Weather Q에서 전체 요구사항 확인
