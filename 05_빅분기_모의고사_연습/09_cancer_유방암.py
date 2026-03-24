# ============================================================
# 09. Cancer 유방암 (분류)
# [유형] 빅분기 실기 2유형(모델링) — 갈래 맞추기 (연습: Datamanim cancer)
# ============================================================
#
# ┌─ [문제 목표] ─────────────────────────────────────────────
# │  종양 특성 수치로 **양성/악성**을 맞춘다. y 파일 열 이름: **diagnosis** (값 M/B).
# │  제출 CSV 컬럼명은 문제에서 **target** 으로 요구하는 경우가 많음 → 아래 submission 참고.
# └──────────────────────────────────────────────────────────
#
# ┌─ [제공 데이터] (학습/시험 이미 분리) ─────────────────────
# │  경로: BASE/cancer/
# │  ┌─────────────┬─────────────────────────────────────────
# │  │ x_train.csv │ 학습 입력 (수치 + ID, 소문자 id 열 있을 수 있음)
# │  │ y_train.csv │ **ID**, **diagnosis** (M=악성, B=양성 등 — 문자열)
# │  │ x_test.csv  │ 시험 입력
# │  │ y_test.csv  │ 연습용 정답 (동일 구조)
# │  └─────────────┴─────────────────────────────────────────
# └──────────────────────────────────────────────────────────
#
# ┌─ [수행 요구사항] ─────────────────────────────────────────
# │  ① ID 분리. ② 정답은 `y_train["diagnosis"]` → 모델용으로 **숫자 인코딩**(LabelEncoder).
# │  ③ **분류** 모델.
# └──────────────────────────────────────────────────────────
#
# ┌─ [제출 산출물] ───────────────────────────────────────────
# │  **submission.csv** — **ID**, **target** (예측 클래스; 0/1 등 인코딩된 값)
# └──────────────────────────────────────────────────────────
#
# ┌─ [평가·연습 시 참고] ─────────────────────────────────────
# │  · y_test["diagnosis"] 를 같은 방식으로 인코딩 후 accuracy 비교.
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

# ---------- [작성] Step 3: X_train, X_test, y_train, y_test 로드 ----------
# TODO: X_train = pd.read_csv(f"{BASE}/cancer/x_train.csv")
# TODO: X_test = pd.read_csv(f"{BASE}/cancer/x_test.csv")
# TODO: y_train = pd.read_csv(f"{BASE}/cancer/y_train.csv")
# TODO: y_test = pd.read_csv(f"{BASE}/cancer/y_test.csv")

X_train = pd.read_csv(f"{BASE}/cancer/x_train.csv")
X_test = pd.read_csv(f"{BASE}/cancer/x_test.csv")
y_train = pd.read_csv(f"{BASE}/cancer/y_train.csv")
y_test = pd.read_csv(f"{BASE}/cancer/y_test.csv")

# ---------- [작성] Step 4: ID 분리, X/y 정리 ----------
# TODO: ID 컬럼 확인 후 분리, y는 diagnosis (문자 M/B → 숫자로 인코딩)

id_col = "ID" if "ID" in X_test.columns else X_test.columns[0]
test_ids = X_test[id_col]
X_train = X_train.drop(columns=[id_col], errors="ignore")
X_test = X_test.drop(columns=[id_col])

# datarepo cancer: 정답 열 이름은 diagnosis (target 열 없음)
y_le = LabelEncoder()
y_train = y_le.fit_transform(y_train["diagnosis"])

# ---------- [작성] Step 5: 전처리 ----------
# TODO: 결측치, 스케일링(필요시)

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
# TODO: submission.to_csv("submission.csv", index=False)

pred = model.predict(X_test)
submission = pd.DataFrame({"ID": test_ids, "target": pred})
submission.to_csv("submission.csv", index=False)

print("submission.csv 저장 완료")
print(submission.head())
y_test_enc = y_le.transform(y_test["diagnosis"])
print("accuracy:", (pred == y_test_enc).mean())
