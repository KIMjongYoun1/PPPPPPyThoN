# ============================================================
# 11. Titanic 타이타닉 (분류)
# [유형] 빅분기 실기 2유형(모델링) — 갈래 맞추기 (연습: Datamanim titanic)
# ============================================================
#
# ┌─ [문제 목표] ─────────────────────────────────────────────
# │  승객 정보로 **생존 여부(Survived)** 를 맞춘다 (0/1).
# └──────────────────────────────────────────────────────────
#
# ┌─ [제공 데이터] ───────────────────────────────────────────
# │  경로: BASE/titanic/train.csv **만** 제공되는 연습 구성 (별도 test 파일 없음).
# │  → **train_test_split** 으로 일부를 떼어 검증(또는 시험 대행)에 쓰는 패턴 연습.
# └──────────────────────────────────────────────────────────
#
# ┌─ [수행 요구사항] ─────────────────────────────────────────
# │  ① **Survived** 를 y로 두고 나머지 특성은 X (PassengerId 처리는 문제·관례에 따름).
# │  ② 범주형 인코딩·결측 처리 후 **train_test_split** (잘린 X_tr/X_val에 인코딩이 반영되게).
# │  ③ **분류** 모델 → 검증 셋 예측 또는 전체 학습 후 test 예측.
# └──────────────────────────────────────────────────────────
#
# ┌─ [산출물 / 정답 형식] ───────────────────────────────────
# │  **submission.csv** 예: **PassengerId**, **Survived** (실제 시험은 문제지 열 이름 따름).
# └──────────────────────────────────────────────────────────
#
# ┌─ [평가·연습 시 참고] ─────────────────────────────────────
# │  · Kaggle식으로 test.csv가 주어지면 동일하게 ID 빼고 예측 후 제출.
# └──────────────────────────────────────────────────────────
#
# [학습 방법] import·BASE만 참고하고, **train 읽기(Step 3)** 직접 작성 후 Step 4~7.
# ============================================================
#
# ┌─ [코드 보존·피드백] 커서룰 ───────────────────────────────
# │  · **내 코드** → `# --- 내 코드 ---` 아래에 주석으로 원문 유지.
# │  · **보완** → 그 블록 **바로 다음 줄부터** `# AI:` 이유 → 실행용 보완 코드.
# │  · 통째 복제·USER_ORIGINAL 한 덩어리 문자열보다, **이웃한 줄**에 붙이는 걸 우선.
# └──────────────────────────────────────────────────────────
#
# [기본 제공] Step 1~2 | [작성] Step 3~7
# ============================================================

# ---------- [기본 제공] Step 1: import ----------
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# ---------- [기본 제공] Step 2: BASE URL ----------
BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

# ---------- [작성] Step 3~7 ----------
# --- 내 코드 ---
# train = pd.read_csv(f"{BASE}/titanic/train.csv")
# head = pd.read_csv(f"{BASE}/titanic/train.csv").head()
# print(head)
# AI: 같은 CSV를 두 번 읽을 필요 없음. 이미 만든 train으로 앞부분·행 개수만 보면 됨.
train = pd.read_csv(f"{BASE}/titanic/train.csv")
print(train.head())
print("train.shape:", train.shape)

# --- 내 코드 ---
# X = train.drop(columns=["Survived"])
# y = train["Survived"]
# AI: 이 구간은 그대로 써도 됨 (아래 실행 코드 동일).
X = train.drop(columns=["Survived"])
y = train["Survived"]

# --- 내 코드 ---
# X_tr, X_val, y_tr, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
# print("Xval", X_val)
# print("yval", y_val)
# print("Xtr", X_tr)
# print("ytr", y_tr)
# cat_col = X.select_dtypes(include=["object"]).columns.tolist()
# for col in cat_col:
#     le = LabelEncoder()
#     X[col] = le.fit_transform(X[col].astype(str))
# X = X.fillna(0)
# AI: split 을 먼저 하면 for 문이 고치는 건 전체 X뿐이라 X_tr/X_val 은 문자열·결측이 남을 수 있음.
#     인코딩·fillna 끝낸 뒤 split 하면 잘린 조각에도 반영됨.
cat_col = X.select_dtypes(include=["object"]).columns.tolist()
for col in cat_col:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))

X = X.fillna(0)

X_tr, X_val, y_tr, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print("분할 후:", X_tr.shape, X_val.shape, y_tr.shape, y_val.shape)

# --- 내 코드 ---
# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_tr, y_tr)
# pred = model.predict(X_val)
# submission = pd.DataFrame({"PassengerId": X_val}, "Survived": pred)
# submission.to_csv("submission.csv", index=False)
# AI: DataFrame 은 dict 하나에 열이 들어가야 함. PassengerId 는 X_val 전체가 아니라 열: X_val["PassengerId"].
#     검증 점수는 pred 와 y_val 과 비교.
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_tr, y_tr)

pred = model.predict(X_val)
print("accuracy (검증):", (pred == y_val.values).mean())

submission = pd.DataFrame({"PassengerId": X_val["PassengerId"], "Survived": pred})
submission.to_csv("submission.csv", index=False)
print("submission.csv 저장 완료")
print(submission.head())
