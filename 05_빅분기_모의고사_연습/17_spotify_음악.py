# ╔══════════════════════════════════════════════════════════════╗
# ║  [1유형-집계] 17. Spotify 음악 차트 Q1~Q10                     ║
# ╚══════════════════════════════════════════════════════════════╝
# ★ ⚠️ 열 이름에 공백 있음: "top genre", "year released" → df["top genre"]
# ★ 날짜처리: pd.to_datetime(df["added"], errors="coerce") → .dt.year


# ═══ import + 로드
# import pandas as pd
# BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
# df = pd.read_csv(f"{BASE}/spotify/spotify.csv")
# genre_col = "top genre" if "top genre" in df.columns else df.columns[2]


# ═══ Q1: artist별 곡 수 상위 10
# nunique() = 고유값 개수 / count() = 비결측 개수 (구분 주의)
# q1 = df.groupby("artist")["title"].nunique().sort_values(ascending=False).head(10)
# print("Q1:", q1)


# ═══ Q2: 장르별 곡 수 (많은 순)
# q2 = df[genre_col].value_counts()
# print("Q2:", q2.head(10))


# ═══ Q3: pop >= 80 곡 개수
# q3 = (df["pop"] >= 80).sum()
# print("Q3:", q3)


# ═══ Q4: 연도별 평균 bpm
# q4 = df.groupby("year released")["bpm"].mean()
# print("Q4:", q4)


# ═══ Q5: nrgy 최대 곡 title
# .idxmax() → 최대값 인덱스 → df.loc[인덱스, "열"]
# q5 = df.loc[df["nrgy"].idxmax(), "title"]
# print("Q5:", q5)


# ═══ Q6: artist type별 곡 수
# q6 = df["artist type"].value_counts()
# print("Q6:", q6)


# ═══ Q7: dnce 상위 5곡 title
# q7 = df.nlargest(5, "dnce")["title"].tolist()
# print("Q7:", q7)


# ═══ Q8: top year == 2010 → top genre 빈도 상위 3
# q8 = df[df["top year"] == 2010][genre_col].value_counts().head(3)
# print("Q8:", q8)


# ═══ Q9: 장르별 dur 평균 가장 긴 장르
# q9 = df.groupby(genre_col)["dur"].mean().idxmax()
# print("Q9:", q9)


# ═══ Q10: added 연도별 곡 수
# errors="coerce" → 변환 불가 값은 NaT(결측)으로 처리
# df["added"] = pd.to_datetime(df["added"], errors="coerce")
# q10 = df["added"].dt.year.value_counts().sort_index()
# print("Q10:", q10)
