# ============================================================
# 07. Diabetes 당뇨병 (분류)
# [유형] 빅분기 실기 2유형(모델링) — 갈래 맞추기 (연습: Datamanim diabetes)
# ============================================================
#
# ┌─ [문제 목표] ─────────────────────────────────────────────
# │  검사 수치 등으로 **당뇨 여부(Outcome)** 를 맞춘다 (보통 0/1).
# └──────────────────────────────────────────────────────────
#
# ┌─ [제공 데이터] (학습/시험 이미 분리) ─────────────────────
# │  경로: BASE/diabetes/ (파일명 소문자 x_train 등)
# │  ┌─────────────┬─────────────────────────────────────────
# │  │ x_train.csv │ 학습 입력 (+ **ID** 또는 첫 열이 번호일 수 있음 — `columns` 확인)
# │  │ y_train.csv │ 학습 정답 (**Outcome**)
# │  │ x_test.csv  │ 시험 입력
# │  │ y_test.csv  │ 연습용 정답 (채점 아님일 수 있음)
# │  └─────────────┴─────────────────────────────────────────
# └──────────────────────────────────────────────────────────
#
# ┌─ [수행 요구사항] ─────────────────────────────────────────
# │  ① ID 열(또는 번호 열)은 **빼서** test_ids 로 보관, 모델 입력 X에는 넣지 않음.
# │  ② `y_train = y_train["Outcome"]`. 결측·필요 시 스케일링 후 **분류** 모델.
# └──────────────────────────────────────────────────────────
#
# ┌─ [제출 산출물] ───────────────────────────────────────────
# │  **submission.csv** — **ID**(또는 문제 지정 열), **Outcome** (0/1 또는 확률)
# └──────────────────────────────────────────────────────────
#
# ┌─ [평가·연습 시 참고] ─────────────────────────────────────
# │  · y_test로 accuracy 등 확인 가능.
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
# TODO: X_train = pd.read_csv(f"{BASE}/diabetes/x_train.csv")
# TODO: X_test = pd.read_csv(f"{BASE}/diabetes/x_test.csv")
# TODO: y_train = pd.read_csv(f"{BASE}/diabetes/y_train.csv")
# TODO: y_test = pd.read_csv(f"{BASE}/diabetes/y_test.csv")

X_train = pd.read_csv(f"{BASE}/diabetes/x_train.csv")
X_test = pd.read_csv(f"{BASE}/diabetes/x_test.csv")
y_train = pd.read_csv(f"{BASE}/diabetes/y_train.csv")
y_test = pd.read_csv(f"{BASE}/diabetes/y_test.csv")

id_col = "ID" if "ID" in X_test.columns else X_test.columns[0]
test_ids = X_test[id_col]
X_train = X_train.drop(columns=[id_col], errors="ignore")
X_test = X_test.drop(columns=[id_col])
y_train = y_train["Outcome"]

# ---------- [작성] Step 4: ID 분리, X/y 정리 ----------
# (위에서 처리됨) x_train에는 Outcome 없음 — y는 y_train.csv만 사용

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
# TODO: pred = model.predict(X_test)  # 또는 predict_proba[:,1]
# TODO: submission.to_csv("submission.csv", index=False)

pred = model.predict(X_test)
submission = pd.DataFrame({"ID": test_ids, "Outcome": pred})
submission.to_csv("submission.csv", index=False)
print("submission.csv 저장 완료")
print(submission.head())
print("accuracy:", (pred == y_test["Outcome"].values).mean())
