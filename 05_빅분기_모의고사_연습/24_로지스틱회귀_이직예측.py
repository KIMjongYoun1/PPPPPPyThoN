# ============================================================
# 24. 로지스틱 회귀 (이직 예측)
# [유형] 3유형 (30점) — 가설검정·통계 / 10회 기출
# ============================================================
#
# ---------- [시험 환경] 요구사항 ----------
# 데이터: HRdata 이직(target) 예측
# 제공: X_train, y_train (BASE/HRdata/) — 수치형 변수만 사용
# 방법: statsmodels logit (sklearn 아님)
# 제출: 소수 셋째 자리까지 반올림
#
# ---------- [추출해야 할 내용 / 정답 형식] ----------
# Q1: 오즈비(odds ratio) — np.exp(회귀계수) → round(값, 3)
# Q2: 유의한 변수(p<0.05) 회귀계수 → round(값, 3)
# (절편 제외, pvalues < 0.05인 변수만)
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
from statsmodels.formula.api import logit

# ---------- [기본 제공] Step 2: BASE URL ----------
BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

# ---------- [기본 제공] Step 3: 데이터 로드 & 병합 ----------
X_train = pd.read_csv(f"{BASE}/HRdata/X_train.csv")
y_train = pd.read_csv(f"{BASE}/HRdata/y_train.csv")
num_cols = ["city_development_index", "training_hours"]
df = X_train[num_cols].copy()
df["target"] = y_train["target"].values
df = df.dropna()

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
