# ╔══════════════════════════════════════════════════════════════╗
# ║  [1유형-집계] 22. Happy 행복 지수 Q1~Q10                       ║
# ╚══════════════════════════════════════════════════════════════╝
# ★ 열: 행복랭킹, 나라명, 점수, 상대GDP, 사회적지원, 년도 등 (한글)
# ★ 파일: happy/happiness.csv
#
# [피벗/병합 패턴 암기]
#   상관계수: df["열1"].corr(df["열2"])
#   분위수:   df["열"].quantile(0.9)
#   선형회귀: from sklearn.linear_model import LinearRegression


# ═══ import + 로드
# import pandas as pd
# BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
# df = pd.read_csv(f"{BASE}/happy/happiness.csv")


# ═══ Q1: 년도별 나라 수
# q1 = df.groupby("년도").size()
# print("Q1:", q1)


# ═══ Q2: 2019년 행복랭킹 상위 5개국 (랭킹 숫자 작을수록 상위)
# .nsmallest(N, "열") = 값이 가장 작은 N개
# d19 = df[df["년도"] == 2019]
# q2  = d19.nsmallest(5, "행복랭킹")[["나라명", "점수"]]
# print("Q2:", q2)


# ═══ Q3: 나라명별 점수 평균 상위 5개국
# q3 = df.groupby("나라명")["점수"].mean().sort_values(ascending=False).head(5)
# print("Q3:", q3)


# ═══ Q4: 상대GDP ↔ 점수 피어슨 상관계수
# q4 = df["상대GDP"].corr(df["점수"])
# print("Q4:", q4)


# ═══ Q5: 년도별 점수 평균
# q5 = df.groupby("년도")["점수"].mean()
# print("Q5:", q5)


# ═══ Q6: 2019년 부패인식 가장 낮은 국가
# q6 = df[df["년도"] == 2019].nsmallest(1, "부패에 대한인식")["나라명"].values[0]
# print("Q6:", q6)


# ═══ Q7: 2019년 사회적지원 상위 10% (quantile 0.9 이상) 국가 점수 평균
# d19  = df[df["년도"] == 2019]
# q0_9 = d19["사회적지원"].quantile(0.9)
# q7   = d19[d19["사회적지원"] >= q0_9]["점수"].mean()
# print("Q7:", q7)


# ═══ Q8: 선택의 자유도(X) → 점수(y) 1차 회귀 기울기
# from sklearn.linear_model import LinearRegression
# import numpy as np
# X8 = df[["선택의 자유도"]].dropna()
# y8 = df.loc[X8.index, "점수"]
# lr = LinearRegression().fit(X8, y8)
# print("Q8 기울기:", lr.coef_[0])


# ═══ Q9: Finland 연도별 점수
# q9 = df[df["나라명"] == "Finland"].sort_values("년도")[["년도", "점수"]]
# print("Q9:", q9)


# ═══ Q10: 2018↔2019 모두 등장한 나라 중 점수 상승 최대 나라
# d18 = df[df["년도"] == 2018][["나라명","점수"]].set_index("나라명")
# d19 = df[df["년도"] == 2019][["나라명","점수"]].set_index("나라명")
# both = d18.join(d19, lsuffix="_18", rsuffix="_19").dropna()
# q10  = (both["점수_19"] - both["점수_18"]).idxmax()
# print("Q10:", q10)
