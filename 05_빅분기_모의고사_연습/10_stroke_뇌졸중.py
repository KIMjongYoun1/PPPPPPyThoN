# ============================================================
# 10. Stroke 뇌졸중 (분류)
# [유형] 2유형 (40점) — 모델링(분류)
# ============================================================
#
# ---------- [시험 환경] 요구사항 ----------
# 데이터: 뇌졸중 발생 여부 (종속변수: stroke)
# 제공: train.csv, test.csv (BASE/stroke_/)
# 평가: accuracy/F1/recall/precision → 예측값 / AUC → predict_proba[:,1]
#
# ---------- [추출해야 할 내용 / 정답 형식] ----------
# submission.csv
#   - ID (test의 ID)
#   - stroke (0 또는 1 예측값, 또는 확률)
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

# ---------- [기본 제공] Step 3: train, test 로드 ----------
train = pd.read_csv(f"{BASE}/stroke_/train.csv")
test = pd.read_csv(f"{BASE}/stroke_/test.csv")

# ---------- [작성] Step 4: X, y 분리 ----------
# TODO: y_train = train["stroke"]
# TODO: X_train = train.drop(columns=["stroke", "ID"])
# TODO: X_test, test_ids 분리

# ---------- [작성] Step 5: 전처리 ----------
# TODO: 결측치, 범주형 인코딩 (gender, ever_married, work_type 등)

# ---------- [작성] Step 6: 모델 학습 ----------
# TODO: model.fit(X_train, y_train)

# ---------- [작성] Step 7: 예측 & 제출 ----------
# TODO: pred = model.predict(X_test)
# TODO: submission = pd.DataFrame({"ID": test_ids, "stroke": pred})
# TODO: submission.to_csv("submission.csv", index=False)
