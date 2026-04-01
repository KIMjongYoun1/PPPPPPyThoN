# ╔══════════════════════════════════════════════════════════════╗
# ║  [2유형-분류] 07. Diabetes 당뇨병 예측                          ║
# ╚══════════════════════════════════════════════════════════════╝
# ★ 바꿀 것: ① diabetes/  ② ID (없으면 첫번째 열)  ③ Outcome (0/1)
# ★ X/y 분리형 | 수치형만 → 인코딩 불필요
#
# [ID열 자동감지 패턴 암기]
#   id_col = "ID" if "ID" in X_test.columns else X_test.columns[0]


# ═══ STEP ①: import
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier


# ═══ STEP ②: 로드
# BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
# X_train = pd.read_csv(f"{BASE}/diabetes/x_train.csv")
# X_test  = pd.read_csv(f"{BASE}/diabetes/x_test.csv")
# y_train = pd.read_csv(f"{BASE}/diabetes/y_train.csv")
# y_test  = pd.read_csv(f"{BASE}/diabetes/y_test.csv")


# ═══ STEP ③④: y·X 분리
# ID열 자동 감지 (없으면 첫 번째 열)
# id_col   = "ID" if "ID" in X_test.columns else X_test.columns[0]
# test_ids = X_test[id_col]
# X_train  = X_train.drop(columns=[id_col], errors="ignore")  # errors="ignore": 없어도 무시
# X_test   = X_test.drop(columns=[id_col])
# y_train  = y_train["Outcome"]


# ═══ STEP ⑤⑥: 결측치 (수치형만 → 인코딩 불필요)
# X_train = X_train.fillna(0)
# X_test  = X_test.fillna(0)


# ═══ STEP ⑦: 학습+예측+제출
# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)
# pred = model.predict(X_test)

# submission = pd.DataFrame({"ID": test_ids, "Outcome": pred})
# submission.to_csv("submission.csv", index=False)
# print("accuracy:", (pred == y_test["Outcome"].values).mean())
