# ============================================================
# 11. Titanic 타이타닉 (분류)
# [유형] 2유형 (40점) — 모델링(분류)
# ============================================================
#
# ---------- [시험 환경] 요구사항 ----------
# 데이터: 타이타닉 생존 여부 (종속변수: Survived)
# 제공: train.csv만 (BASE/titanic/) — test 없음 → train_test_split으로 검증
# 평가: accuracy/F1/recall/precision → 예측값
#
# ---------- [추출해야 할 내용 / 정답 형식] ----------
# submission.csv
#   - PassengerId (test 또는 검증용 ID)
#   - Survived (0 또는 1 예측값)
# train_test_split으로 검증용 분할 후 학습·예측
#
# ---------- [학습 목표] ----------
# 나중에 주석 지우고 [기본 제공] + [요구사항]만 보고 연습
# ============================================================
#
# [기본 제공] Step 1~3 | [작성] Step 4~7
# ============================================================

# ---------- [기본 제공] Step 1: import ----------
import pandas as pd
from sklearn.model_selection import train_test_split

# ---------- [기본 제공] Step 2: BASE URL ----------
BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

# ---------- [기본 제공] Step 3: train 로드 ----------
train = pd.read_csv(f"{BASE}/titanic/train.csv")

# ---------- [작성] Step 4: X, y 분리 & train_test_split ----------
# TODO: X = train.drop(columns=["Survived"])
# TODO: y = train["Survived"]
# TODO: X_tr, X_val, y_tr, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# ---------- [작성] Step 5: 전처리 ----------
# TODO: 결측치, 범주형 인코딩 (Sex, Embarked 등)

# ---------- [작성] Step 6: 모델 학습 ----------
# TODO: model.fit(X_tr, y_tr)

# ---------- [작성] Step 7: 예측 & 제출 ----------
# TODO: pred = model.predict(X_val)
# TODO: submission 형식에 맞게 저장 (또는 train 전체로 학습 후 test 예측)
