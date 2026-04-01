# ╔══════════════════════════════════════════════════════════════╗
# ║  [2유형-회귀] 01. Admission 대학원 합격률 예측                  ║
# ╚══════════════════════════════════════════════════════════════╝
# ★ 시험에서 바꿀 3가지: ① 데이터 경로  ② ID열 이름  ③ 정답열 이름
#   ① admission/     ② Serial No.     ③ Chance of Admit  (끝에 공백!)
#
# ─────────────────────────────────────────────────
# ★★ 2유형 시험 공략법 ★★
# ─────────────────────────────────────────────────
# [분류 vs 회귀 구분]
#   정답이 0/1, 예/아니오, 글자 라벨  →  분류 (RandomForestClassifier)
#   정답이 가격, 점수, 확률 등 연속값  →  회귀 (RandomForestRegressor)
#   ※ 이 문제: 합격가능성(0.0~1.0 실수)  →  회귀 선택
#
# [7단계 뼈대 — 무조건 암기, 어떤 문제도 이 구조]
#   ① import   : pandas + sklearn 라이브러리 3줄
#   ② 로드     : train/test CSV 두 줄
#   ③ y 분리   : 정답열 꺼내기 (y_train)
#   ④ X 분리   : ID+정답 제거 → 특성만 (X_train, X_test)
#   ⑤ 인코딩   : 글자열(object) → 숫자 (LabelEncoder)
#   ⑥ 결측처리 : 빈 칸 채우기 (fillna)
#   ⑦ 학습+제출: fit → predict → to_csv(index=False)
#
# [시험 준비법]
#   이 파일 주석 보면서 빈 .py 파일에 직접 타이핑 → 반복
#   → 주석만 보고 코드가 바로 나올 때까지 연습
#   → 02~15번 모두 이 7단계 동일, 경로/열명만 다름
# ─────────────────────────────────────────────────


# ═══ STEP ①: import ══════════════════════════════════════════
# pandas로 표를 다루고, sklearn으로 모델을 만든다
# 회귀=Regressor / 분류=Classifier  (R=숫자, C=갈래)

# import pandas as pd
# from sklearn.ensemble import RandomForestRegressor  # 회귀: Regressor
# from sklearn.preprocessing import LabelEncoder       # 글자→숫자 변환기


# ═══ STEP ②: 데이터 로드 ═════════════════════════════════════
# train(정답 포함) / test(정답 없음) 두 파일 모두 읽는다
# 이 2줄은 항상 고정 — 경로(admission)만 바꾼다

# BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
# train = pd.read_csv(f"{BASE}/admission/train.csv")
# test  = pd.read_csv(f"{BASE}/admission/test.csv")

# [시험장 첫 동작] shape+head로 열 이름·행 수 파악 → 정답열·ID열 이름 확인
# print("train:", train.shape)
# print(train.head(2))
# print("test:", test.shape)


# ═══ STEP ③: y(정답) 분리 ════════════════════════════════════
# 모델에 정답을 따로 줘야 학습이 가능하다
# 열 이름을 head()로 정확히 확인! 공백·대소문자 틀리면 KeyError
# ⚠️ 이 데이터는 "Chance of Admit " — 끝에 공백 포함

# y_train = train["Chance of Admit "]   # 정답열
# ids     = test["Serial No."]          # 제출파일에 넣을 ID (나중에 사용)


# ═══ STEP ④: X(특성) 분리 ════════════════════════════════════
# 모델 입력(X)에는 정답열과 ID열이 없어야 한다
# train: 정답열 + ID열 둘 다 제거 / test: ID열만 제거

# X_train = train.drop(columns=["Chance of Admit ", "Serial No."])
# X_test  = test.drop(columns=["Serial No."])


# ═══ STEP ⑤: 인코딩 (글자열 → 숫자) ════════════════════════
# sklearn 모델은 숫자만 받는다 — 글자(object) 열을 숫자로 바꿔야 한다
# ⚠️ 핵심: train+test 합쳐서 fit → test에만 있는 값도 오류 없이 처리

# num_cols = X_train.select_dtypes(include=["number"]).columns    # 수치형 열
# cat_cols = X_train.select_dtypes(include=["object", "string"]).columns  # 글자형 열

# for c in num_cols:                          # 수치형 결측 → train 중앙값으로
#     med = X_train[c].median()
#     X_train[c] = X_train[c].fillna(med)
#     X_test[c]  = X_test[c].fillna(med)     # test도 train 통계로 채움

# for c in cat_cols:                          # 글자형 결측 → 최빈값으로
#     mode = X_train[c].mode().iloc[0]
#     X_train[c] = X_train[c].fillna(mode)
#     X_test[c]  = X_test[c].fillna(mode)
#     le   = LabelEncoder()
#     comb = pd.concat([X_train[c], X_test[c]]).astype(str)  # 합쳐서 fit!
#     le.fit(comb)
#     X_train[c] = le.transform(X_train[c].astype(str))
#     X_test[c]  = le.transform(X_test[c].astype(str))


# ═══ STEP ⑥: 결측치 처리 ═════════════════════════════════════
# 빈 칸이 있으면 모델이 오류난다 — 반드시 채워야 한다
# [빠른 방법] 시간 없으면 아래 2줄로 한번에 (위 반복문 대신 사용 가능)

# X_train = X_train.fillna(0)
# X_test  = X_test.fillna(0)


# ═══ STEP ⑦: 학습 + 예측 + 제출 ══════════════════════════════
# 모델에 X_train/y_train을 주고 패턴 학습 → X_test로 예측
# n_estimators=100~200, random_state=42 고정값으로 암기

# model = RandomForestRegressor(n_estimators=200, random_state=42)
# model.fit(X_train, y_train)               # 학습

# pred = model.predict(X_test)              # 예측
# ※ 회귀: predict()만 / 분류: predict_proba()[:,1] 확률 필요 시

# ⚠️ index=False 필수 — 빠뜨리면 0,1,2... 열 추가돼서 오답 처리!
# submission = pd.DataFrame({"Serial No.": ids, "Chance of Admit ": pred})
# submission.to_csv("submission.csv", index=False)
# print("저장 완료")
# print(submission.head())
