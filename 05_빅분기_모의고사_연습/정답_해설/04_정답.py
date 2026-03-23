# ============================================================
# 04. HRdata 이직 예측 (정답)
# ============================================================

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

# Step 3: 데이터 로드
X_train = pd.read_csv(f"{BASE}/HRdata/X_train.csv")
X_test = pd.read_csv(f"{BASE}/HRdata/X_test.csv")
y_train = pd.read_csv(f"{BASE}/HRdata/y_train.csv")
y_test = pd.read_csv(f"{BASE}/HRdata/y_test.csv")

# Step 4: ID 분리, X/y 정리
enrollee_id = X_test["enrollee_id"]
X_train = X_train.drop(columns=["enrollee_id"])
X_test = X_test.drop(columns=["enrollee_id"])
y_train = y_train["target"]

# Step 5: 전처리 — 범주형 인코딩, 결측치
cat_cols = X_train.select_dtypes(include=["object"]).columns.tolist()
for col in cat_cols:
    le = LabelEncoder()
    # test에만 등장하는 범주 대비: train+test 합쳐서 fit
    both = pd.concat([X_train[col], X_test[col]], axis=0).astype(str)
    le.fit(both)
    X_train[col] = le.transform(X_train[col].astype(str))
    X_test[col] = le.transform(X_test[col].astype(str))

X_train = X_train.fillna(0)
X_test = X_test.fillna(0)

# Step 6: 모델 학습
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 7: 예측 & 제출
pred = model.predict(X_test)
submission = pd.DataFrame({"enrollee_id": enrollee_id, "target": pred})
submission.to_csv("submission.csv", index=False)
print("submission.csv 저장 완료")
print("accuracy:", (pred == y_test["target"].values).mean())
