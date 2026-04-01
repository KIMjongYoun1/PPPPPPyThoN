# ╔══════════════════════════════════════════════════════════════╗
# ║  [3유형-통계] 24. 로지스틱 회귀 (이직 예측)                       ║
# ╚══════════════════════════════════════════════════════════════╝
# ★ sklearn 아님 → statsmodels.formula.api.logit 사용
# ★ 결과: round(값, 3) 출력
#
# [3유형 로지스틱 회귀 암기]
#   logit("y ~ x1 + x2", data=df).fit()  ← formula 형식
#   오즈비: np.exp(model.params["변수명"])
#   유의변수: model.pvalues < 0.05  (절편=Intercept 제외)
#   결측 제거: df.dropna() 후 fit


# ═══ import + 로드
# import pandas as pd
# import numpy as np
# from statsmodels.formula.api import logit
# BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
# X_train = pd.read_csv(f"{BASE}/HRdata/X_train.csv")
# y_train = pd.read_csv(f"{BASE}/HRdata/y_train.csv")


# ═══ 데이터 준비 (수치형 변수 + 정답 병합)
# num_cols = ["city_development_index", "training_hours"]
# df = X_train[num_cols].copy()
# df["target"] = y_train["target"].values
# df = df.dropna()   # 결측 행 제거 필수


# ═══ 모델 학습
# 포뮬러: "정답 ~ 변수1 + 변수2" 형식으로 작성
# model = logit("target ~ city_development_index + training_hours", data=df).fit()
# print(model.summary())


# ═══ Q1: 오즈비 (city_development_index 변수)
# 오즈비 = np.exp(회귀계수)
# odds_ratio = np.exp(model.params["city_development_index"])
# print("Q1 오즈비:", round(odds_ratio, 3))


# ═══ Q2: 유의한 변수(p<0.05) 회귀계수 (절편 제외)
# sig = model.pvalues[model.pvalues < 0.05].drop("Intercept", errors="ignore")
# print("Q2 유의한 변수 회귀계수:", model.params[sig.index].round(3))
