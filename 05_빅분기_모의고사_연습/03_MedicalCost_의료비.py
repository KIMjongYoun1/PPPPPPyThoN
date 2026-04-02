# ╔══════════════════════════════════════════════════════════════╗
# ║  [2유형-회귀] 03. MedicalCost 의료비 예측                       ║
# ╚══════════════════════════════════════════════════════════════╝
# ★ 바꿀 것: ① MedicalCost/  ② ID없음→index사용  ③ charges (연속값)
# ★ ⚠️ ID열 없는 경우: test_ids = X_test.index  (행 번호를 ID로)
#   ※ 지문 판단법: "의료비를 예측하시오" → 금액(소수 연속값) → 회귀
#                  import: RandomForestRegressor
#
# [ID 없는 경우 암기] test_ids = X_test.index → DataFrame({"ID": test_ids, ...})


# ═══ STEP ①: import
# import pandas as pd
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.preprocessing import LabelEncoder


# ═══ STEP ②: 로드
# BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
# train = pd.read_csv(f"{BASE}/MedicalCost/train.csv")
# test  = pd.read_csv(f"{BASE}/MedicalCost/test.csv")


# ═══ STEP ③④: y·X 분리
# y_train  = train["charges"]
# X_train  = train.drop(columns=["charges"])
# X_test   = test.copy()
# test_ids = X_test.index          # ⚠️ ID없으면 인덱스(행번호)를 ID로 사용


# ═══ STEP ⑤: 인코딩 (sex, smoker, region 등 글자열)
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
# model = RandomForestRegressor(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)
# pred = model.predict(X_test)

# submission = pd.DataFrame({"ID": test_ids, "charges": pred})
# submission.to_csv("submission.csv", index=False)
# print(submission.head())
