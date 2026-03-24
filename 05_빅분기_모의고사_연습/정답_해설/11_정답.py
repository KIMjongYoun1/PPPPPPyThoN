# ============================================================
# 11. Titanic 타이타닉 (정답)
# — 연습 파일 11_titanic_타이타닉.py 에서 # AI 보완 반영한 실행 코드만 (ME/AI 주석 없음)
# ============================================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

train = pd.read_csv(f"{BASE}/titanic/train.csv")
print(train.head())
print("train.shape:", train.shape)

X = train.drop(columns=["Survived"])
y = train["Survived"]

cat_col = X.select_dtypes(include=["object"]).columns.tolist()
for col in cat_col:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))

X = X.fillna(0)

X_tr, X_val, y_tr, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print("분할 후:", X_tr.shape, X_val.shape, y_tr.shape, y_val.shape)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_tr, y_tr)

pred = model.predict(X_val)
print("accuracy (검증):", (pred == y_val.values).mean())

submission = pd.DataFrame({"PassengerId": X_val["PassengerId"], "Survived": pred})
submission.to_csv("submission.csv", index=False)
print("submission.csv 저장 완료")
print(submission.head())
