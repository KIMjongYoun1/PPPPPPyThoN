# ============================================================
# 12. 모형 평가 지표 (빅분기·실무)
# ============================================================
#
# [왜 평가 지표가 필요한가]
# 모델을 학습시킨 뒤, "얼마나 잘 맞추는지"를 숫자로 보려면 지표가 필요하다.
# 회귀와 분류는 예측 형태가 다르므로, 쓰는 지표도 다르다.
#
# [회귀 지표 — 예측값과 실제값의 "차이"를 본다]
# - RMSE (Root Mean Squared Error): 오차 제곱의 평균에 루트. 단위가 원래 값과 같음. 작을수록 좋음.
# - MAE (Mean Absolute Error): 오차 절댓값의 평균. RMSE보다 이상치에 덜 민감. 작을수록 좋음.
# - R2 (결정계수): 0~1. 1에 가까울수록 "실제값을 잘 설명한다" = 좋음. 0에 가까우면 별로.
#
# [분류 지표 — 맞힌 개수·비율을 본다]
# - 정확도(accuracy): 전체 중 맞힌 비율. 클래스가 균형일 때 유용.
# - 정밀도(precision): "양성(1)이라고 예측한 것 중" 실제로 양성인 비율. 거짓 양성 줄일 때 중요.
# - 재현율(recall): "실제 양성인 것 중" 양성으로 맞힌 비율. 놓치면 안 될 때 중요.
# - F1: 정밀도와 재현율의 조화평균. 클래스 불균형(0이 많고 1이 적을 때)일 때 정확도보다 F1을 쓴다.
#
# [혼동 행렬 (confusion_matrix)]
# - TN(True Negative): 실제 0, 예측 0 (맞음)
# - FP(False Positive): 실제 0, 예측 1 (틀림 — 거짓 양성)
# - FN(False Negative): 실제 1, 예측 0 (틀림 — 놓침)
# - TP(True Positive): 실제 1, 예측 1 (맞음)
# - [[TN, FP], [FN, TP]] 순서로 나온다.
#
# [import — 각 함수 역할]
# 회귀:
#   mean_squared_error  → MSE (오차 제곱 평균). RMSE는 이걸 sqrt.
#   mean_absolute_error → MAE (오차 절댓값 평균)
#   r2_score            → R2 결정계수 (1에 가까울수록 좋음)
# 분류:
#   accuracy_score   → 정확도 (전체 맞힌 비율)
#   f1_score        → F1 (정밀도·재현율 조화평균)
#   precision_score → 정밀도 (양성 예측 중 실제 양성 비율)
#   recall_score    → 재현율 (실제 양성 중 맞힌 비율)
#   confusion_matrix → 혼동 행렬 [[TN,FP],[FN,TP]]
# ============================================================

import numpy as np
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score,
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    confusion_matrix,
)

# ---------- 따라 칠 코드 (1): 회귀 — RMSE, MAE, R2 ----------
# → 실제값(y_true)과 예측값(y_pred)의 차이를 RMSE, MAE, R2로 측정.
y_true = np.array([10, 20, 30, 40])
y_pred = np.array([12, 18, 32, 38])
rmse = np.sqrt(mean_squared_error(y_true, y_pred))
mae = mean_absolute_error(y_true, y_pred)
r2 = r2_score(y_true, y_pred)
print(f"RMSE: {rmse:.2f}, MAE: {mae:.2f}, R2: {r2:.2f}")

import numpy as np
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score,
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    confusion_matrix,
)

y_true = np.array([10, 20, 30, 40])
y_pred = np.array([12, 18, 32, 38])
rmse = np.sqrt(mean_squared_error(y_true, y_pred))
mae = mean_absolute_error(y_true, y_pred)
r2 = r2_score(y_true, y_pred)
print(f"RMSE: {rmse:.2f}, MAE: {mae:.2f}, R2: {r2:.2f}")

# ---------- 따라 칠 코드 (2): 분류 — 정확도, F1 ----------
# → 전체 맞힌 비율(accuracy), 정밀도·재현율 조화평균(F1).

import numpy as np
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score,
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    confusion_matrix,
)
y_true_c = [1, 0, 1, 1, 0]
y_pred_c = [1, 0, 0, 1, 0]
acc = accuracy_score(y_true_c, y_pred_c)
f1 = f1_score(y_true_c, y_pred_c, average="binary")  # 이진 분류
print(f"정확도: {acc:.2f}, F1: {f1:.2f}")

import numpy as np
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score,
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    confusion_matrix,
)
y_true_c = [1, 0, 1, 1, 0]
y_pred_c = [1, 0 ,0, 1, 0]
acc = accuracy_score(y_true_c, y_pred_c)
f1 = f1_score(y_true_c, y_pred_c, average="binary")
print(f"정확도 : {acc:.2f}, F1 : {f1:.2f}")

# ---------- 따라 칠 코드 (3): 정밀도, 재현율 ----------
# → 정밀도 = "1이라고 예측한 것 중" 실제 1인 비율. 재현율 = "실제 1인 것 중" 1로 맞힌 비율.
prec = precision_score(y_true_c, y_pred_c, zero_division=0)
rec = recall_score(y_true_c, y_pred_c, zero_division=0)
print(f"정밀도: {prec:.2f}, 재현율: {rec:.2f}")

prec = precision_score(y_true_c, y_pred_c, zero_division=0)
rec = recall_score(y_true_c, y_pred_c, zero_division=0)
print(f"정밀도 :{prec:.2f}, 재현율 : {rec:.2f}")

# ---------- 따라 칠 코드 (4): 혼동 행렬 ----------
# → [[TN, FP], [FN, TP]]. TN=실제0예측0, FP=실제0예측1, FN=실제1예측0, TP=실제1예측1.
cm = confusion_matrix(y_true_c, y_pred_c)
print("Confusion matrix:\n", cm)

cm = confusion_matrix(y_true_c, y_pred_c)
print(f"혼동 행렬 confusion_matrix: \n{cm}")

# ---------- 예제 ----------
# y_true = [1,1,0,0], y_pred = [1,0,0,1] 일 때 정확도, F1, confusion_matrix를 출력하세요.

from sklearn.metrics import (
    accuracy_score,
    f1_score,
    confusion_matrix,
)

yt = [1, 1, 0, 0]
yp = [1, 0, 0, 1]
print(accuracy_score(yt, yp))
print(f1_score(yt, yp, average="binary"))
print(confusion_matrix(yt, yp))


from sklearn.metrics import (
    accuracy_score,
    f1_score,
    confusion_matrix,
)
yt = [1, 1, 0, 0]
yp = [1, 0, 0, 1]
print("accuracy_score", yt, yp)
print(accuracy_score(yt, yp))
print("f1_score", yt, yp)
print(f1_score(yt, yp, average="binary"))  
print("confusion_matrix", yt, yp) 
print(confusion_matrix(yt, yp))
