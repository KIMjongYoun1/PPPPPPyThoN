# ╔══════════════════════════════════════════════════════════════╗
# ║  [2유형-분류] 02. Churn 고객 이탈 예측                         ║
# ╚══════════════════════════════════════════════════════════════╝
# ★ 바꿀 것: ① churn/  ② CustomerId  ③ Exited (0=잔류 1=이탈)
# ★ 분류 = RandomForestClassifier | predict() → 0 또는 1
#
# [7단계 뼈대] import → 로드 → y분리 → X분리 → 인코딩 → 결측 → 학습+제출
# [train/test 분리형] train에 정답열 포함 → y꺼내기 → drop으로 X만들기


# ═══ STEP ①: import
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier  # 분류: Classifier
# from sklearn.preprocessing import LabelEncoder


# ═══ STEP ②: 로드
# BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
# train = pd.read_csv(f"{BASE}/churn/train.csv")
# test  = pd.read_csv(f"{BASE}/churn/test.csv")


# ═══ STEP ③④: y·X 분리
# y_train  = train["Exited"]
# X_train  = train.drop(columns=["Exited", "CustomerId"])  # 정답+ID 둘 다 제거
# X_test   = test.drop(columns=["CustomerId"])
# test_ids = test["CustomerId"]                            # 제출용 ID 보관


# ═══ STEP ⑤: 인코딩 (글자열 → 숫자)
# ⚠️ train+test 합쳐서 fit → test에만 있는 값도 오류 없이 처리
# cat_cols = X_train.select_dtypes(include=["object"]).columns.tolist()
# for col in cat_cols:
#     le   = LabelEncoder()
#     comb = pd.concat([X_train[col], X_test[col]]).astype(str)
#     le.fit(comb)
#     X_train[col] = le.transform(X_train[col].astype(str))
#     X_test[col]  = le.transform(X_test[col].astype(str))


# ═══ STEP ⑥: 결측치
# X_train = X_train.fillna(0)
# X_test  = X_test.fillna(0)


# ═══ STEP ⑦: 학습+예측+제출
# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)
# pred = model.predict(X_test)

# ⚠️ index=False 필수!
# submission = pd.DataFrame({"CustomerId": test_ids, "Exited": pred})
# submission.to_csv("submission.csv", index=False)
# print(submission.head())
