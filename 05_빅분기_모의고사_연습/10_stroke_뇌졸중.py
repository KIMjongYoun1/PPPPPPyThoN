# ============================================================
# 10. Stroke 뇌졸중 (분류)
# [유형] 빅분기 실기 2유형(모델링) — 갈래 맞추기 (연습: Datamanim stroke_)
# ============================================================
#
# ┌─ [문제 목표] ─────────────────────────────────────────────
# │  환자 정보로 **뇌졸중 발생 여부(stroke)** 를 맞춘다 (0/1).
# └──────────────────────────────────────────────────────────
#
# ┌─ [제공 데이터] ───────────────────────────────────────────
# │  경로: BASE/stroke_/  (폴더 이름에 밑줄 주의)
# │  ┌────────────┬──────────────────────────────────────────
# │  │ train.csv  │ 특성 + **stroke** + **id** (소문자 열 이름)
# │  │ test.csv   │ 특성 + **id**
# │  └────────────┴──────────────────────────────────────────
# └──────────────────────────────────────────────────────────
#
# ┌─ [수행 요구사항] ─────────────────────────────────────────
# │  ① ID 분리. ② stroke 는 y만. ③ gender, work_type 등 글자 열 인코딩. ④ 분류 모델.
# └──────────────────────────────────────────────────────────
#
# ┌─ [제출 산출물] ───────────────────────────────────────────
# │  **submission.csv** — **id**, **stroke** (DataManim 예시는 소문자 id)
# └──────────────────────────────────────────────────────────
#
# ┌─ [평가·연습 시 참고] ─────────────────────────────────────
# │  · 문제지에 따른 지표·확률 제출.
# └──────────────────────────────────────────────────────────
#
# [학습 방법] import·BASE만 참고하고, **파일 읽기(Step 3)** 직접 작성 후 Step 4~7.
# ============================================================
#
# [기본 제공] Step 1~2 | [작성] Step 3~7
# ============================================================

# ---------- [기본 제공] Step 1: import ----------
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# ---------- [기본 제공] Step 2: BASE URL ----------
BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

# ---------- [작성] Step 3: train, test 로드 ----------
# TODO: train = pd.read_csv(f"{BASE}/stroke_/train.csv")
# TODO: test = pd.read_csv(f"{BASE}/stroke_/test.csv")

train = pd.read_csv(f"{BASE}/stroke_/train.csv")
test = pd.read_csv(f"{BASE}/stroke_/test.csv")

# ---------- [작성] Step 4: X, y 분리 ----------
# TODO: y_train = train["stroke"]
# TODO: X_train = train.drop(columns=["stroke", "id"])
# TODO: X_test, test_ids 분리

y_train = train["stroke"]
X_train = train.drop(columns=["stroke", "id"])
X_test = test.drop(columns=["id"])
test_ids = test["id"]

# ---------- [작성] Step 5: 전처리 ----------
# TODO: 결측치, 범주형 인코딩 (gender, ever_married, work_type 등)

cat_col = X_train.select_dtypes(include=["object"]).columns.tolist()
for col in cat_col:
    le = LabelEncoder()
    X_train[col] = le.fit_transform(X_train[col].astype(str))
    X_test[col] = le.transform(X_test[col].astype(str))

X_train = X_train.fillna(0)
X_test = X_test.fillna(0)

# ---------- [작성] Step 6: 모델 학습 ----------
# TODO: model.fit(X_train, y_train)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ---------- [작성] Step 7: 예측 & 제출 ----------
# TODO: pred = model.predict(X_test)
# TODO: submission = pd.DataFrame({"id": test_ids, "stroke": pred})
# TODO: submission.to_csv("submission.csv", index=False)

pred = model.predict(X_test)
submission = pd.DataFrame({"id": test_ids, "stroke": pred})
submission.to_csv("submission.csv", index=False)
print("submission.csv 저장 완료")
print(submission.head())
# pred 는 test 행 개수, y_train 은 train 행 개수 → 서로 비교하면 안 됨.
# stroke_ 공개 데이터에는 y_test.csv 없음 → accuracy 는 별도 라벨 없으면 생략.