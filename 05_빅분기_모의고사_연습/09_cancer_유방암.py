# ╔══════════════════════════════════════════════════════════════╗
# ║  [2유형-분류] 09. Cancer 유방암 예측                            ║
# ╚══════════════════════════════════════════════════════════════╝
# ★ 바꿀 것: ① cancer/  ② ID  ③ diagnosis (M=악성/B=양성)
# ★ ⚠️ y가 글자(M/B) → LabelEncoder로 숫자 변환 후 학습, 제출도 숫자
#
# [y 글자→숫자 암기]
#   le_y = LabelEncoder()
#   y_enc = le_y.fit_transform(y_train["열명"])   ← 학습용
#   le_y.inverse_transform(pred)                  ← 글자로 복원 (필요시)


# ═══ STEP ①: import
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import LabelEncoder


# ═══ STEP ②: 로드
# BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
# X_train = pd.read_csv(f"{BASE}/cancer/x_train.csv")
# X_test  = pd.read_csv(f"{BASE}/cancer/x_test.csv")
# y_train = pd.read_csv(f"{BASE}/cancer/y_train.csv")
# y_test  = pd.read_csv(f"{BASE}/cancer/y_test.csv")


# ═══ STEP ③④: y·X 분리
# id_col   = "ID" if "ID" in X_test.columns else X_test.columns[0]
# test_ids = X_test[id_col]
# X_train  = X_train.drop(columns=[id_col], errors="ignore")
# X_test   = X_test.drop(columns=[id_col])

# y도 LabelEncoder 필요 (M/B → 0/1)
# le_y    = LabelEncoder()
# y_train = le_y.fit_transform(y_train["diagnosis"])


# ═══ STEP ⑤⑥: 결측치 (수치형만)
# X_train = X_train.fillna(0)
# X_test  = X_test.fillna(0)


# ═══ STEP ⑦: 학습+예측+제출
# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)
# pred = model.predict(X_test)

# submission = pd.DataFrame({"ID": test_ids, "target": pred})
# submission.to_csv("submission.csv", index=False)
# y_test_enc = le_y.transform(y_test["diagnosis"])
# print("accuracy:", (pred == y_test_enc).mean())
