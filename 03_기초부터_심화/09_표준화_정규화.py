# ============================================================
# 09. 표준화·정규화 (스케일링) — 빅분기·실무
# ============================================================
#
# [교수님 말] 스케일링이 왜 필요한가
# - 모델에 넣는 변수마다 숫자 크기가 다르면(예: 나이 20~60, 소득 수백만), 거리·가중치를 쓰는
#   알고리즘은 "큰 숫자" 쪽에 더 민감하게 반응한다. 그러면 나이 같은 작은 범위 변수의 영향이 작아진다.
# - "스케일링"은 변수별로 비슷한 범위로 맞춰서, 모델이 각 변수를 공평하게(또는 균형 있게) 쓰게 하는 전처리다.
#
# [표준화 StandardScaler]
# - 각 열(변수)마다 (값 - 그 열 평균) / 그 열 표준편차 로 바꾼다.
# - 바꾼 뒤에는 그 열의 평균이 0에 가깝고, 표준편차가 1에 가깝게 된다.
# - 이상치(아주 큰 값)가 있으면 평균·표준편차가 끌려가서 표준화 결과도 민감해질 수 있다.
#
# [정규화 MinMaxScaler]
# - 각 열마다 (값 - 최소) / (최대 - 최소) 로 바꾼다.
# - 그 열 안에서 최솟값은 0, 최댓값은 1이 되고, 그 사이는 0~1 사이로 선형으로 배치된다.
# - 최소·최대가 극단값에 끌려가면 전체 구간이 넓어질 수 있어서, 이상치에 더 민감할 수 있다.
#
# [fit 과 transform]
# - fit: 학습 데이터로 "평균·표준편차" 또는 "최소·최대"를 구해 둔다. = 스케일 기준을 정한다.
# - transform: 그 기준으로 값을 바꾼다. 테스트 데이터는 반드시 학습에서 구한 기준으로만 transform 한다.
# - fit_transform: fit 한 다음 바로 transform. 학습용 데이터에 주로 쓴다.
#
# [테스트로 fit 하면 안 되는 이유]
# - 테스트는 "알고 싶은 미래/새 데이터"를 가정한다. 테스트로 평균·최소·최대를 구해서 맞추면,
#   시험에 답을 미리 본 것처럼 기준이 새 데이터에 맞춰져 버린다. = 정보 누수.
# - 실전에서는 train으로만 fit 하고, test·제출 데이터는 train 기준으로 transform 만 한다.
#
# [용어 정리]
# - StandardScaler: 표준화 전용 도구. sklearn이 평균·표준편차를 내부에 저장해 둔다.
# - MinMaxScaler: 0~1 정규화 전용. 최소·최대를 내부에 저장해 둔다.
#
# ===================== 표준화·정규화 한눈에 정리 =====================
#
# 1) 왜 하나?
#    - 변수마다 숫자 크기가 다르면 모델이 큰 숫자 쪽만 반응함. 스케일링으로 범위를 맞춰서 공평하게 씀.
#
# 2) 표준화 vs 정규화
#    - 표준화(StandardScaler): (값 - 평균) / 표준편차 → 평균 0, 표준편차 1. "평균에서 표준편차 몇 배 떨어졌나".
#    - 정규화(MinMaxScaler): (값 - 최소) / (최대 - 최소) → 0~1. "구간 안에서 어디쯤인가".
#
# 3) fit / transform
#    - fit: 데이터를 보고 "기준"(평균·표준편차 또는 최소·최대)을 정해서 scaler 안에 저장.
#    - transform: 그 기준으로 값만 바꿈.
#    - fit_transform: fit + transform 한 번에. 학습용 데이터에만.
#
# 4) train만 fit, test는 transform만
#    - 기준은 train으로만 정함. test·새 데이터는 그 기준으로 transform만 함.
#    - test로 fit 하면 "미래 정보로 기준을 바꾼 것" = 정보 누수.
#
# 5) 스케일된 값의 의미·용도
#    - 의미: 원래 단위가 아니라 "기준 대비 상대적 위치"로 통일된 숫자.
#    - 용도: 회귀·분류·클러스터링 등 모델에 넣을 "전처리된 입력"으로 사용.
#
# 6) 언제 뭘 쓸까
#    - StandardScaler: 일반적으로 많이 씀. 이상치 많으면 RobustScaler 고려.
#    - MinMaxScaler: 0~1이 꼭 필요할 때(신경망 입력 등). 이상치에 민감.
#
# 7) import — 각 모듈 역할
#    numpy (np): 배열, mean, std 등 수치 연산.
#    StandardScaler: 표준화 (평균 0, 표준편차 1). fit, transform, fit_transform.
#    MinMaxScaler: 0~1 정규화. fit, transform, fit_transform.
#    train_test_split: 데이터를 train/test로 나눔.
#
# 8) 실전 코드 패턴
#    scaler = StandardScaler()
#    scaler.fit(X_train)              # 기준은 train으로만
#    X_train_s = scaler.transform(X_train)
#    X_test_s = scaler.transform(X_test)   # test는 transform만
#
# ====================================================================
#
# ---------- 따라칠 때 보는 요약 (뭘 하는지만 먼저 보기) ----------
# (1) StandardScaler 맛보기: 데이터 한 덩어리(X)를 fit_transform → 평균 0, 표준편차 1에 가깝게 만든다.
# (2) 새 데이터는 transform만: X로 fit 해 둔 뒤, 나중에 들어온 new는 fit 안 하고 transform만 한다.
# (2-보충) train/test 나눴을 때: train으로만 fit, test는 transform만. (2)를 train·test 버전으로 쓴 것.
# (3) MinMaxScaler: 같은 데이터를 0~1 구간으로 눌러 넣는다. fit_transform 한 번에.
# (4) 실전 패턴: DataFrame으로 train/test 나누고, train만 fit → train/test 둘 다 transform (test는 fit 없음).
# 마지막 예제: MinMax로 [1,2,3,4,5] 학습한 뒤, 10을 넣으면? (직접 실행해 보기)
# ---------- ----------------------------------------------------
# ============================================================

import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# ---------- 따라 칠 코드 (1): StandardScaler ----------
# → 한 덩어리 데이터를 "표준화"(평균0, 표준편차1) 한 번에 하기. fit_transform 쓰면 fit+transform 동시.

X = [[10], [20], [30], [40], [50]]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("표준화 후 평균:", X_scaled.mean(axis=0))
print("표준화 후 표준편차:", X_scaled.std(axis=0))

import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

X = [[10], [20], [30], [40], [50]]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(f"표준화 후 평균: {X_scaled.mean(axis=0)}")
print(f"표준화 후 표준 편차: {X_scaled.std(axis=0)}")
print(X_scaled)

# ---------- 따라 칠 코드 (2): 새 데이터는 transform만 (fit 하지 않음) ----------
# → X로 "기준" 잡고(fit), 새 데이터 new는 그 기준으로만 변환(transform). new로 fit 하면 안 됨.
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

X = [[10], [20], [30], [40], [50]]
scaler = StandardScaler()
scaler.fit(X)   # X 기준으로 평균·표준편차 학습 (필수)
new = [[25], [35]]
new_scaled = scaler.transform(new)
print("새 데이터 변환:", new_scaled)

# ---------- (2-보충) train만 fit · test는 transform만 (한 덩어리씩 소스로) ----------
# → (2)를 train/test 나눈 버전. fit(X_tr) 한 번만, X_te는 transform만.
# ↓ 이 블록만 골라 실행할 때도 되게 import 를 여기서 다시 넣음 (위에서 안 돌렸으면 NameError 남)
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_all = np.array([[10], [20], [30], [40], [50], [15], [45]])  # 2D array 권장 (한 블록만 실행해도 동작)
X_tr, X_te = train_test_split(X_all, test_size=0.3, random_state=0)
scaler_split = StandardScaler()
scaler_split.fit(X_tr)                    # ★ fit 은 train 으로만
X_tr_scaled = scaler_split.transform(X_tr)   # train 변환 (transform 한 줄로도 가능)
X_te_scaled = scaler_split.transform(X_te)   # ★ test 는 transform 만 (fit 없음)
print("(2-보충) train 스케일:", X_tr_scaled.flatten())
print("(2-보충) test 스케일 (train 기준):", X_te_scaled.flatten())

# ---------- 따라 칠 코드 (3): MinMaxScaler (0~1) ----------
# → 데이터를 "최소=0, 최대=1" 구간으로 눌러 넣기. fit_transform 한 번에.
mm = MinMaxScaler()
X_mm = mm.fit_transform(X)
print("MinMax 결과:", X_mm.flatten())

mm = MinMaxScaler()
X_mm = mm.fit_transform(X)
print(f"MIN MAX 결과 : {X_mm.flatten()}")


# ---------- 따라 칠 코드 (4): train만 fit, test는 transform만 (소스로 보기) ----------
# → DataFrame으로 train/test 나눈 뒤, scaler.fit( train ) → train/test 둘 다 transform (test는 fit 없음).
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.DataFrame({
    "나이": [25, 35, 45, 55],
    "소득": [3000, 5000, 4000, 6000],  # 만원 단위
})
# 1) 데이터를 train / test 로 나눔
X_train, X_test = train_test_split(df, test_size=0.5, random_state=42)

scaler2 = StandardScaler()
# 2) ★ fit 은 "학습용(train)" 데이터로만. 여기서 평균·표준편차가 scaler 안에 저장됨.
scaler2.fit(X_train)

# 3) train 변환: 방금 fit으로 구한 기준으로 변환 (fit_transform 한 번에 해도 됨)
X_train_s = scaler2.transform(X_train)

# 4) ★ test 변환: fit 하지 않음. train에서 구한 기준으로 transform 만 함.
X_test_s = scaler2.transform(X_test)

print("Train 스케일:", X_train_s)
print("Test 스케일:", X_test_s)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

df = pd.DataFrame({
    "나이": [25, 35 ,45 ,55],
    "소득": [3000, 5000, 4000, 6000],
})

X_train, X_test = train_test_split(df, test_size = 0.5, random_state = 42)
scaler3 = StandardScaler()
scaler3.fit(X_train)
X_train_s = scaler3.transform(X_train)
X_test_s = scaler3.transform(X_test)

print(f"Train 스케일 : {X_train_s}")
print(f"Test 스케일 : {X_test_s}")

# ---------- 예제 ----------
# [1, 2, 3, 4, 5] 를 MinMaxScaler로 변환한 뒤, 값 10을 같은 scaler로 transform 하면 얼마나 나올까? (직접 실행해 보기)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd



data = [[1], [2], [3], [4], [5]]
m = MinMaxScaler()
m.fit(data)
print("10 변환:", m.transform([[10]]))
