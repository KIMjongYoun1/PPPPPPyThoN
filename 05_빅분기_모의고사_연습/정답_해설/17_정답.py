# ============================================================
# 17. Spotify 음악 (정답 예시)
# │  연습 스크립트 `17_spotify_음악.py` 상단 [수행 요구사항] Q1~Q10과 대응.
# │  열 이름에 공백이 있으면: `df["top genre"]` 처럼 따옴표로 접근.
# ============================================================

import pandas as pd

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
df = pd.read_csv(f"{BASE}/spotify/spotify.csv")

genre_col = "top genre" if "top genre" in df.columns else df.columns[2]

# --- Q1: 아티스트별 곡 수 상위 10 (title 기준 고유 개수) ---
q1 = df.groupby("artist")["title"].nunique().sort_values(ascending=False).head(10)
print("Q1 artist별 title 수 상위 10:")
print(q1)

# --- Q2: 장르별 곡 수 ---
q2 = df[genre_col].value_counts()
print(f"\nQ2 {genre_col}별 곡 수 (일부):")
print(q2.head(10))

# --- Q3: pop >= 80 ---
q3 = (df["pop"] >= 80).sum()
print("\nQ3 pop>=80 곡 개수:", q3)

# 나머지 Q4~Q10은 연습 파일의 열 설명·TODO를 참고.
