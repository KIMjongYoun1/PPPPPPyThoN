# ============================================================
# 16. NBA 농구 (정답) — typeone.html NBA Q 참고
# ============================================================

import pandas as pd

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
df = pd.read_csv(f"{BASE}/nba/nba.csv", encoding="latin-1", sep=";")

# 예시: 팀(Tm)별 평균 득점(PTS) 상위 5
answer = df.groupby("Tm")["PTS"].mean().sort_values(ascending=False).head(5)
print("팀별 평균 득점 상위 5:")
print(answer)

# 예시: 포지션(Pos)별 선수 수
pos_count = df.groupby("Pos").size().sort_values(ascending=False)
print("\n포지션별 선수 수:")
print(pos_count)

# typeone.html NBA 섹션에서 전체 Q 확인
