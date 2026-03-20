# ============================================================
# 21. Drug 약물 분류 (정답) — 다중분류
# ============================================================

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

X_train = pd.read_csv(f"{BASE}/drug/x_train.csv")
X_test = pd.read_csv(f"{BASE}/drug/x_test.csv")
y_train = pd.read_csv(f"{BASE}/drug/y_train.csv")
y_test = pd.read_csv(f"{BASE}/drug/y_test.csv")

id_col = "ID" if "ID" in X_test.columns else X_test.columns[0]
test_ids = X_test[id_col]
X_train = X_train.drop(columns=[id_col], errors="ignore")
X_test = X_test.drop(columns=[id_col])
y_train = y_train["Drug"]

cat_cols = X_train.select_dtypes(include=["object"]).columns.tolist()
for col in cat_cols:
    le = LabelEncoder()
    X_train[col] = le.fit_transform(X_train[col].astype(str))
    X_test[col] = le.transform(X_test[col].astype(str))

# y도 LabelEncoder (다중분류)
le_y = LabelEncoder()
y_train_enc = le_y.fit_transform(y_train)

X_train = X_train.fillna(0)
X_test = X_test.fillna(0)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train_enc)

pred_enc = model.predict(X_test)
pred = le_y.inverse_transform(pred_enc)
submission = pd.DataFrame({"ID": test_ids, "Drug": pred})
submission.to_csv("submission.csv", index=False)
print("accuracy:", (pred == y_test["Drug"].values).mean())
