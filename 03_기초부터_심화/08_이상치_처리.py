# ============================================================
# 08. 이상치 처리 (빅분기·실무)
# ============================================================
#
# [교수님 말] 이상치란
# - "나머지 데이터와 비슷한 패턴에서 많이 벗어난 값"을 이상치(outlier)라고 부른다.
# - 수집 오류(입력 실수, 센서 고장), 특수 케이스(연봉 1억인 CEO 한 명) 때문에 생긴다.
# - 그대로 두면 평균·표준편차가 왜곡되고, 회귀·분류 모형도 한쪽으로 끌려 가서 성능이 나빠진다.
# - 그래서 "찾아서 제거"하거나, "경계 밖이면 경계값으로 자르는 캡핑", "평균/중앙값으로 대치" 같은 전처리를 한다.
#
# [IQR 방법] — 구간으로 이상치 판별
# - 데이터를 작은 순으로 늘어놓았을 때, 1/4 지점 값 = 1사분위수(Q1), 3/4 지점 값 = 3사분위수(Q3).
# - IQR = Q3 - Q1 (가운데 50% 구간의 폭). 이 폭의 1.5배를 Q1 아래·Q3 위로 넓혀서 "정상 범위"로 본다.
# - 즉 "Q1 - 1.5*IQR 보다 작은 값" 또는 "Q3 + 1.5*IQR 보다 큰 값"을 이상치로 본다.
# - 예: 점수들이 대부분 60~90인데 10, 100 이 있으면 IQR로 10·100이 이상치로 잡힐 수 있다.
#
# [Z-score 방법] — 평균에서 얼마나 멀리 떨어졌는지
# - 각 값에 대해 (값 - 평균) / 표준편차 를 계산한 게 Z-score다. "평균으로부터 표준편차 몇 배만큼 떨어졌나"를 나타낸다.
# - 보통 -2 ~ 2 안에 있으면 정상, 그 밖이면 이상치로 보는 경우가 많다. (절대값 2 초과면 이상치)
#
# [캡핑] — 제거 대신 "경계로 자른다"
# - 이상치를 지우지 않고, "아래 경계보다 작으면 아래 경계값으로, 위 경계보다 크면 위 경계값으로" 바꾼다.
# - 극단값의 영향은 줄이면서, 데이터 개수는 유지할 수 있다.
#
# [용어 정리]
# - percentile(백분위수): 정렬된 데이터에서 "몇 % 지점"의 값을 구함. np.percentile(data, 25)=25% 지점 값.
# - Q1(1사분위수): 25% 지점 값. Q3(3사분위수): 75% 지점 값.
# - 선형 보간: 두 값 사이가 "직선으로 변한다"고 보고, 그 사이 위치에 해당하는 값을 비율로 채워 넣는 것. 예: 3번째=13, 4번째=14 → 3.5번째=13.5.
# - IQR(Interquartile Range): Q3 - Q1. "가운데 50% 구간의 폭".
# - 경계: IQR로 정한 "정상 범위"의 끝. low = Q1-1.5*IQR, high = Q3+1.5*IQR. 이 밖이면 이상치.
# - Z-score: (값 - 평균) / 표준편차. "평균에서 표준편차 몇 배만큼 떨어졌나". 절대값 2 초과면 이상치로 보는 경우 많음.
# - 캡핑(capping): 이상치를 지우지 않고, 경계 밖이면 경계값으로 잘라 넣는 것. .clip(lower=..., upper=...) 가 이 역할.
#
# [import — 각 모듈 역할]
# numpy (np): percentile(백분위수), mean, std, abs 등 수치 연산.
# pandas (pd): DataFrame, clip(캡핑) 등 표 형태 데이터 처리.
# ============================================================

import numpy as np
import pandas as pd

# ---------- 따라 칠 코드 (1): IQR로 이상치 경계 구하기 ----------
data = [10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 100]  # 100이 이상치
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1
low = q1 - 1.5 * iqr
high = q3 + 1.5 * iqr
print(f"Q1={q1}, Q3={q3}, IQR={iqr}, 경계: [{low}, {high}]")


import numpy as np
import pandas as pd
data = [10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 100]
# percentile: 정렬 후 "몇 % 지점" 값을 구함. 25%·75%는 1~(n-1) 위치 공식 쓰고, 정수 사이면 선형 보간.
q1 = np.percentile(data, 25)   # 25% 지점 값 = 13.5 (Q1)
q3 = np.percentile(data, 75)  # 75% 지점 값 = 18.5 (Q3)
iqr = q3 - q1                  # 가운데 50% 구간의 "폭" = 5.0 (데이터가 얼마나 퍼져 있는지)
low = q1 - 1.5 * iqr           # 정상 범위 "아래 경계" (이보다 작으면 이상치)
high = q3 + 1.5 * iqr          # 정상 범위 "위 경계" (이보다 크면 이상치)

# 의미: 6.0 ~ 26.0 안에 있으면 정상, 밖이면 이상치. → 100은 26보다 크니까 이상치.
print(f"Q1 = {q1}, Q3 = {q3}, IQR = {iqr}, 경계: [{low}, {high}]")




# ---------- 따라 칠 코드 (2): 이상치 여부 판별 ----------
def is_outlier_iqr(arr):
    q1, q3 = np.percentile(arr, [25, 75])
    iqr = q3 - q1
    low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    return (arr < low) | (arr > high)

arr = np.array(data)
mask = is_outlier_iqr(arr)
print("이상치 인덱스:", np.where(mask)[0])
print("이상치 제외:", arr[~mask])

import numpy as np
import pandas as pd
data = [10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 100]
def is_outlier_iqr(arr):
    q1, q3 = np.percentile(arr, [25, 75])
    iqr = q3 - q1
    low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr   # high는 q3 + 1.5*IQR (위쪽 경계)
    return (arr < low) | (arr > high)         # return만. print는 호출하는 쪽에서
arr = np.array(data)
print(is_outlier_iqr(arr))

arr = np.array(data)
print(np.array(data))
mask = is_outlier_iqr(arr)
print("이상치 인덱스:", np.where(mask)[0])
print("이상치 제외:", arr[~mask])


# ---------- 따라 칠 코드 (3): Z-score로 이상치 (절대값 2 초과) ----------
# [함수 설명]
# - np.mean(arr): arr 전체의 평균(하나의 숫자).
# - np.std(arr): 표준편차. 평균에서 얼마나 퍼져 있는지 크기. 0이면 모두 같은 값.
# - arr - mean: 배열 각 요소에서 평균을 뺀 것(브로드캐스트).
# - (arr - mean) / std: Z-score. "평균에서 표준편차 몇 배만큼 떨어졌나". 요소마다 하나.
# - np.abs(...): 절대값. 음수 Z-score도 크기만 보려고.
# - z > threshold: Z 절대값이 threshold(기본 2)보다 크면 True → 이상치로 본다.
# - np.zeros(len(arr), dtype=bool): std==0일 땐 나눌 수 없으므로 "이상치 없음"으로 전부 False인 배열 반환.
def is_outlier_zscore(arr, threshold=2):
    mean, std = np.mean(arr), np.std(arr)  # 평균·표준편차
    if std == 0:
        return np.zeros(len(arr), dtype=bool)  # 같은 값만 있으면 이상치 판단 불가 → 전부 False
    z = np.abs((arr - mean) / std)  # 요소별 Z-score 절대값
    return z > threshold  # 임계값 초과면 True(이상치)

print("Z-score 이상치:", arr[is_outlier_zscore(arr)])

import numpy as np
import pandas as pd

arr = np.array([10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 100])

def is_outlier_zscore(arr, threshold=2):
    mean, std = np.mean(arr), np.std(arr)
    if std == 0:
        return np.zeros(len(arr), dtype=bool)
    z = np.abs((arr - mean) / std)
    return z > threshold

print("Z-score 이상치:", arr[is_outlier_zscore(arr)])

# ---------- 따라 칠 코드 (4): DataFrame 열에서 이상치 캡핑(경계로 자르기) ----------
# 캡핑: 제거 대신 경계 밖 값을 경계값으로 "자르기". .clip(lower=..., upper=...) 사용.
df = pd.DataFrame({"점수": [50, 65, 70, 75, 80, 85, 90, 95, 150]})
q1, q3 = df["점수"].quantile(0.25), df["점수"].quantile(0.75)
iqr = q3 - q1
cap_low, cap_high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
df["점수_캡핑"] = df["점수"].clip(lower=cap_low, upper=cap_high)  # cap_low 미만→cap_low, cap_high 초과→cap_high
print(df)

import numpy as np
import pandas as pd
df = pd.DataFrame({"점수": [50, 65, 70, 75, 80, 85, 90, 95, 150]})
q1, q3 = df["점수"].quantile(0.25), df["점수"].quantile(0.75)
iqr = q3 - q1
cap_low, cap_high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
df["점수_캡핑"] = df["점수"].clip(lower=cap_low, upper=cap_high)
print(q1)
print(q3)
print(cap_low)
print(cap_high)
print(iqr)
print(df)

# ---------- 예제 ----------
# 리스트 [3, 5, 7, 8, 9, 10, 11, 12, 100] 에서 IQR 기준 이상치를 제거한 평균을 구하세요.

import numpy as np
import pandas as pd
def is_outlier_iqrF(arr):
    q1, q3 = np.percentile(arr, [25, 75])
    iqr = q3 -q1
    low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    return (arr <low) | (  arr > high)


values = [3, 5, 7, 8, 9, 10, 11, 12, 100]
v = np.array(values)
out = is_outlier_iqrF(v)
clean = v[~out]
print([~out])
print(out)
print(clean)
print(f"이상치 제거 후 평균: {clean.mean():.2f}")
