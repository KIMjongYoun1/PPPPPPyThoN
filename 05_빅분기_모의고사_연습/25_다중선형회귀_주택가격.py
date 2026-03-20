# ============================================================
# 25. 다중선형회귀 (주택 가격)
# [유형] 3유형 (30점) — 가설검정·통계 / 10회 기출
# ============================================================
#
# ---------- [시험 환경] 요구사항 ----------
# 데이터: redwine quality(품질) 회귀
# 제공: x_train, y_train (BASE/redwine/) — 수치형 변수만
# 방법: statsmodels ols (sklearn 아님)
# 제출: 소수 셋째 자리까지 반올림
#
# ---------- [추출해야 할 내용 / 정답 형식] ----------
# Q1: 결정계수 R² → round(model.rsquared, 3)
# Q2: 유의한 변수(p<0.05) 회귀계수 합 → round(합, 3)
# (절편 제외, pvalues < 0.05인 변수 회귀계수만 합산)
#
# ---------- [학습 목표] ----------
# 나중에 주석 지우고 [기본 제공] + [요구사항]만 보고 연습
# ============================================================
#
# [기본 제공] Step 1~4 | [작성] Step 5~7
# ============================================================

# ---------- [기본 제공] Step 1: import ----------
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols

# ---------- [기본 제공] Step 2: BASE URL ----------
BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

# ---------- [기본 제공] Step 3: 데이터 로드 & 병합 ----------
X_train = pd.read_csv(f"{BASE}/redwine/x_train.csv")
y_train = pd.read_csv(f"{BASE}/redwine/y_train.csv")
cols = X_train.columns[:3].tolist()
df = X_train[cols].copy()
df["quality"] = y_train.iloc[:, 0]
df = df.dropna()
df.columns = ["c1", "c2", "c3", "quality"]

# ---------- [기본 제공] Step 4: formula 준비 ----------
# formula = "quality ~ c1 + c2 + c3"

# ---------- [작성] Step 5: 다중선형회귀 적합 ----------
# TODO: model = ols("quality ~ c1 + c2 + c3", data=df).fit()
# TODO: print(model.summary())

# ---------- [작성] Step 6: Q1 결정계수 R² ----------
# TODO: print("R²:", round(model.rsquared, 3))

# ---------- [작성] Step 7: Q2 유의한 변수 회귀계수 합 ----------
# TODO: sig_coefs = model.params[model.pvalues < 0.05].drop("Intercept", errors="ignore")
# TODO: print("유의한 변수 회귀계수 합:", round(sig_coefs.sum(), 3))
