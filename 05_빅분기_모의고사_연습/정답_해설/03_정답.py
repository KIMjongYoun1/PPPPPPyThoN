# ============================================================
# 03. MedicalCost 의료비 예측 (정답)
# ============================================================
# 참고: datarepo MedicalCost — train/test CSV에 ID 컬럼 없음
#       (train: age,sex,...,charges / test: age,sex,...,region)
#       제출용 ID는 행 순서와 맞추기 위해 보통 pandas 인덱스(0,1,2,...) 사용.
#       실제 시험에 ID 컬럼이 있으면 test["ID"] 등 문제 지시대로 사용.

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

# Step 3: 데이터 로드
train = pd.read_csv(f"{BASE}/MedicalCost/train.csv")
test = pd.read_csv(f"{BASE}/MedicalCost/test.csv")

# Step 4: X, y 분리 (ID 컬럼 없음 → charges만 타깃에서 제외)
y_train = train["charges"]
X_train = train.drop(columns=["charges"])
X_test = test.copy()
# 제출 ID: CSV에 없으면 행 순서 = 인덱스 (채점 y_test와 같은 순서 가정)
test_ids = X_test.index

# Step 5: 전처리 — 범주형 인코딩 (sex, smoker, region)
cat_cols = ["sex", "smoker", "region"]
for col in cat_cols:
    le = LabelEncoder()
    X_train[col] = le.fit_transform(X_train[col].astype(str))
    X_test[col] = le.transform(X_test[col].astype(str))

X_train = X_train.fillna(0)
X_test = X_test.fillna(0)

# Step 6: 모델 학습
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 7: 예측 & 제출
pred = model.predict(X_test)
submission = pd.DataFrame({"ID": test_ids, "charges": pred})
submission.to_csv("submission.csv", index=False)
print("submission.csv 저장 완료")
print(submission.head())
