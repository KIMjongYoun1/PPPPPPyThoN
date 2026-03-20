# ============================================================
# 14. KingCountyPrice 주택 가격 (정답) — 회귀
# ============================================================

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

X_train = pd.read_csv(f"{BASE}/kingcountyprice/x_train.csv")
X_test = pd.read_csv(f"{BASE}/kingcountyprice/x_test.csv")
y_train = pd.read_csv(f"{BASE}/kingcountyprice/y_train.csv")
y_test = pd.read_csv(f"{BASE}/kingcountyprice/y_test.csv")

id_col = "ID" if "ID" in X_test.columns else X_test.columns[0]
test_ids = X_test[id_col]
X_train = X_train.drop(columns=[id_col], errors="ignore")
X_test = X_test.drop(columns=[id_col])
y_train = y_train["price"]

cat_cols = X_train.select_dtypes(include=["object"]).columns.tolist()
for col in cat_cols:
    le = LabelEncoder()
    X_train[col] = le.fit_transform(X_train[col].astype(str))
    X_test[col] = le.transform(X_test[col].astype(str))

X_train = X_train.fillna(0)
X_test = X_test.fillna(0)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
submission = pd.DataFrame({"ID": test_ids, "price": pred})
submission.to_csv("submission.csv", index=False)
print("RMSE:", (pd.Series(pred - y_test["price"].values) ** 2).mean() ** 0.5)
