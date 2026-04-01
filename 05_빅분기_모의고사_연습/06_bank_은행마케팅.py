# ╔══════════════════════════════════════════════════════════════╗
# ║  [2유형-분류] 06. Bank 은행 마케팅 (정기예금 가입 예측)            ║
# ╚══════════════════════════════════════════════════════════════╝
# ★ 바꿀 것: ① bank/  ② ID  ③ y (0/1)
# ★ train/test 분리형 | 범주형 있음


# ═══ STEP ①: import
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import LabelEncoder


# ═══ STEP ②: 로드
# BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
# train = pd.read_csv(f"{BASE}/bank/train.csv")
# test  = pd.read_csv(f"{BASE}/bank/test.csv")


# ═══ STEP ③④: y·X 분리
# y_train  = train["y"]
# X_train  = train.drop(columns=["y", "ID"])
# X_test   = test.drop(columns=["ID"])
# test_ids = test["ID"]


# ═══ STEP ⑤: 인코딩
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

# submission = pd.DataFrame({"ID": test_ids, "y": pred})
# submission.to_csv("submission.csv", index=False)
# print(submission.head())
