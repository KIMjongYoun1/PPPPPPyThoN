# ╔══════════════════════════════════════════════════════════════╗
# ║  [1유형-집계] 18. Weather 날씨 시계열 Q1~Q10                   ║
# ╚══════════════════════════════════════════════════════════════╝
# ★ 핵심: 시계열 처리 → pd.to_datetime 후 .dt 속성 활용
#   ※ 지문 판단법: "Q1. ~를 구하시오" 형태로 질문 여러 개 나열 → 1유형
#                  "예측하시오" 없음, submission 제출 없음 → print()로 출력
#                  import: pandas만
#
# [시계열 .dt 속성 암기]
#   .dt.date          → 날짜(일) 단위
#   .dt.to_period("M")→ 월 단위 (2020-01 형태)
#   .dt.year / .dt.month / .dt.hour  → 연/월/시
#   .dt.day_name()    → 요일 문자 (Monday, Sunday...)
#   .dt.dayofweek >= 5 → 주말 (5=토, 6=일)


# ═══ import + 로드
# import pandas as pd
# BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
# df = pd.read_csv(f"{BASE}/weather/weather2.csv")
# df["time"] = pd.to_datetime(df["time"])   # ★ 첫 줄에서 datetime 변환


# ═══ Q1: 전체 행 개수
# print("Q1:", len(df))


# ═══ Q2: 일별 이화동기온 평균
# groupby(df["열"].dt.date) = 날짜별 그룹
# daily_temp = df.groupby(df["time"].dt.date)["이화동기온"].mean()
# print("Q2:", daily_temp.head())


# ═══ Q3: 월별 수영동강수 합
# .dt.to_period("M") = 2020-01 형태로 월 그룹
# monthly_rain = df.groupby(df["time"].dt.to_period("M"))["수영동강수"].sum()
# print("Q3:", monthly_rain.head())


# ═══ Q4: 이화동기온 0 이상 시각 수
# q4 = (df["이화동기온"] >= 0).sum()
# print("Q4:", q4)


# ═══ Q5: 시간(0~23)별 이화동기온 평균
# q5 = df.groupby(df["time"].dt.hour)["이화동기온"].mean()
# print("Q5:", q5)


# ═══ Q6: 수영동기온 − 이화동기온 차이 전체 평균
# q6 = (df["수영동기온"] - df["이화동기온"]).mean()
# print("Q6:", q6)


# ═══ Q7: 일별 이화동강수 합 최대 날짜
# q7 = df.groupby(df["time"].dt.date)["이화동강수"].sum().idxmax()
# print("Q7:", q7)


# ═══ Q8: 주말 vs 평일 이화동기온 평균
# .dt.dayofweek: 0=월...4=금, 5=토, 6=일
# weekend = df["time"].dt.dayofweek >= 5
# print("Q8 주말:", df[weekend]["이화동기온"].mean())
# print("Q8 평일:", df[~weekend]["이화동기온"].mean())


# ═══ Q9: 2020년 1월 일별 이화동기온 최댓값
# q9 = df[(df["time"].dt.year == 2020) & (df["time"].dt.month == 1)] \
#     .groupby(df["time"].dt.date)["이화동기온"].max()
# print("Q9:", q9)


# ═══ Q10: 이화동기온 ↔ 수영동기온 상관계수
# df["열1"].corr(df["열2"]) = 피어슨 상관계수
# q10 = df["이화동기온"].corr(df["수영동기온"])
# print("Q10:", q10)
