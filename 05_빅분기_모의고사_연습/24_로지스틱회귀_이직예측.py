# ============================================================
# 24. 로지스틱 회귀 (이직 예측)
# [유형] 빅분기 실기 3유형 — 통계 모델링 (연습: HRdata, 기출 유사 / **sklearn 아님**)
# ============================================================
#
# ┌─ [문제 목표] ─────────────────────────────────────────────
# │  **이직 여부(target)** 와 연관된 **수치형 설명변수**만으로 **로지스틱 회귀**를 맞추고,
# │  **오즈비**·**유의한 변수의 회귀계수**를 숫자로 낸다.
# └──────────────────────────────────────────────────────────
#
# ┌─ [제공 데이터] ───────────────────────────────────────────
# │  경로: BASE/HRdata/X_train.csv, y_train.csv
# │  · 이 연습 파일: **city_development_index**, **training_hours** 만 사용 (문제지와 다를 수 있음).
# └──────────────────────────────────────────────────────────
#
# ┌─ [수행 요구사항] ─────────────────────────────────────────
# │  ① `statsmodels.formula.api.logit` 로 `target ~ 변수1 + 변수2` 적합.
# │  ② 결측 행 제거 후 적합 (`dropna`).
# │  ③ Q1: 특정 변수 **오즈비** = `np.exp(그 변수의 계수)`.
# │  ④ Q2: **p < 0.05** 인 변수의 **회귀계수** (절편 Intercept 제외) 출력, **round(..., 3)**.
# └──────────────────────────────────────────────────────────
#
# ┌─ [산출물 / 정답 형식] ───────────────────────────────────
# │  · **round(값, 3)**. submission.csv 가 아니라 **문제가 요구하는 통계값**.
# └──────────────────────────────────────────────────────────
#
# ┌─ [평가·연습 시 참고] ─────────────────────────────────────
# │  · **RandomForest / sklearn 로지스틱** 이 아니라 **statsmodels logit** 이 정답 루트인 문항.
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
from statsmodels.formula.api import logit

# ---------- [기본 제공] Step 2: BASE URL ----------
BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

# ---------- [작성] Step 3: 데이터 로드 & 병합 ----------
# TODO: X_train = pd.read_csv(f"{BASE}/HRdata/X_train.csv")
# TODO: y_train = pd.read_csv(f"{BASE}/HRdata/y_train.csv")
# TODO: num_cols = ["city_development_index", "training_hours"]
# TODO: df = X_train[num_cols].copy()
# TODO: df["target"] = y_train["target"].values
# TODO: df = df.dropna()

# ---------- [기본 제공] Step 4: formula 준비 ----------
# formula = "target ~ city_development_index + training_hours"

# ---------- [작성] Step 5: 로지스틱 회귀 적합 ----------
# TODO: model = logit("target ~ city_development_index + training_hours", data=df).fit()
# TODO: print(model.summary())

# ---------- [작성] Step 6: Q1 오즈비 ----------
# TODO: odds_ratio = np.exp(model.params["city_development_index"])
# TODO: print("오즈비:", round(odds_ratio, 3))

# ---------- [작성] Step 7: Q2 유의한 변수 회귀계수 ----------
# TODO: sig = model.pvalues[model.pvalues < 0.05].drop("Intercept", errors="ignore")
# TODO: print("유의한 변수 회귀계수:", model.params[sig.index].round(3))
