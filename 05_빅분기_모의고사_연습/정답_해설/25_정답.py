# ============================================================
# 25. 다중선형회귀 주택 가격 (정답)
# ============================================================

import pandas as pd
import numpy as np
from statsmodels.formula.api import ols

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

X_train = pd.read_csv(f"{BASE}/redwine/x_train.csv")
y_train = pd.read_csv(f"{BASE}/redwine/y_train.csv")
cols = X_train.columns[:3].tolist()
df = X_train[cols].copy()
df["quality"] = y_train.iloc[:, 0]
df = df.dropna()
df.columns = ["c1", "c2", "c3", "quality"]

model = ols("quality ~ c1 + c2 + c3", data=df).fit()
print(model.summary())

# Q1: 결정계수 R²
print("Q1 R²:", round(model.rsquared, 3))

# Q2: 유의한 변수 회귀계수 합 (p<0.05, 절편 제외)
sig_coefs = model.params[model.pvalues < 0.05].drop("Intercept", errors="ignore")
print("Q2 유의한 변수 회귀계수 합:", round(sig_coefs.sum(), 3))
