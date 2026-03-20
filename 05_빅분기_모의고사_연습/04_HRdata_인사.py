# ============================================================
# 04. HRdata 이직 예측
# [유형] 2유형 (40점) — 모델링(분류)
# ============================================================
#
# ---------- [시험 환경] 요구사항 ----------
# 데이터: 이직여부 (target: 1=이직, 0=이직x)
# 제공: X_train, X_test, y_train, y_test (BASE/HRdata/) — 이미 분리됨
# 평가: accuracy/F1/recall/precision → 예측값 / AUC → predict_proba[:,1]
#
# ---------- [추출해야 할 내용 / 정답 형식] ----------
# submission.csv
#   - enrollee_id (X_test의 ID)
#   - target (0 또는 1 예측값, 또는 확률)
# y_test로 정확도 확인 가능
#
# ---------- [학습 목표] ----------
# 나중에 주석 지우고 [기본 제공] + [요구사항]만 보고 연습
# ============================================================
#
# [기본 제공] Step 1~3 | [작성] Step 4~7
# ============================================================

# ---------- [기본 제공] Step 1: import ----------
import pandas as pd

# ---------- [기본 제공] Step 2: BASE URL ----------
BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

# ---------- [기본 제공] Step 3: X_train, X_test, y_train, y_test 로드 ----------
X_train = pd.read_csv(f"{BASE}/HRdata/X_train.csv")
X_test = pd.read_csv(f"{BASE}/HRdata/X_test.csv")
y_train = pd.read_csv(f"{BASE}/HRdata/y_train.csv")
y_test = pd.read_csv(f"{BASE}/HRdata/y_test.csv")

# ---------- [작성] Step 4: ID 분리, X/y 정리 ----------
# TODO: enrollee_id = X_test["enrollee_id"]
# TODO: X_train = X_train.drop(columns=["enrollee_id"])
# TODO: X_test = X_test.drop(columns=["enrollee_id"])
# TODO: y_train = y_train["target"]

# ---------- [작성] Step 5: 전처리 ----------
# TODO: 결측치, 범주형 인코딩 (city, gender 등)

# ---------- [작성] Step 6: 모델 학습 ----------
# TODO: model.fit(X_train, y_train)

# ---------- [작성] Step 7: 예측 & 제출 ----------
# TODO: pred = model.predict(X_test)  # 또는 predict_proba[:,1]
# TODO: submission = pd.DataFrame({"enrollee_id": enrollee_id, "target": pred})
# TODO: submission.to_csv("submission.csv", index=False)
