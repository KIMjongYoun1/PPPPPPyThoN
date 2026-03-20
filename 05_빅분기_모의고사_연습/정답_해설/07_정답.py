# ============================================================
# 07. Diabetes 당뇨병 (정답)
# ============================================================

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

X_train = pd.read_csv(f"{BASE}/diabetes/x_train.csv")
X_test = pd.read_csv(f"{BASE}/diabetes/x_test.csv")
y_train = pd.read_csv(f"{BASE}/diabetes/y_train.csv")
y_test = pd.read_csv(f"{BASE}/diabetes/y_test.csv")

# ID 컬럼 확인 (일부 데이터셋은 ID 없을 수 있음)
id_col = "ID" if "ID" in X_test.columns else X_test.columns[0]
test_ids = X_test[id_col]
X_train = X_train.drop(columns=[id_col], errors="ignore")
X_test = X_test.drop(columns=[id_col])
y_train = y_train["Outcome"]

X_train = X_train.fillna(0)
X_test = X_test.fillna(0)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
submission = pd.DataFrame({"ID": test_ids, "Outcome": pred})
submission.to_csv("submission.csv", index=False)
print("accuracy:", (pred == y_test["Outcome"].values).mean())
