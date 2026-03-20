# ============================================================
# 24. 로지스틱 회귀 이직 예측 (정답)
# ============================================================

import pandas as pd
import numpy as np
from statsmodels.formula.api import logit

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

X_train = pd.read_csv(f"{BASE}/HRdata/X_train.csv")
y_train = pd.read_csv(f"{BASE}/HRdata/y_train.csv")
num_cols = ["city_development_index", "training_hours"]
df = X_train[num_cols].copy()
df["target"] = y_train["target"].values
df = df.dropna()

model = logit("target ~ city_development_index + training_hours", data=df).fit()
print(model.summary())

# Q1: 오즈비
odds_ratio = np.exp(model.params["city_development_index"])
print("Q1 오즈비:", round(odds_ratio, 3))

# Q2: 유의한 변수 회귀계수 (p<0.05, 절편 제외)
sig = model.pvalues[model.pvalues < 0.05].drop("Intercept", errors="ignore")
print("Q2 유의한 변수 회귀계수:", model.params[sig.index].round(3))
