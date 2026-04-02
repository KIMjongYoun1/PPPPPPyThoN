# ╔══════════════════════════════════════════════════════════════╗
# ║  [2유형-분류] 04. HRdata 이직 예측                              ║
# ╚══════════════════════════════════════════════════════════════╝
# ★ 바꿀 것: ① HRdata/  ② enrollee_id  ③ target (0=잔류 1=이직)
# ★ ⚠️ X/y 파일 분리형: X_train.csv + y_train.csv + X_test.csv 따로 로드
#   ※ 지문 판단법: "이직 여부를 예측하시오" → 이직함/안함, 둘 중 하나 → 분류
#                  import: RandomForestClassifier
#
# [X/y 분리형 vs train/test 분리형]
#   train/test 분리형: train 안에 정답열 있음 → train["정답열"]로 꺼냄
#   X/y 분리형:        y_train.csv 별도 존재 → y_train["정답열"]로 꺼냄


# ═══ STEP ①: import
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import LabelEncoder


# ═══ STEP ②: 로드 (X/y 분리형 → 파일 4개)
# BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
# X_train = pd.read_csv(f"{BASE}/HRdata/X_train.csv")
# X_test  = pd.read_csv(f"{BASE}/HRdata/X_test.csv")
# y_train = pd.read_csv(f"{BASE}/HRdata/y_train.csv")
# y_test  = pd.read_csv(f"{BASE}/HRdata/y_test.csv")  # 연습용


# ═══ STEP ③④: y·X 분리
# enrollee_id = X_test["enrollee_id"]               # 제출용 ID 먼저 보관
# X_train     = X_train.drop(columns=["enrollee_id"])
# X_test      = X_test.drop(columns=["enrollee_id"])
# y_train     = y_train["target"]                   # ⚠️ DataFrame→Series (1열만 꺼내기)


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

# submission = pd.DataFrame({"enrollee_id": enrollee_id, "target": pred})
# submission.to_csv("submission.csv", index=False)
# print("accuracy:", (pred == y_test["target"].values).mean())
