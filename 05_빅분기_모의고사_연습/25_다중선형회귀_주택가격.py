# ╔══════════════════════════════════════════════════════════════╗
# ║  [3유형-통계] 25. 다중선형회귀 (와인 품질)                        ║
# ╚══════════════════════════════════════════════════════════════╝
# ★ sklearn 아님 → statsmodels.formula.api.ols 사용
# ★ 결과: round(값, 3) 출력
#
# [3유형 OLS 선형회귀 암기]
#   ols("y ~ c1 + c2 + c3", data=df).fit()  ← formula 형식
#   R²:      model.rsquared
#   유의변수: model.pvalues < 0.05  (절편=Intercept 제외)
#   계수합:  model.params[유의변수].sum()
#   열 이름: 짧게 변경 (c1, c2, c3) → 포뮬러 오류 방지


# ═══ import + 로드
# import pandas as pd
# import numpy as np
# from statsmodels.formula.api import ols
# BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
# X_train = pd.read_csv(f"{BASE}/redwine/x_train.csv")
# y_train = pd.read_csv(f"{BASE}/redwine/y_train.csv")


# ═══ 데이터 준비 (수치열 3개 + 정답 병합, 열명 단순화)
# cols = X_train.columns[:3].tolist()
# df   = X_train[cols].copy()
# df["quality"] = y_train.iloc[:, 0]
# df = df.dropna()
# df.columns = ["c1", "c2", "c3", "quality"]   # ⚠️ 열명 단순화 (한글/특수문자 오류 방지)


# ═══ 모델 학습
# model = ols("quality ~ c1 + c2 + c3", data=df).fit()
# print(model.summary())


# ═══ Q1: 결정계수 R²
# model.rsquared = 모델이 데이터를 얼마나 설명하는지 (0~1, 클수록 좋음)
# print("Q1 R²:", round(model.rsquared, 3))


# ═══ Q2: 유의한 변수(p<0.05) 회귀계수 합 (절편 제외)
# sig_coefs = model.params[model.pvalues < 0.05].drop("Intercept", errors="ignore")
# print("Q2 유의한 계수 합:", round(sig_coefs.sum(), 3))
