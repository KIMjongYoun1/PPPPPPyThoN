# ============================================================
# 03. MedicalCost 의료비 예측
# [유형] 2유형 (40점) — 모델링(회귀)
# ============================================================
#
# ---------- [시험 환경] 요구사항 ----------
# 데이터: 의료비(charges) 회귀 예측
# 제공: train.csv, test.csv (BASE/MedicalCost/)
# 평가: RMSE 등 회귀 지표
#
# ---------- [추출해야 할 내용 / 정답 형식] ----------
# submission.csv
#   - ID (datarepo 기준 CSV에 ID 컬럼 없음 → 행 순서용으로 0,1,2,... 인덱스 사용)
#   - charges (회귀 예측값, 연속형)
#   실제 시험에 test에 ID 컬럼이 있으면 문제 지시대로 그 컬럼 사용.
# 제출 후 DataManim에서 RMSE 확인 (또는 y_test와 비교)
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

# ---------- [기본 제공] Step 3: train, test 로드 ----------
train = pd.read_csv(f"{BASE}/MedicalCost/train.csv")
test = pd.read_csv(f"{BASE}/MedicalCost/test.csv")

# ---------- [작성] Step 4: X, y 분리 ----------
# TODO: y_train = train["charges"]
# TODO: X_train = train.drop(columns=["charges"])
# TODO: X_test = test.copy()   # test는 전부 특성 (ID 컬럼 없음)
# TODO: test_ids = test.index  # 제출용 ID (0,1,2,...). 시험에 ID 컬럼 있으면 test["ID"]



# ---------- [작성] Step 5: 전처리 ----------
# TODO: 결측치, 범주형 인코딩 (sex, smoker, region)

# ---------- [작성] Step 6: 모델 학습 ----------
# TODO: from sklearn.ensemble import RandomForestRegressor  # 또는 LinearRegression
# TODO: model.fit(X_train, y_train)

# ---------- [작성] Step 7: 예측 & 제출 ----------
# TODO: pred = model.predict(X_test)
# TODO: submission = pd.DataFrame({"ID": test_ids, "charges": pred})
# TODO: submission.to_csv("submission.csv", index=False)
