# ============================================================
# 21. Drug 약물 분류 (다중분류)
# [유형] 2유형 (40점) — 모델링(분류)
# ============================================================
#
# ---------- [시험 환경] 요구사항 ----------
# 데이터: 약물 유형 다중분류 (DrugY 등)
# 제공: x_train, x_test, y_train, y_test (BASE/drug/)
# 평가: 다중분류 accuracy 등
#
# ---------- [추출해야 할 내용 / 정답 형식] ----------
# submission.csv
#   - ID (x_test의 ID)
#   - Drug (다중분류 예측값, 범주형)
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

# ---------- [기본 제공] Step 3: x_train, x_test, y_train, y_test 로드 ----------
X_train = pd.read_csv(f"{BASE}/drug/x_train.csv")
X_test = pd.read_csv(f"{BASE}/drug/x_test.csv")
y_train = pd.read_csv(f"{BASE}/drug/y_train.csv")
y_test = pd.read_csv(f"{BASE}/drug/y_test.csv")

# ---------- [작성] Step 4: ID 분리, X/y 정리 ----------
# TODO: ID 컬럼 확인, y_train = y_train["Drug"]

# ---------- [작성] Step 5: 전처리 ----------
# TODO: 결측치, 범주형 인코딩 (다중분류 → LabelEncoder)

# ---------- [작성] Step 6: 모델 학습 ----------
# TODO: model.fit(X_train, y_train)  # 다중분류

# ---------- [작성] Step 7: 예측 & 제출 ----------
# TODO: pred = model.predict(X_test)
# TODO: submission = pd.DataFrame({"ID": test_ids, "Drug": pred})
# TODO: submission.to_csv("submission.csv", index=False)
