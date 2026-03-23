# ============================================================
# 13. RedWine 와인 품질 (회귀)
# [유형] 빅분기 실기 2유형(모델링) — 숫자 맞추기·회귀 (연습: Datamanim redwine)
# ============================================================
#
# ┌─ [문제 목표] ─────────────────────────────────────────────
# │  화학·감각 지표로 **와인 품질 점수(quality)** 를 숫자로 예측한다.
# └──────────────────────────────────────────────────────────
#
# ┌─ [제공 데이터] (학습/시험 이미 분리) ─────────────────────
# │  경로: BASE/redwine/
# │  ┌─────────────┬─────────────────────────────────────────
# │  │ x_train.csv │ 학습 입력
# │  │ y_train.csv │ **quality**
# │  │ x_test.csv  │ 시험 입력
# │  │ y_test.csv  │ 연습용 정답 (RMSE 확인 등)
# │  └─────────────┴─────────────────────────────────────────
# └──────────────────────────────────────────────────────────
#
# ┌─ [수행 요구사항] ─────────────────────────────────────────
# │  ① ID 분리. ② `y_train["quality"]`. ③ **회귀(Regressor)** 로 예측.
# └──────────────────────────────────────────────────────────
#
# ┌─ [제출 산출물] ───────────────────────────────────────────
# │  **submission.csv** — **ID**, **quality** (실수 예측값)
# └──────────────────────────────────────────────────────────
#
# ┌─ [평가·연습 시 참고] ─────────────────────────────────────
# │  · RMSE 등은 문제지·채점 기준 확인.
# └──────────────────────────────────────────────────────────
#
# [학습 방법] import·BASE만 참고하고, **파일 읽기(Step 3)** 직접 작성 후 Step 4~7.
# ============================================================
#
# [기본 제공] Step 1~2 | [작성] Step 3~7
# ============================================================

# ---------- [기본 제공] Step 1: import ----------
import pandas as pd

# ---------- [기본 제공] Step 2: BASE URL ----------
BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

# ---------- [작성] Step 3: X_train, X_test, y_train, y_test 로드 ----------
# TODO: X_train = pd.read_csv(f"{BASE}/redwine/x_train.csv")
# TODO: X_test = pd.read_csv(f"{BASE}/redwine/x_test.csv")
# TODO: y_train = pd.read_csv(f"{BASE}/redwine/y_train.csv")
# TODO: y_test = pd.read_csv(f"{BASE}/redwine/y_test.csv")

# ---------- [작성] Step 4: ID 분리, X/y 정리 ----------
# TODO: ID 컬럼 확인 후 분리, y_train = y_train["quality"]

# ---------- [작성] Step 5: 전처리 ----------
# TODO: 결측치, 스케일링(필요시)

# ---------- [작성] Step 6: 모델 학습 ----------
# TODO: model = RandomForestRegressor() 또는 LinearRegression
# TODO: model.fit(X_train, y_train)

# ---------- [작성] Step 7: 예측 & 제출 ----------
# TODO: pred = model.predict(X_test)
# TODO: submission = pd.DataFrame({"ID": test_ids, "quality": pred})
# TODO: submission.to_csv("submission.csv", index=False)
