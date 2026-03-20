# ============================================================
# 23. 가설검정 (F검정, t검정)
# [유형] 3유형 (30점) — 가설검정·통계
# ============================================================
#
# ---------- [시험 환경] 요구사항 ----------
# 데이터: 암 환자(1) vs 정상인(2) 리지스틴(Resistin) 수치
# 제공: s1.csv (BASE/krdatacertificate/) — Classification, Resistin
# 전처리: 로그 변환 후 두 집단 차이 검정
# 제출: 소수 셋째 자리까지 반올림
#
# ---------- [추출해야 할 내용 / 정답 형식] ----------
# Q1-1: F검정 통계량 (분자 자유도 > 분모, 분자 분산 > 분모 분산) → round(값, 3)
# Q1-2: 합동 분산 추정량 → round(값, 3)
# Q1-3: 독립표본 t검정 p-value → round(값, 3)
#
# ---------- [학습 목표] ----------
# 나중에 주석 지우고 [기본 제공] + [요구사항]만 보고 연습
# ============================================================
#
# [기본 제공] Step 1~4 | [작성] Step 5~7
# ============================================================

# ---------- [기본 제공] Step 1: import ----------
import pandas as pd
import numpy as np
from scipy import stats

# ---------- [기본 제공] Step 2: BASE URL ----------
BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

# ---------- [기본 제공] Step 3: 데이터 로드 ----------
df = pd.read_csv(f"{BASE}/krdatacertificate/s1.csv")

# ---------- [기본 제공] Step 4: 두 집단 분리 & 로그 변환 ----------
cls_1 = df[df["Classification"] == 1]["Resistin"]
cls_2 = df[df["Classification"] == 2]["Resistin"]
cls_1_log = np.log(cls_1)
cls_2_log = np.log(cls_2)

# ---------- [작성] Step 5: Q1-1 F검정 통계량 ----------
# TODO: 분산 계산 (ddof=1), 분자>분모 조건으로 F = 큰분산/작은분산
# TODO: print("Q1-1:", round(f_stat, 3))

# ---------- [작성] Step 6: Q1-2 합동 분산 ----------
# TODO: var_pooled = ((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2)
# TODO: print("Q1-2:", round(var_pooled, 3))

# ---------- [작성] Step 7: Q1-3 t검정 p-value ----------
# TODO: t_stat, p_value = stats.ttest_ind(cls_1_log, cls_2_log)
# TODO: print("Q1-3:", round(p_value, 3))
