# ============================================================
# 15. CarsPrice 자동차 가격 (회귀)
# [유형] 2유형 (40점) — 모델링(회귀)
# ============================================================
#
# ---------- [시험 환경] 요구사항 ----------
# 데이터: 자동차 가격 회귀 예측
# 제공: X_train, X_test, y_train, y_test (BASE/carsprice/)
# 평가: RMSE 등 회귀 지표
#
# ---------- [추출해야 할 내용 / 정답 형식] ----------
# submission.csv
#   - ID (X_test의 ID)
#   - price (회귀 예측값, 연속형)
# y_test로 RMSE 확인 가능
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
X_train = pd.read_csv(f"{BASE}/carsprice/X_train.csv")
X_test = pd.read_csv(f"{BASE}/carsprice/X_test.csv")
y_train = pd.read_csv(f"{BASE}/carsprice/y_train.csv")
y_test = pd.read_csv(f"{BASE}/carsprice/y_test.csv")

# ---------- [작성] Step 4: ID 분리, X/y 정리 ----------
# TODO: ID 컬럼 확인 후 분리, y_train = y_train["price"]

# ---------- [작성] Step 5: 전처리 ----------
# TODO: 결측치, 범주형 인코딩(필요시)

# ---------- [작성] Step 6: 모델 학습 ----------
# TODO: model.fit(X_train, y_train)

# ---------- [작성] Step 7: 예측 & 제출 ----------
# TODO: pred = model.predict(X_test)
# TODO: submission.to_csv("submission.csv", index=False)
