# ============================================================
# 11. Titanic 타이타닉 (정답)
# ============================================================

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

train = pd.read_csv(f"{BASE}/titanic/train.csv")

X = train.drop(columns=["Survived"])
y = train["Survived"]

# 범주형 인코딩
cat_cols = X.select_dtypes(include=["object"]).columns.tolist()
for col in cat_cols:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))

X = X.fillna(0)

X_tr, X_val, y_tr, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_tr, y_tr)

pred = model.predict(X_val)
print("accuracy:", (pred == y_val.values).mean())

# submission (train 전체로 재학습 후 test 예측 — test 없으면 검증용)
model_full = RandomForestClassifier(n_estimators=100, random_state=42)
model_full.fit(X, y)
# test.csv 있으면 로드 후 예측
