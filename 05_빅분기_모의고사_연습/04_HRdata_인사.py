# ============================================================
# 04. HRdata 이직 예측
# [유형] 빅분기 실기 2유형(모델링) — 분류 문제 (연습: Datamanim HRdata)
# ============================================================
#
# ┌─ [문제 목표] ─────────────────────────────────────────────
# │  지원자 특성(X)을 보고 **이직 여부**를 맞춘다.
# │  정답 열 이름: **target** → **1 = 이직**, **0 = 이직 안 함**
# └──────────────────────────────────────────────────────────
#
# ┌─ [제공 데이터] (이미 학습용/시험용으로 나뉨) ─────────────
# │  경로: BASE/HRdata/
# │  ┌─────────────────┬────────────────────────────────────
# │  │ 파일            │ 역할
# │  ├─────────────────┼────────────────────────────────────
# │  │ X_train.csv     │ 학습용 **입력만** (특성 + enrollee_id)
# │  │ y_train.csv     │ 학습용 **정답만** (target 열)
# │  │ X_test.csv      │ 시험용 **입력만** (특성 + enrollee_id)
# │  │ y_test.csv      │ 연습용 **정답** (채점은 보통 없음; 스스로 맞는지 확인)
# │  └─────────────────┴────────────────────────────────────
# └──────────────────────────────────────────────────────────
#
# ┌─ [수행 요구사항] (실기에서 할 일과 동일한 흐름) ─────────
# │  ① enrollee_id는 “사람 번호”이므로 **예측에 넣지 말고** 따로 빼 둔다.
# │  ② X_train, X_test에서 enrollee_id 열을 **제거**한 뒤 모델에 넣는다.
# │  ③ y_train은 **target 열 하나**만 써서 1차원 정답으로 만든다.
# │  ④ 글자(object) 열은 숫자로 바꾼다(예: LabelEncoder). 빈 칸은 채운다.
# │  ⑤ **분류** 모델로 학습 후, 시험용 X_test에 대해 예측한다.
# └──────────────────────────────────────────────────────────
#
# ┌─ [제출 산출물] ───────────────────────────────────────────
# │  파일명: **submission.csv** (저장 시 index=False)
# │  열 1: **enrollee_id** → X_test에 있던 지원자 ID 그대로 (순서 유지)
# │  열 2: **target** → 각 지원자별 예측값
# │        · 문제가 “0/1 예측”이면 → 0 또는 1 (predict)
# │        · 문제가 “AUC” 등 확률이면 → 0~1 사이 (predict_proba[:, 1])
# └──────────────────────────────────────────────────────────
#
# ┌─ [평가·연습 시 참고] ─────────────────────────────────────
# │  · 채점 방식은 **출제 기관·문제지 문구**를 따름 (accuracy, F1, AUC 등).
# │  · 이 데이터는 y_test가 있어 **연습 시** 예측과 비교해 정확도 등을 볼 수 있음.
# └──────────────────────────────────────────────────────────
#
# [학습 방법] import·BASE만 참고하고, **파일 읽기(Step 3)** 부터 직접 작성해 본다.
# ============================================================
#
# [기본 제공] Step 1~2 | [작성] Step 3~7
# ============================================================

# ---------- [기본 제공] Step 1: import ----------
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# ---------- [기본 제공] Step 2: BASE URL ----------
BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

# ---------- [작성] Step 3: X_train, X_test, y_train, y_test 로드 ----------
# TODO: X_train = pd.read_csv(f"{BASE}/HRdata/X_train.csv")
# TODO: X_test = pd.read_csv(f"{BASE}/HRdata/X_test.csv")
# TODO: y_train = pd.read_csv(f"{BASE}/HRdata/y_train.csv")
# TODO: y_test = pd.read_csv(f"{BASE}/HRdata/y_test.csv")

X_train = pd.read_csv(f"{BASE}/HRdata/X_train.csv")
X_test = pd.read_csv(f"{BASE}/HRdata/X_test.csv")
y_train = pd.read_csv(f"{BASE}/HRdata/y_train.csv")
y_test = pd.read_csv(f"{BASE}/HRdata/y_test.csv")



# ---------- [작성] Step 4: ID 분리, X/y 정리 ----------
# TODO: enrollee_id = X_test["enrollee_id"]
# TODO: X_train = X_train.drop(columns=["enrollee_id"])
# TODO: X_test = X_test.drop(columns=["enrollee_id"])
# TODO: y_train = y_train["target"]

enrollee_id = X_test["enrollee_id"]
X_train = X_train.drop(columns=["enrollee_id"])
X_test = X_test.drop(columns=["enrollee_id"])
y_train = y_train["target"]

# ---------- [작성] Step 5: 전처리 ----------
# TODO: 결측치, 범주형 인코딩 (city, gender 등)
# LabelEncoder 는 맨 위 Step 1에서 import

cat_cols = X_train.select_dtypes(include=["object"]).columns.tolist()
for col in cat_cols:
    le = LabelEncoder()
    # test에만 있는 범주(예: city_171)가 있으면 train만 fit 시 KeyError → train+test 값으로 함께 fit
    both = pd.concat([X_train[col], X_test[col]], axis=0).astype(str)
    le.fit(both)
    X_train[col] = le.transform(X_train[col].astype(str))
    X_test[col] = le.transform(X_test[col].astype(str))

X_train = X_train.fillna(0)
X_test = X_test.fillna(0)


# ---------- [작성] Step 6: 모델 학습 ----------
# TODO: model.fit(X_train, y_train)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


# ---------- [작성] Step 7: 예측 & 제출 ----------
# TODO: pred = model.predict(X_test)  # 또는 predict_proba[:,1]
# TODO: submission = pd.DataFrame({"enrollee_id": enrollee_id, "target": pred})
# TODO: submission.to_csv("submission.csv", index=False)

pred = model.predict(X_test)
submission = pd.DataFrame({"enrollee_id": enrollee_id, "target": pred})
submission.to_csv("submission.csv", index=False)
print("submission.csv SAVE COMPLETE")