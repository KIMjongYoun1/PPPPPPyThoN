# ╔══════════════════════════════════════════════════════════════╗
# ║  [2유형-분류] 11. Titanic 타이타닉 생존 예측                     ║
# ╚══════════════════════════════════════════════════════════════╝
# ★ ⚠️ train.csv만 제공 → train_test_split으로 직접 나눔
# ★ 정답열: Survived / ID열: PassengerId
#
# [train만 있을 때 패턴]
#   X, y 분리 → train_test_split → X_tr/X_val/y_tr/y_val
# [stratify 암기]
#   stratify=y → 정답 분포 유지하며 분할 (불균형 데이터에 필수)


# ═══ STEP ①: import
# import pandas as pd
# from sklearn.model_selection import train_test_split  # train만 있을 때 필요
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import LabelEncoder


# ═══ STEP ②: 로드 (train만)
# BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
# train = pd.read_csv(f"{BASE}/titanic/train.csv")
# print(train.head(2))


# ═══ STEP ③④: y·X 분리
# X = train.drop(columns=["Survived"])
# y = train["Survived"]


# ═══ STEP ⑤: 인코딩
# cat_col = X.select_dtypes(include=["object"]).columns.tolist()
# for col in cat_col:
#     le = LabelEncoder()
#     X[col] = le.fit_transform(X[col].astype(str))  # train만 있어 train으로만 fit


# ═══ STEP ⑥: 결측치
# X = X.fillna(0)


# ═══ STEP ⑦: train_test_split → 학습+제출
# X_tr, X_val, y_tr, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_tr, y_tr)
# pred = model.predict(X_val)
# print("accuracy:", (pred == y_val.values).mean())

# submission = pd.DataFrame({"PassengerId": X_val["PassengerId"], "Survived": pred})
# submission.to_csv("submission.csv", index=False)
# print(submission.head())
