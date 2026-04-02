# ╔══════════════════════════════════════════════════════════════╗
# ║  [3유형-통계] 23. 가설검정 (F검정, 합동분산, t검정)               ║
# ╚══════════════════════════════════════════════════════════════╝
# ★ sklearn 아님 → numpy / scipy.stats 사용
# ★ 결과: round(값, 3) 출력 (소수 셋째 자리)
#   ※ 지문 판단법: "검정통계량을 구하시오", "유의확률(p값)", "등분산 검정" → 3유형
#                  import: numpy, scipy.stats (sklearn 절대 아님!)
#
# [3유형 핵심 암기]
#   F검정:   큰분산 / 작은분산  (ddof=1 표본분산)
#   합동분산: ((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2)
#   t검정:   scipy.stats.ttest_ind(그룹1, 그룹2) → (t통계량, p값)
#   로그변환: np.log(값)  ← 단위 정규화 목적


# ═══ import + 로드
# import pandas as pd
# import numpy as np
# from scipy import stats
# BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
# df = pd.read_csv(f"{BASE}/krdatacertificate/s1.csv")


# ═══ 집단 분리 + 로그 변환
# cls_1 = df[df["Classification"] == 1]["Resistin"]
# cls_2 = df[df["Classification"] == 2]["Resistin"]
# cls_1_log = np.log(cls_1)
# cls_2_log = np.log(cls_2)


# ═══ Q1-1: F검정 통계량 (큰 분산 / 작은 분산)
# ddof=1 → 표본분산 (시험에서는 항상 ddof=1)
# cls_1_var = np.var(cls_1_log, ddof=1)
# cls_2_var = np.var(cls_2_log, ddof=1)
# f_stat = cls_1_var / cls_2_var if cls_1_var > cls_2_var else cls_2_var / cls_1_var
# print("Q1-1:", round(f_stat, 3))


# ═══ Q1-2: 합동 분산 (pooled variance)
# n1, n2 = len(cls_1), len(cls_2)
# var_pooled = ((n1 - 1) * cls_1_var + (n2 - 1) * cls_2_var) / (n1 + n2 - 2)
# print("Q1-2:", round(var_pooled, 3))


# ═══ Q1-3: 독립표본 t검정 p-value
# ttest_ind → (t통계량, p값) 반환 → p값만 씀
# t_stat, p_value = stats.ttest_ind(cls_1_log, cls_2_log)
# print("Q1-3:", round(p_value, 3))
