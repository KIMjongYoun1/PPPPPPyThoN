# ============================================================
# 03. MedicalCost 의료비 예측
# [유형] 빅분기 실기 2유형(모델링) — 숫자 맞추기·회귀 (연습: Datamanim MedicalCost)
# ============================================================
#
# ┌─ [문제 목표] ─────────────────────────────────────────────
# │  보험·건강 특성을 보고 **의료비 charges** (연속 숫자)를 예측한다.
# └──────────────────────────────────────────────────────────
#
# ┌─ [제공 데이터] ───────────────────────────────────────────
# │  경로: BASE/MedicalCost/
# │  ┌────────────┬──────────────────────────────────────────
# │  │ 파일       │ 역할
# │  ├────────────┼──────────────────────────────────────────
# │  │ train.csv  │ 학습용 — 특성 + **charges**(정답)
# │  │ test.csv   │ 시험용 — 특성만 (datarepo 기준 **ID 열 없음**)
# │  └────────────┴──────────────────────────────────────────
# └──────────────────────────────────────────────────────────
#
# ┌─ [수행 요구사항] ─────────────────────────────────────────
# │  ① **charges** 는 정답(y) → X_train 에서만 제거, test에는 원래 없음.
# │  ② 글자 열(sex, smoker, region 등)은 숫자로 인코딩. 빈 칸 처리.
# │  ③ **회귀** 모델(Regressor)로 학습·예측.
# └──────────────────────────────────────────────────────────
#
# ┌─ [제출 산출물] ───────────────────────────────────────────
# │  파일명: **submission.csv** (`index=False`)
# │  열 1: **ID** — CSV에 ID가 없으면 `test.index`(0,1,2,…) 사용. 문제에 ID 열 있으면 그 열.
# │  열 2: **charges** — 예측된 의료비(실수)
# └──────────────────────────────────────────────────────────
#
# ┌─ [평가·연습 시 참고] ─────────────────────────────────────
# │  · 채점은 보통 **RMSE** 등 (문제지 확인).
# │  · 제출 양식에서 ID가 1부터라고 하면 `range(1, len(test)+1)` 등으로 맞출 것.
# └──────────────────────────────────────────────────────────
#
# [학습 방법] import·BASE만 참고하고, **파일 읽기(Step 3)** 부터 이어서 작성.
# ============================================================
#
# [기본 제공] Step 1~2 | [작성] Step 3~7
# ============================================================

# ---------- [기본 제공] Step 1: import ----------
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# ---------- [기본 제공] Step 2: BASE URL ----------
BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

# ---------- [작성] Step 3: train, test 로드 ----------
# TODO: train = pd.read_csv(f"{BASE}/MedicalCost/train.csv")
# TODO: test = pd.read_csv(f"{BASE}/MedicalCost/test.csv")

# ---------- [작성] Step 4: X, y 분리 ----------
# TODO: y_train = train["charges"]
# TODO: X_train = train.drop(columns=["charges"])
# TODO: X_test = test.copy()   # test는 전부 특성 (ID 컬럼 없음)
# TODO: test_ids = test.index  # 제출용 ID (0,1,2,...). 시험에 ID 컬럼 있으면 test["ID"]

y_train = train["charges"]
X_train = train.drop(columns=["charges"])
X_test = test.copy()
test_ids = test.index  # 제출용 ID (0,1,2,...). test에 ID 컬럼 있으면 test["ID"]

# ---------- [작성] Step 5: 전처리 ----------
# TODO: 결측치, 범주형 인코딩 (sex, smoker, region)

cat_cols = ["sex", "smoker", "region"]
for col in cat_cols:
    le = LabelEncoder()
    X_train[col] = le.fit_transform(X_train[col].astype(str))
    X_test[col] = le.transform(X_test[col].astype(str))

X_train = X_train.fillna(0)
X_test = X_test.fillna(0)

# ---------- [작성] Step 6: 모델 학습 ----------
# TODO: RandomForestRegressor 또는 LinearRegression
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
# ---------- [작성] Step 7: 예측 & 제출 ----------
# TODO: pred = model.predict(X_test)
# TODO: submission = pd.DataFrame({"ID": test_ids, "charges": pred})
# TODO: submission.to_csv("submission.csv", index=False)

pred = model.predict(X_test)
submission = pd.DataFrame({"ID": test_ids, "charges": pred})
submission.to_csv("submission.csv", index=False)
print("submission.csv 저장 완료")
print(submission.head())