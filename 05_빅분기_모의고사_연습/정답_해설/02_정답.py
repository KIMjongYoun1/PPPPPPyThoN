# ============================================================
# 02. Churn 고객 이탈 예측 (정답)
# ============================================================

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

# Step 3: 데이터 로드
train = pd.read_csv(f"{BASE}/churn/train.csv")
test = pd.read_csv(f"{BASE}/churn/test.csv")

# Step 4: X, y 분리
y_train = train["Exited"]
X_train = train.drop(columns=["Exited", "CustomerId"])
X_test = test.drop(columns=["CustomerId"])
test_ids = test["CustomerId"]

# Step 5: 전처리 — 범주형 인코딩
cat_cols = ["Geography", "Gender"]
le_dict = {}
for col in cat_cols:
    le = LabelEncoder()
    X_train[col] = le.fit_transform(X_train[col].astype(str))
    X_test[col] = le.transform(X_test[col].astype(str))

# 결측치 (필요시)
X_train = X_train.fillna(0)
X_test = X_test.fillna(0)

# Step 6: 모델 학습
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 7: 예측 & 제출
pred = model.predict(X_test)
submission = pd.DataFrame({"CustomerId": test_ids, "Exited": pred})
submission.to_csv("submission.csv", index=False)
print("submission.csv 저장 완료")
print(submission.head())
