# ============================================================
# 02. Churn 고객 이탈 예측
# [유형] 2유형 (40점) — 모델링(분류)
# ============================================================
#
# ---------- [시험 환경] 요구사항 ----------
# 데이터: 은행 고객 이탈 예측 (종속변수: Exited, 0/1)
# 제공: train.csv, test.csv (BASE/churn/)
# 평가: accuracy, F1, recall, precision → 예측값 제출
#
# ---------- [추출해야 할 내용 / 정답 형식] ----------
# submission.csv
#   - CustomerId (test의 ID 컬럼)
#   - Exited (0 또는 1 예측값)
# 제출 후 DataManim에서 정확도 확인 (또는 y_test와 비교)
#
# ---------- [학습 목표] ----------
# 나중에 주석 지우고 [기본 제공] + [요구사항]만 보고 연습
# ============================================================
#
# [기본 제공] Step 1~3 | [작성] Step 4~7
# ============================================================

# ---------- [기본 제공] Step 1: import ----------
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
# ---------- [기본 제공] Step 2: BASE URL ----------
BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

# ---------- [기본 제공] Step 3: train, test 로드 ----------
train = pd.read_csv(f"{BASE}/churn/train.csv")
test = pd.read_csv(f"{BASE}/churn/test.csv")

print(train)
print(test)

# ---------- [작성] Step 4: X, y 분리 ----------
# TODO: y_train = train["Exited"]
# TODO: X_train = train.drop(columns=["Exited", "CustomerId"])
# TODO: X_test = test.drop(columns=["CustomerId"])
# TODO: test_ids = test["CustomerId"]

y_train = train["Exited"]
X_train = train.drop(columns=["Exited", "CustomerId"])
X_test = test.drop(columns=["CustomerId"])
test_ids=test["CustomerId"]


# ---------- [작성] Step 5: 전처리 ----------
# TODO: 결측치 처리, 범주형 인코딩 (Geography, Gender 등)

cat_cols = X_train.select_dtypes(include = ["object"]).columns.tolist()
for col in cat_cols:
    le = LabelEncoder()  # pyright: ignore[reportUndefinedVariable]
    X_train[col] = le.fit_transform(X_train[col].astype(str))
    X_test[col] = le.transform(X_test[col].astype(str))

X_train = X_train.fillna(0)
X_test = X_test.fillna(0)

# ---------- [작성] Step 6: 모델 학습 ----------
# TODO: from sklearn.ensemble import RandomForestClassifier
# TODO: model.fit(X_train, y_train)

model = RandomForestClassifier(n_estimators = 100, random_state = 42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
submission = pd.DataFrame({"CustomerId": test_ids, "Exited": pred})
submission.to_csv("submission.csv", index = False)


# ---------- [작성] Step 7: 예측 & 제출 ----------
# TODO: pred = model.predict(X_test)
# TODO: submission = pd.DataFrame({"CustomerId": test_ids, "Exited": pred})
# TODO: submission.to_csv("submission.csv", index=False)

pred = model.predict(X_test)
submission = pd.DataFrame({"CustomerId": test_ids, "Exited": pred})
submission.to_csv("submission.csv", index = False)
print("submission.csv 저장 완료")
print(submission.head())