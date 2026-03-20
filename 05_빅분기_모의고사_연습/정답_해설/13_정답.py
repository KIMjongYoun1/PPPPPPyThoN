# ============================================================
# 13. RedWine 와인 품질 (정답) — 회귀
# ============================================================

import pandas as pd
from sklearn.ensemble import RandomForestRegressor

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

X_train = pd.read_csv(f"{BASE}/redwine/x_train.csv")
X_test = pd.read_csv(f"{BASE}/redwine/x_test.csv")
y_train = pd.read_csv(f"{BASE}/redwine/y_train.csv")
y_test = pd.read_csv(f"{BASE}/redwine/y_test.csv")

id_col = "ID" if "ID" in X_test.columns else X_test.columns[0]
test_ids = X_test[id_col]
X_train = X_train.drop(columns=[id_col], errors="ignore")
X_test = X_test.drop(columns=[id_col])
y_train = y_train["quality"]

X_train = X_train.fillna(0)
X_test = X_test.fillna(0)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
submission = pd.DataFrame({"ID": test_ids, "quality": pred})
submission.to_csv("submission.csv", index=False)

from sklearn.metrics import mean_squared_error
import numpy as np
print("RMSE:", np.sqrt(mean_squared_error(y_test["quality"], pred)))
