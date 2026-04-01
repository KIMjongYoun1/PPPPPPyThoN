# ╔══════════════════════════════════════════════════════════════╗
# ║  [2유형-분류] 21. Drug 약물 분류 (다중분류)                       ║
# ╚══════════════════════════════════════════════════════════════╝
# ★ 바꿀 것: ① drug/  ② ID  ③ Drug (DrugA/B/C/X/Y 등 글자 라벨)
# ★ ⚠️ 다중분류: 정답이 2개 이상 → y도 LabelEncoder 필요
#
# [다중분류 y처리 암기]
#   le_y = LabelEncoder()
#   y_enc = le_y.fit_transform(y_train["Drug"])   ← 학습: 숫자로
#   pred  = le_y.inverse_transform(pred_enc)       ← 제출: 글자로 복원


# ═══ STEP ①: import
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import LabelEncoder


# ═══ STEP ②: 로드
# BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
# X_train = pd.read_csv(f"{BASE}/drug/x_train.csv")
# X_test  = pd.read_csv(f"{BASE}/drug/x_test.csv")
# y_train = pd.read_csv(f"{BASE}/drug/y_train.csv")
# y_test  = pd.read_csv(f"{BASE}/drug/y_test.csv")


# ═══ STEP ③④: y·X 분리
# id_col   = "ID" if "ID" in X_test.columns else X_test.columns[0]
# test_ids = X_test[id_col]
# X_train  = X_train.drop(columns=[id_col], errors="ignore")
# X_test   = X_test.drop(columns=[id_col])
# y_train  = y_train["Drug"]


# ═══ STEP ⑤: X 인코딩 (범주형)
# cat_cols = X_train.select_dtypes(include=["object"]).columns.tolist()
# for col in cat_cols:
#     le   = LabelEncoder()
#     comb = pd.concat([X_train[col], X_test[col]]).astype(str)
#     le.fit(comb)
#     X_train[col] = le.transform(X_train[col].astype(str))
#     X_test[col]  = le.transform(X_test[col].astype(str))

# y도 인코딩 (글자→숫자)
# le_y      = LabelEncoder()
# y_train_enc = le_y.fit_transform(y_train)


# ═══ STEP ⑥: 결측치
# X_train = X_train.fillna(0)
# X_test  = X_test.fillna(0)


# ═══ STEP ⑦: 학습+예측+제출
# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train_enc)
# pred_enc = model.predict(X_test)
# pred     = le_y.inverse_transform(pred_enc)   # 숫자 → 약 이름 복원

# submission = pd.DataFrame({"ID": test_ids, "Drug": pred})
# submission.to_csv("submission.csv", index=False)
# print("accuracy:", (pred == y_test["Drug"].values).mean())
