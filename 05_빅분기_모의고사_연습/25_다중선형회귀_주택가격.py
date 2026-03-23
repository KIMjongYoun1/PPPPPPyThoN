# ============================================================
# 25. 다중선형회귀 (와인 품질)
# [유형] 빅분기 실기 3유형 — 통계 회귀 (연습: redwine / **sklearn 아님**)
# ============================================================
#
# ┌─ [문제 목표] ─────────────────────────────────────────────
# │  수치형 설명변수로 **와인 품질(quality)** 을 **선형회귀(OLS)** 로 맞추고,
# │  **R²** 와 **유의한 변수 계수의 합**을 숫자로 낸다. (파일 제목은 ‘주택’이었으나 본 연습 데이터는 redwine)
# └──────────────────────────────────────────────────────────
#
# ┌─ [제공 데이터] ───────────────────────────────────────────
# │  경로: BASE/redwine/x_train.csv, y_train.csv
# │  · 이 연습 파일: 앞쪽 **수치 열 3개 + quality** 만 병합해 사용 (c1,c2,c3 로 이름 변경됨).
# └──────────────────────────────────────────────────────────
#
# ┌─ [수행 요구사항] ─────────────────────────────────────────
# │  ① `statsmodels.formula.api.ols` 로 `quality ~ c1 + c2 + c3` 적합.
# │  ② 결측 제거 후 적합.
# │  ③ Q1: **결정계수 R²** → `model.rsquared` 를 **round(..., 3)**.
# │  ④ Q2: **p < 0.05** 인 설명변수의 **회귀계수만** 골라 **합** (절편 제외) → **round(..., 3)**.
# └──────────────────────────────────────────────────────────
#
# ┌─ [산출물 / 정답 형식] ───────────────────────────────────
# │  · **round(값, 3)**. submission.csv 아님.
# └──────────────────────────────────────────────────────────
#
# ┌─ [평가·연습 시 참고] ─────────────────────────────────────
# │  · 3유형은 **ols / logit** 등 **statsmodels** 패턴이 빈번함.
# └──────────────────────────────────────────────────────────
#
# [학습 방법] import·BASE 참고. **Step 3: csv 읽기 + 분석용 df 만들기** 직접 작성.
#            Step 4는 formula 힌트. Step 5~7 직접 작성.
# ============================================================
#
# [기본 제공] Step 1~2, 4 | [작성] Step 3, 5~7
# ============================================================

# ---------- [기본 제공] Step 1: import ----------
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols

# ---------- [기본 제공] Step 2: BASE URL ----------
BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

# ---------- [작성] Step 3: 데이터 로드 & 병합 ----------
# TODO: X_train = pd.read_csv(f"{BASE}/redwine/x_train.csv")
# TODO: y_train = pd.read_csv(f"{BASE}/redwine/y_train.csv")
# TODO: cols = X_train.columns[:3].tolist()
# TODO: df = X_train[cols].copy()
# TODO: df["quality"] = y_train.iloc[:, 0]
# TODO: df = df.dropna()
# TODO: df.columns = ["c1", "c2", "c3", "quality"]

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
