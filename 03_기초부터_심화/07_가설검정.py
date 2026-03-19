# ============================================================
# 07. 가설검정 — t검정 & 카이제곱 (심화)
# ============================================================
#
# [교수님 말]
# 가설검정은 "차이가 있는지", "연관이 있는지"를 숫자로 판단하는 방법이야.
# 먼저 "차이 없다 / 연관 없다"라고 가정하고, p-value = "그 가정이 맞는데도 지금처럼 나올 확률"을 구해.
# 이 확률이 0.05보다 작으면 → 우연이라고 보기 어렵다 → "차이 있다 / 연관 있다"고 결론.
# 0.05보다 크면 → 우연일 수 있다 → "차이 없다 / 연관 없다"로 본다.
#
# t검정: 두 집단의 "숫자 값" 평균이 같은지 비교. (예: A반 점수 vs B반 점수)
# 카이제곱: 두 "범주형" 변수가 서로 연관 있는지. (예: 성별 vs 구매여부)
# 자세한 원리 설명은 02_실습코드/hypothesis_test_visual.py 상단 docstring 참고.
#
# [import — 각 모듈 역할]
# scipy.stats: 통계 검정. ttest_ind(두 집단 평균 비교), chi2_contingency(카이제곱, 범주형 연관).
# pandas (pd): 표 형태 데이터. crosstab(분할표 만들기) 등.
# numpy (np): 배열·수치 연산. array, mean 등.
# ============================================================

from scipy import stats
import pandas as pd
import numpy as np

# ---------- 따라 칠 코드 (1): t검정 — 두 집단 평균 비교 ----------
group1 = np.array([100, 102, 98, 105, 97])   # A반
group2 = np.array([108, 110, 106, 112, 104]) # B반

t_stat, p_value = stats.ttest_ind(group1, group2)
print(f"t검정 p-value: {p_value:.4f}")
if p_value < 0.05:
    print("결론: 두 집단 평균에 차이가 있다 (유의함)")
else:
    print("결론: 두 집단 평균에 유의한 차이가 없다")


from scipy import stats
import pandas as pd
import numpy as np

group1 = np.array([100, 102, 98, 105, 101])
group2 = np.array([108, 110, 106, 99, 88])
agg1 = group1.mean()
agg2 = group2.mean()
print(f"group1 평균: {agg1:.2f}")
print(f"group2 평균: {agg2:.2f}")

t_stat, p_value = stats.ttest_ind(group1, group2)
print(f"검정 p_value: {p_value:.4}")
print(t_stat)
if p_value < 0.05:
    print("결론 : 두집단은 차이가 있다 (유의함)")
else:
    print("결론 : 두집단은 차이가 없다")


# ---------- 따라 칠 코드 (2): 카이제곱 — 두 범주형 변수 연관 ----------
# 예: 성별(남/여) vs 구매(예/아니오)
row_cat = ["남", "남", "여", "여", "남", "여", "남", "여"]
col_cat = ["예", "아니오", "예", "예", "아니오", "아니오", "예", "예"]

table = pd.crosstab(row_cat, col_cat)
print("분할표:")
print(table)

chi2, p_chi, dof, expected = stats.chi2_contingency(table)
print(f"카이제곱 p-value: {p_chi:.4f}")
if p_chi < 0.05:
    print("결론: 두 변수는 연관이 있다 (유의함)")
else:
    print("결론: 두 변수는 유의한 연관이 없다")

from scipy import stats
import pandas as pd
import numpy as np
row_cat = ["남", "남", "여","여", "남", "여","남", "여"]
col_cat = ["예", "아니오", "예", "예", "아니오", "아니오", "예", "예"]
table = pd.crosstab(row_cat, col_cat)
print("분할표:")
print(table)

chi2, p_chi, dof, expected = stats.chi2_contingency(table)
# 결론에 필요한 건 p-value 뿐. chi2, dof, expected 는 참고용이라 출력 안 함.
print(f"카이제곱 p-value: {p_chi:.4f}")
if p_chi < 0.05:
    print("결론: 두 변수는 연관이 있다 (유의함)")
else:
    print("결론: 두 변수는 유의한 연관이 없다")

# ---------- 예제 (직접 풀기) ----------
# (1) t검정: 아래 두 그룹 점수에 유의한 차이가 있는지 판단하세요.
#    ttest_ind 호출 → p-value 출력 → 0.05 기준으로 "차이 있다" / "차이 없다" 출력
scores_a = [70, 72, 75, 78, 80]
scores_b = [72, 74, 76, 78, 80]
# 여기에 코드 작성
t_stats, p_value = stats.ttest_ind(scores_a, scores_b)
print(f"p_value: {p_value:.4f}")

if p_value < 0.05:
    print("결롱 두 그룹은 차이가 있다")
else:
    print("결롱 두그룹은 차이가 없음")

# (2) 카이제곱: 성별=["남","남","여","여"], 구매=["예","아니오","예","아니오"] 로
#    crosstab 만든 뒤 chi2_contingency 호출하고, p-value 0.05 기준으로 결론 출력하세요.
# 여기에 코드 작성

col1_cat = ["남", "여", "여", "남", "여", "여", "남"]   # 7명
col2_cat = ["아니오", "예", "예", "예", "아니오", "아니오", "예"]  # 7명으로 맞춤 (한 사람당 한 쌍)

table = pd.crosstab(col1_cat, col2_cat)

chi2, p_chi, dof, expected = stats.chi2_contingency(table)
if p_chi < 0.05:
    print("결론: 두 변수는 연관이 있다 (유의함)")
else:
    print("결론: 두 변수는 유의한 연관이 없다")

# ---------- 풀이 (풀고 나서 확인) ----------
# (1) t, p = stats.ttest_ind(scores_a, scores_b)
#     print(f"p-value: {p:.4f}"); print("차이 있다" if p < 0.05 else "차이 없다")
# (2) tab = pd.crosstab(["남","남","여","여"], ["예","아니오","예","아니오"])
#     chi2, p_chi, dof, exp = stats.chi2_contingency(tab)
#     print(f"p-value: {p_chi:.4f}"); print("연관 있다" if p_chi < 0.05 else "연관 없다")
