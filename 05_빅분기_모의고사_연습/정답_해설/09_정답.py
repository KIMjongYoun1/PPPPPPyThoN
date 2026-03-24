# ============================================================
# 09. Cancer 유방암 (정답)
# ============================================================
# datarepo의 y_train/y_test는 열 이름이 diagnosis (M/B). 모델은 숫자 라벨 필요.

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

X_train = pd.read_csv(f"{BASE}/cancer/x_train.csv")
X_test = pd.read_csv(f"{BASE}/cancer/x_test.csv")
y_train = pd.read_csv(f"{BASE}/cancer/y_train.csv")
y_test = pd.read_csv(f"{BASE}/cancer/y_test.csv")

id_col = "ID" if "ID" in X_test.columns else X_test.columns[0]
test_ids = X_test[id_col]
X_train = X_train.drop(columns=[id_col], errors="ignore")
X_test = X_test.drop(columns=[id_col])

y_le = LabelEncoder()
y_train = y_le.fit_transform(y_train["diagnosis"])

X_train = X_train.fillna(0)
X_test = X_test.fillna(0)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
submission = pd.DataFrame({"ID": test_ids, "target": pred})
submission.to_csv("submission.csv", index=False)

y_test_enc = y_le.transform(y_test["diagnosis"])
print("accuracy:", (pred == y_test_enc).mean())
