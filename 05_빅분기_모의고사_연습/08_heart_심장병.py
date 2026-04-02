# ╔══════════════════════════════════════════════════════════════╗
# ║  [2유형-분류] 08. Heart 심장병 예측                             ║
# ╚══════════════════════════════════════════════════════════════╝
# ★ 바꿀 것: ① heart/  ② ID  ③ target (0/1)
# ★ X/y 분리형 | 범주형 있음
#   ※ 지문 판단법: "심장병 여부를 예측하시오" → 있음/없음, 둘 중 하나 → 분류
#                  import: RandomForestClassifier


# ═══ STEP ①: import
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import LabelEncoder


# ═══ STEP ②: 로드
# BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
# X_train = pd.read_csv(f"{BASE}/heart/x_train.csv")
# X_test  = pd.read_csv(f"{BASE}/heart/x_test.csv")
# y_train = pd.read_csv(f"{BASE}/heart/y_train.csv")
# y_test  = pd.read_csv(f"{BASE}/heart/y_test.csv")


# ═══ STEP ③④: y·X 분리
# id_col   = "ID" if "ID" in X_test.columns else X_test.columns[0]
# test_ids = X_test[id_col]
# X_train  = X_train.drop(columns=[id_col], errors="ignore")
# X_test   = X_test.drop(columns=[id_col])
# y_train  = y_train["target"]


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

# submission = pd.DataFrame({"ID": test_ids, "target": pred})
# submission.to_csv("submission.csv", index=False)
# print("accuracy:", (pred == y_test["target"].values).mean())
