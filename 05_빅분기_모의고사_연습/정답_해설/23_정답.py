# ============================================================
# 23. 가설검정 F검정, t검정 (정답)
# ============================================================

import pandas as pd
import numpy as np
from scipy import stats

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
df = pd.read_csv(f"{BASE}/krdatacertificate/s1.csv")

cls_1 = df[df["Classification"] == 1]["Resistin"]
cls_2 = df[df["Classification"] == 2]["Resistin"]
cls_1_log = np.log(cls_1)
cls_2_log = np.log(cls_2)

# Q1-1: F검정 통계량 (분자 분산 > 분모 분산)
cls_1_var = np.var(cls_1_log, ddof=1)
cls_2_var = np.var(cls_2_log, ddof=1)
f_stat = cls_1_var / cls_2_var if cls_1_var > cls_2_var else cls_2_var / cls_1_var
print("Q1-1:", round(f_stat, 3))

# Q1-2: 합동 분산
n1, n2 = len(cls_1), len(cls_2)
var_pooled = ((n1 - 1) * cls_1_var + (n2 - 1) * cls_2_var) / (n1 + n2 - 2)
print("Q1-2:", round(var_pooled, 3))

# Q1-3: t검정 p-value
t_stat, p_value = stats.ttest_ind(cls_1_log, cls_2_log)
print("Q1-3:", round(p_value, 3))
