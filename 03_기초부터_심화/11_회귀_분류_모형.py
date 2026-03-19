# ============================================================
# 11. 회귀·분류 모형 구축 (빅분기·실무)
# ============================================================
#
# [회귀 vs 분류가 뭐냐]
# - 분류(Classification): 예측 결과가 몇 개의 카테고리 중 하나.
#   예) 0/1, 합격/불합격, 정상/불량, A/B/C 등 → "라벨" 맞히기.
# - 회귀(Regression): 예측 결과가 연속된 숫자.
#   예) 금액, 점수, 매출, 온도, 집값 등 → "숫자" 맞히기.
#
# [왜 train / test 를 나누냐]
# - train: 모델이 배우는 데이터. 여기로만 fit.
# - test: "처음 보는 데이터"라고 가정하고 성능을 확인하는 용도.
# - train만 잘 맞으면 과적합이어서, 항상 train_test_split 으로 나눠서
#   train으로 fit, test로 평가(accuracy, RMSE 등)를 보는 패턴을 쓴다.
#
# [전처리 → 모델 흐름 (시험·실무 공통 패턴)]
# 1) 데이터 읽기 (pandas)
# 2) 결측/이상치 처리
# 3) 범주 인코딩(라벨/원-핫), 파생변수 생성
# 4) X(입력), y(정답) 분리
# 5) train/test 분리 (train_test_split)
# 6) 스케일링 (StandardScaler, MinMaxScaler 등)
#    - scaler.fit(X_train)
#    - X_train_s = scaler.transform(X_train)
#    - X_test_s = scaler.transform(X_test)
# 7) 모델 선택 후 학습
#    - 회귀: LinearRegression, RandomForestRegressor 등
#    - 분류: LogisticRegression, RandomForestClassifier 등
# 8) 예측·평가
#    - y_pred = model.predict(X_test_s)
#    - 분류: accuracy, F1, 혼동행렬 / 회귀: RMSE, MAE 등
#
# [이 파일의 예제 구성]
# - (1) 분류 예제: 랜덤 데이터로 0/1 클래스를 예측 (train/test, 스케일링, RandomForestClassifier).
# - (2) 회귀 예제: 점수로 어떤 연속값을 예측 (LinearRegression).
# - (3) 간단 분류 예제: 점수 70 이상이면 합격(1), 아니면 불합격(0)을 예측.
#
# [import — 각 모듈 역할]
# pandas (pd): DataFrame, 데이터 읽기·전처리.
# numpy (np): 배열, random(난수), array 등.
# train_test_split: X, y를 train/test로 나눔. stratify로 클래스 비율 유지.
# StandardScaler: 표준화. fit, transform.
# LabelEncoder: 범주형(문자) → 숫자(0,1,2...) 변환.
# LinearRegression: 회귀 모델.
# RandomForestClassifier, RandomForestRegressor: 분류·회귀 앙상블 모델.
# ============================================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

# ---------- 따라 칠 코드 (1): 분류 — train/test 분리, 스케일링, 학습, 예측 ----------
np.random.seed(42)  # 난수 고정. 같은 결과가 나오게 함.
n = 80  # 데이터 개수
df = pd.DataFrame({
    "특징1": np.random.randn(n) * 10 + 50,   # 랜덤 숫자 (평균 50 근처)
    "특징2": np.random.randn(n) * 5 + 20,   # 랜덤 숫자 (평균 20 근처)
})
# 0/1 구분 기준: 특징1 + 특징2 >= 70 이면 1(합격), 아니면 0(불합격)
df["클래스"] = np.where(df["특징1"] + df["특징2"] >= 70, 1, 0)
X = df[["특징1", "특징2"]]   # 모델에 넣을 입력(특징)
y = df["클래스"]             # 맞춰야 할 정답
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
# train 80%, test 20% 로 나눔. stratify=y → 0/1 비율 유지

scaler = StandardScaler()   # 표준화 도구
X_train_s = scaler.fit_transform(X_train)   # train으로 기준 잡고, train 표준화
X_test_s = scaler.transform(X_test)        # test는 transform만 (fit 안 함)

model = RandomForestClassifier(n_estimators=50, random_state=42)  # 분류 모델 (트리 50개)
model.fit(X_train_s, y_train)   # 학습
y_pred = model.predict(X_test_s)  # 예측
print("분류 예측 샘플:", y_pred[:5])

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

np.random.seed(42)
n = 80
df = pd.DataFrame ({
    "특징1" : np.random.randn(n) * 10 + 50,
    "특징2" : np.random.randn(n) * 5 + 20,
    
})
df["Class"] = np.where(df["특징1"] + df["특징2"] >= 33, 1, 0) 
X = df[["특징1", "특징2"]]
y = df["Class"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42, stratify = y)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)
model = RandomForestClassifier(n_estimators = 50, random_state = 42)
model.fit(X_train_s, y_train)
y_pred = model.predict(X_test_s)
print(f"분류 예측 셈플 : {y_pred[:5]}")

# ---------- 따라 칠 코드 (2): 회귀 — 연속값 예측 ----------
df2 = pd.DataFrame({
    "x1": np.random.rand(50) * 10,
    "x2": np.random.rand(50) * 5,
})
df2["y"] = 2 * df2["x1"] + 3 * df2["x2"] + np.random.randn(50)  # y ≈ 2*x1 + 3*x2 + 노이즈
Xr = df2[["x1", "x2"]]   # 입력
yr = df2["y"]            # 예측할 연속값(정답)
Xr_tr, Xr_te, yr_tr, yr_te = train_test_split(Xr, yr, test_size=0.2, random_state=42)
scaler_r = StandardScaler()
Xr_tr_s = scaler_r.fit_transform(Xr_tr)   # train 표준화
Xr_te_s = scaler_r.transform(Xr_te)       # test transform만
reg = RandomForestRegressor(n_estimators=50, random_state=42)  # 회귀 모델
reg.fit(Xr_tr_s, yr_tr)   # 학습
yr_pred = reg.predict(Xr_te_s)  # 연속값 예측
print("회귀 예측 샘플:", yr_pred[:5])

# y 생성 공식 로그: y = 2*x1 + 3*x2 + 노이즈 (소수점은 x1,x2가 rand라 0~10 실수, 노이즈도 실수)
print("--- 회귀 연산 공식 ---")
print("y 생성 공식: y = 2*x1 + 3*x2 + np.random.randn() (노이즈)")
print("예시 (test 5개): x1, x2 → y_정답(공식) | y_예측(모델)")
for i in range(5):
    x1, x2 = Xr_te.iloc[i]["x1"], Xr_te.iloc[i]["x2"]
    y_true = yr_te.iloc[i]
    y_pr = yr_pred[i]
    print(f"  {i+1}: x1={x1:.3f}, x2={x2:.3f} → 정답={y_true:.3f} | 예측={y_pr:.3f}")

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

df2 = pd.DataFrame({
    "x1" : np.random.randint(0,20,50) * 10,
    "x2" : np.random.randint(0,50,50) * 5,
})
df2["y"] = 2 * df2["x1"] + 3 * df2["x2"] + np.random.randint(50)
Xr = df2[["x1", "x2"]]
yr = df2["y"]
Xr_tr, Xr_te, yr_tr, yr_te = train_test_split(Xr, yr, test_size = 0.2, random_state=42)
scaler_r = StandardScaler()
Xr_tr_s = scaler_r.fit_transform(Xr_tr)
Xr_te_s = scaler_r.transform(Xr_te)
reg = RandomForestRegressor(n_estimators=50, random_state=42)
reg.fit(Xr_tr_s, yr_tr)
yr_pred = reg.predict(Xr_te_s)
print(f"회귀 예측 셈플 : {yr_pred[:5]}")
print("--- 회귀 연산 공식 ---")
print("y 생성 공식: y = 2*x1 + 3*x2 + np.random.randn() (노이즈)")
print("예시 (test 5개): x1, x2 → y_정답(공식) | y_예측(모델)")
for i in range(5):
    x1, x2 = Xr_te.iloc[i]["x1"], Xr_te.iloc[i]["x2"]
    y_true = yr_te.iloc[i]
    y_pr = yr_pred[i]
    print(f"  {i+1}: x1={x1:.3f}, x2={x2:.3f} → 정답={y_true:.3f} | 예측={y_pr:.3f}")

# ---------- 따라 칠 코드 (3): 범주형이 있을 때 LabelEncoder ----------
df3 = pd.DataFrame({
    "직업": ["A", "B", "A", "B", "A"],
    "점수": [70, 80, 75, 85, 72],
})
le = LabelEncoder()   # 문자 → 숫자로 바꾸는 도구
df3["직업_코드"] = le.fit_transform(df3["직업"])   # A→0, B→1 등으로 변환
X3 = df3[["직업_코드", "점수"]]   # 이후 train_test_split → 스케일 → fit 동일

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
df3 = pd.DataFrame({
    "직업" : ["A","B","A","A","B"],
    "점수" : [20, 50,99,32,21],
})
label = LabelEncoder()
df3["직업_코드"] = label.fit_transform(df3["직업"])
X3 = df3[["직업_코드", "점수"]]
print(X3)

# ---------- 예제 ----------
# 아래 데이터로 "합격(1)/불합격(0)" 분류 모델을 만들고, 마지막 한 행에 대한 예측을 출력하세요.

exam = pd.DataFrame({
    "점수": [60, 75, 80, 55, 90, 70],
    "합격": [0, 1, 1, 0, 1, 1],
})
X_ex = exam[["점수"]]   # 입력
y_ex = exam["합격"]    # 정답
scaler_ex = StandardScaler()
X_ex_s = scaler_ex.fit_transform(X_ex)   # 전체로 fit (예제라 train/test 안 나눔)
clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(X_ex_s, y_ex)   # 학습
last = scaler_ex.transform(pd.DataFrame({"점수": [70]}))   # 열 이름 맞추면 경고 없음
print("점수 70 예측:", clf.predict(last)[0])

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier

exam = pd.DataFrame({
    "점수" : [60, 61, 70, 65, 80, 64],
    "합격" : [0, 0 ,1, 1, 1 ,0],
})
X_ex = exam[["점수"]]
y_ex = exam["합격"]

scaler_ex = StandardScaler()
X_ex_s = scaler_ex.fit_transform(X_ex)
clf = RandomForestClassifier(n_estimators = 10, random_state = 42)
clf.fit(X_ex_s, y_ex)
last = scaler_ex.transform(pd.DataFrame({"점수": [32]}))  # 열 이름 맞추면 경고 없음
print(f"점수 65 예측 : {clf.predict(last)}")