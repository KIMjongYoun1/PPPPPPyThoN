# ============================================================
# 02. Churn 고객 이탈 예측
# [유형] 빅분기 실기 2유형(모델링) — 갈래 맞추기·분류 (연습: Datamanim churn)
# ============================================================
#
# ┌─ [문제 목표] ─────────────────────────────────────────────
# │  고객 정보를 보고 **이탈 여부**를 맞춘다.
# │  정답 열: **Exited** → **1 = 이탈**, **0 = 이탈 안 함** (문제지·데이터 기준)
# └──────────────────────────────────────────────────────────
#
# ┌─ [제공 데이터] ───────────────────────────────────────────
# │  경로: BASE/churn/
# │  ┌────────────┬──────────────────────────────────────────
# │  │ 파일       │ 역할
# │  ├────────────┼──────────────────────────────────────────
# │  │ train.csv  │ 학습용 — 특성 + **Exited** + **CustomerId**
# │  │ test.csv   │ 시험용 — 특성 + **CustomerId** (정답 열 없음)
# │  └────────────┴──────────────────────────────────────────
# └──────────────────────────────────────────────────────────
#
# ┌─ [수행 요구사항] ─────────────────────────────────────────
# │  ① **CustomerId** 는 사람 번호 → 예측 입력(X)에서 빼고 제출용으로만 둔다.
# │  ② **Exited** 는 정답 → y_train 만든 뒤, X_train/X_test 에서는 제거한다.
# │  ③ 글자(object) 열은 숫자로 바꾼다. 빈 칸은 채운다.
# │  ④ **분류** 모델로 학습·예측한다. (AUC·확률 제출 시 `predict_proba[:,1]`)
# └──────────────────────────────────────────────────────────
#
# ┌─ [제출 산출물] ───────────────────────────────────────────
# │  파일명: **submission.csv** (`index=False`)
# │  열 1: **CustomerId** (test와 같은 순서)
# │  열 2: **Exited** — 0/1 예측 또는 문제가 요구하면 0~1 확률
# └──────────────────────────────────────────────────────────
#
# ┌─ [평가·연습 시 참고] ─────────────────────────────────────
# │  · 채점 지표는 **문제지** (accuracy, F1, AUC 등).
# │  · y_test가 있으면 로컬에서 맞는지 비교 가능.
# └──────────────────────────────────────────────────────────
#
# [학습 방법] import·BASE만 참고하고, **파일 읽기(Step 3)** 부터 이어서 작성.
# ============================================================
#
# [기본 제공] Step 1~2 | [작성] Step 3~7
# ============================================================

# ---------- [기본 제공] Step 1: import ----------
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
# ---------- [기본 제공] Step 2: BASE URL ----------
BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

# ---------- [작성] Step 3: train, test 로드 ----------
# TODO: train = pd.read_csv(f"{BASE}/churn/train.csv")
# TODO: test = pd.read_csv(f"{BASE}/churn/test.csv")

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