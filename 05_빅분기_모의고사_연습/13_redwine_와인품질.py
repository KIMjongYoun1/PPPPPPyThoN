# ╔══════════════════════════════════════════════════════════════╗
# ║  [2유형-회귀] 13. RedWine 와인 품질 예측                         ║
# ╚══════════════════════════════════════════════════════════════╝
# ★ 바꿀 것: ① redwine/  ② ID  ③ quality (연속값)
# ★ X/y 분리형 | 수치형만 → 인코딩 불필요
# ★ 성능지표: RMSE = np.sqrt(mean_squared_error(실제, 예측))
#   ※ 지문 판단법: "와인 품질을 예측하시오" → 품질 점수(소수 연속값) → 회귀
#                  import: RandomForestRegressor


# ═══ STEP ①: import
# import pandas as pd
# from sklearn.ensemble import RandomForestRegressor   # 회귀: Regressor
# import numpy as np
# from sklearn.metrics import mean_squared_error


# ═══ STEP ②: 로드
# BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
# X_train = pd.read_csv(f"{BASE}/redwine/x_train.csv")
# X_test  = pd.read_csv(f"{BASE}/redwine/x_test.csv")
# y_train = pd.read_csv(f"{BASE}/redwine/y_train.csv")
# y_test  = pd.read_csv(f"{BASE}/redwine/y_test.csv")


# ═══ STEP ③④: y·X 분리
# id_col   = "ID" if "ID" in X_test.columns else X_test.columns[0]
# test_ids = X_test[id_col]
# X_train  = X_train.drop(columns=[id_col], errors="ignore")
# X_test   = X_test.drop(columns=[id_col])
# y_train  = y_train["quality"]


# ═══ STEP ⑤⑥: 결측치 (수치형만)
# X_train = X_train.fillna(0)
# X_test  = X_test.fillna(0)


# ═══ STEP ⑦: 학습+예측+제출
# model = RandomForestRegressor(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)
# pred = model.predict(X_test)

# submission = pd.DataFrame({"ID": test_ids, "quality": pred})
# submission.to_csv("submission.csv", index=False)
# print("RMSE:", np.sqrt(mean_squared_error(y_test["quality"], pred)))
