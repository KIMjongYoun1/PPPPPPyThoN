# ============================================================
# 17. Spotify 음악 (정답) — typeone.html Spotify Q 참고
# ============================================================

import pandas as pd

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
df = pd.read_csv(f"{BASE}/spotify/spotify.csv")

# 예시: 아티스트별 곡 수 상위 5
if "artists" in df.columns:
    answer = df["artists"].value_counts().head(5)
    print("아티스트별 곡 수 상위 5:")
    print(answer)

# typeone.html Spotify Q에서 전체 요구사항 확인
