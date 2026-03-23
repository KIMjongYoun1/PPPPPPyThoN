# ============================================================
# 16. NBA 농구 (정답 예시)
# │  연습 스크립트 `16_nba_농구.py` 상단 [수행 요구사항] Q1~Q10과 대응.
# ============================================================

import pandas as pd

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
df = pd.read_csv(f"{BASE}/nba/nba.csv", encoding="latin-1", sep=";")

# --- Q1: 팀별 평균 득점 상위 5 ---
q1 = df.groupby("Tm")["PTS"].mean().sort_values(ascending=False).head(5)
print("Q1 팀별 평균 PTS 상위 5:")
print(q1)

# --- Q2: 포지션별 선수 수 ---
q2 = df.groupby("Pos").size().sort_values(ascending=False)
print("\nQ2 포지션별 선수 수:")
print(q2)

# --- Q3: PTS 상위 10명 ---
q3 = df.nlargest(10, "PTS")[["Player", "PTS"]]
print("\nQ3 PTS 상위 10명:")
print(q3)

# 나머지 Q4~Q10은 연습 파일 TODO·힌트를 참고해 동일 패턴으로 작성.
