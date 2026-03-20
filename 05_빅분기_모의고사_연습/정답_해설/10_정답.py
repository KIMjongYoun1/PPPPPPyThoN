# ============================================================
# 10. Stroke 뇌졸중 (정답)
# ============================================================

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

train = pd.read_csv(f"{BASE}/stroke_/train.csv")
test = pd.read_csv(f"{BASE}/stroke_/test.csv")

y_train = train["stroke"]
X_train = train.drop(columns=["stroke", "id"])
X_test = test.drop(columns=["id"])
test_ids = test["id"]

cat_cols = X_train.select_dtypes(include=["object"]).columns.tolist()
for col in cat_cols:
    le = LabelEncoder()
    X_train[col] = le.fit_transform(X_train[col].astype(str))
    X_test[col] = le.transform(X_test[col].astype(str))

X_train = X_train.fillna(0)
X_test = X_test.fillna(0)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
submission = pd.DataFrame({"id": test_ids, "stroke": pred})
submission.to_csv("submission.csv", index=False)
print("submission.csv 저장 완료")
