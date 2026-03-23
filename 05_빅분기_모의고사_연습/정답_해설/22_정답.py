# ============================================================
# 22. Happy 행복 지수 (정답 예시)
# │  연습 스크립트 `22_happy_행복지수.py` 상단 [수행 요구사항] Q1~Q10과 대응.
# │  CSV 헤더는 한글: `df.columns`로 확인 후 동일 이름 사용.
# ============================================================

import pandas as pd

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
df = pd.read_csv(f"{BASE}/happy/happiness.csv")

# --- Q1: 년도별 나라 수 ---
q1 = df.groupby("년도").size()
print("Q1 년도별 행 수:")
print(q1)

# --- Q2: 2019년 행복랭킹 상위 5 (랭킹 숫자가 작을수록 상위) ---
d19 = df[df["년도"] == 2019]
q2 = d19.nsmallest(5, "행복랭킹")[["나라명", "점수"]]
print("\nQ2 2019 랭킹 상위 5:")
print(q2)

# --- Q4: 상대GDP vs 점수 상관 ---
q4 = df["상대GDP"].corr(df["점수"])
print("\nQ4 상대GDP-점수 상관:", q4)

# --- Q9: Finland 연도별 점수 ---
q9 = df[df["나라명"] == "Finland"].sort_values("년도")[["년도", "점수"]]
print("\nQ9 Finland 연도별 점수:")
print(q9)

# Q3, Q5~Q8, Q10은 연습 파일 TODO·힌트 참고 (pivot/merge, 분위수, LinearRegression 등).
