# ╔══════════════════════════════════════════════════════════════╗
# ║  [2유형-분류] 10. Stroke 뇌졸중 예측                            ║
# ╚══════════════════════════════════════════════════════════════╝
# ★ 바꿀 것: ① stroke_/ (밑줄!)  ② id (소문자!)  ③ stroke (0/1)
# ★ ⚠️ 폴더명 stroke_ / ID열 소문자 id — 대소문자 틀리면 FileNotFoundError


# ═══ STEP ①: import
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import LabelEncoder


# ═══ STEP ②: 로드
# BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
# train = pd.read_csv(f"{BASE}/stroke_/train.csv")   # ⚠️ stroke_ (밑줄!)
# test  = pd.read_csv(f"{BASE}/stroke_/test.csv")


# ═══ STEP ③④: y·X 분리
# y_train  = train["stroke"]
# X_train  = train.drop(columns=["stroke", "id"])    # ⚠️ id 소문자
# X_test   = test.drop(columns=["id"])
# test_ids = test["id"]


# ═══ STEP ⑤: 인코딩 (gender, work_type 등)
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

# ⚠️ 제출 열명도 소문자 id, stroke
# submission = pd.DataFrame({"id": test_ids, "stroke": pred})
# submission.to_csv("submission.csv", index=False)
# print(submission.head())
