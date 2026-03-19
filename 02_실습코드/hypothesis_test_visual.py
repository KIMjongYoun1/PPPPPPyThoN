# -*- coding: utf-8 -*-
"""
가설검정 + 카이제곱: 코드 동작 원리 & 시각화

실행: cd 02_실습코드 && python hypothesis_test_visual.py
필요: pip install matplotlib scipy pandas numpy

=============================================================================
[전체 동작 원리 — 읽는 순서]
=============================================================================
1. Part 1 (t검정)
   - group1, group2: 비교할 두 집단 숫자 배열. (실전에서는 CSV/엑셀에서 열로 읽어옴)
   - stats.ttest_ind(그룹1, 그룹2): 두 집단 평균이 같은지 검정 → t_stat, p_value 반환
   - p_value < 0.05 → "차이 있다", 아니면 "차이 없다" 결론

2. Part 2 (t검정 시각화)
   - matplotlib으로 두 그룹 막대그래프 + 평균 점선, 오른쪽에 평균 막대 + p-value 문구
   - PNG 파일로 저장 (matplotlib 없으면 스킵)

3. Part 3 (카이제곱)
   - row_cat, col_cat: 두 범주형 변수 (각 행이 한 사람의 "범주 값"). 실전에서는 df의 두 열
   - pd.crosstab(행범주, 열범주): 조합별 개수 표(분할표) 만듦
   - stats.chi2_contingency(분할표): 두 변수 연관 있는지 검정 → chi2, p_chi, ...
   - p_chi < 0.05 → "연관 있다", 아니면 "연관 없다"

4. Part 4 (카이제곱 시각화)
   - 분할표를 히트맵 + 막대그래프로 그려서 PNG 저장
=============================================================================

=============================================================================
[가설검정 · 카이제곱 — 원리 설명] (수학 기호 없이 말로만)
=============================================================================

■ 가설검정이란 (쉽게)
  - 먼저 "차이 없다" 또는 "연관 없다"라고 가정해 둔다.
  - p-value = "그 가정이 맞는데도, 지금 같은 결과가 우연히 나올 확률"
  - 이 확률이 작으면 → 우연이라고 보기 어렵다 → 가정을 버리고 "차이 있다" 또는 "연관 있다"고 본다.
  - 이 확률이 크면 → 우연일 수 있다고 본다 → "차이 없다" 또는 "연관 없다"로 본다.
  - 0.05(5퍼센트) = 기준선. p가 0.05보다 작으면 "있다"고 결론 내리는 걸로 정해 둔 것.

■ t검정 원리 (두 집단 평균)
  - 가정: "두 집단 평균이 같다."
  - 두 그룹 숫자를 넣으면, 컴퓨터가 내부적으로 "평균 차이 크기"랑 "데이터가 얼마나 들쭉날쭉한지"를 같이 본다.
  - 그걸 합쳐서 "평균이 같은데 이만큼 차이 날 확률"을 계산한 게 p-value.
  - p가 0.05보다 작으면 → "평균이 같은데 이렇게 나오기 어렵다" → "두 집단 평균은 다르다"고 결론.
  - 필요한 것: 두 집단의 숫자 값들만 있으면 됨. (직장인 소득, 자영업 소득 같은 식)

■ 카이제곱 원리 (두 범주형 변수)
  - 가정: "두 변수는 서로 무관하다." (한 변수 값이 달라도 다른 변수랑 상관없다)
  - 분할표 = "두 변수 조합별로 몇 명인지" 세어 둔 표. 예: 남자이면서 구매한 사람 몇 명, 여자이면서 미구매 몇 명, ...
  - "무관하면" 조합별 개수가 대충 비슷한 패턴이어야 한다. 컴퓨터가 "무관할 때 이렇게 나와야 하는 개수"를 따로 구해 둔 다음, 실제 개수랑 비교한다.
  - 실제 개수랑 "그렇게 나와야 하는 개수"가 많이 다르면 → "무관하다"고 보기 어렵다 → "두 변수는 연관이 있다"고 결론.
  - 그 "얼마나 다른지"를 하나의 숫자로 만들고, 그걸 다시 "우연히 이만큼 다를 확률"로 바꾼 게 p-value.
  - p가 0.05보다 작으면 → "무관하다" 기각 → "연관 있다"고 결론.
  - 필요한 것: 두 개의 범주형 열 (성별, 구매여부 같은 식). 개수만 있으면 됨.

■ 시험에서 할 일만 기억
  - t검정: 두 그룹 숫자 넣고 ttest_ind 호출 → 나온 p가 0.05보다 작으면 "차이 있다".
  - 카이제곱: 두 범주 열로 crosstab 만들고 chi2_contingency 호출 → 나온 p가 0.05보다 작으면 "연관 있다".
  - 시각화는 시험에 안 나오므로, 원리(말로) + 코드 패턴만 익히면 됨.
=============================================================================
"""

import os
import numpy as np
# SCRIPT_DIR = 이 파이썬 파일이 있는 폴더 경로. 나중에 PNG 저장할 때 같은 폴더에 쓰기 위함.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# =============================================================================
# Part 1: t검정 — 코드 동작 원리 (주석으로 단계별 설명)
# =============================================================================
print("=" * 60)
print("【 t검정: 코드 동작 원리 】")
print("=" * 60)

# [1] 두 집단 데이터 (예: A반 점수 vs B반 점수)
# 동작 원리: np.array(...) = 리스트를 넘파이 배열로 만듦. ttest_ind는 배열을 받음.
# 실전에서는 df[df["직업"]=="직장인"]["소득"] 처럼 CSV/엑셀에서 읽어서 여기 넣음.
group1 = np.array([100, 102, 98, 105, 97])   # A반 5명 점수
group2 = np.array([108, 110, 106, 112, 104])  # B반 5명 점수
# → 평균: group1 약 100.4, group2 약 108. 숫자만 보면 B가 높아 보임.
# → "이 차이가 진짜인가, 우연인가?" 를 t검정이 판단.

# [2] t검정 함수 호출
# 동작 원리: scipy.stats 에서 ttest_ind 함수 가져옴. (두 집단 평균 차이 검정)
# ttest_ind(그룹1, 그룹2) = 두 배열을 넣으면, 내부에서 평균·분산·개수로 t통계량 계산 후
# "평균이 같은데 이만큼 차이 날 확률"을 p_value 로 반환. 반환값은 (t_stat, p_value) 튜플.
from scipy import stats
t_stat, p_value = stats.ttest_ind(group1, group2)
# t_stat = t통계량(차이 크기 반영), p_value = "우연히 이만큼 차이 날 확률"

# [3] p-value 해석
print(f"\n  group1 평균 = {group1.mean():.2f}, group2 평균 = {group2.mean():.2f}")
print(f"  t통계량 = {t_stat:.4f}, p-value = {p_value:.4f}")
if p_value < 0.05:
    print("  → p < 0.05 이므로: 두 집단 평균에 '유의한 차이가 있다' (우연이 아님)")
else:
    print("  → p >= 0.05 이므로: '유의한 차이가 없다' (우연일 수 있음)")

# =============================================================================
# Part 2: t검정 시각화 — 두 집단 값 비교
# 동작 원리: matplotlib 으로 그림 객체(fig) 만들고, 그 위에 막대·선을 그림. 마지막에 PNG 저장.
# =============================================================================
try:
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.rcParams["axes.unicode_minus"] = False  # 마이너스 기호 깨짐 방지

    # fig = 그림 전체, axes = 왼쪽/오른쪽 두 개의 서브플롯. (1행 2열, 가로 10 세로 4 인치)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    # [왼쪽] 두 그룹 값 막대로 비교
    # 동작: ax1 = 첫 번째 칸. np.arange(len(group1)) = [0,1,2,3,4] → 막대 x 위치.
    # bar(x, 높이) = x 위치에 높이만큼 막대 그림. axhline = 수평선(평균선).
    ax1 = axes[0]
    x1 = np.arange(len(group1))
    x2 = np.arange(len(group2)) + len(group1) + 0.5  # group2 막대는 오른쪽에 띄어서
    ax1.bar(x1, group1, color="steelblue", label="group1 (A반)")
    ax1.bar(x2, group2, color="coral", label="group2 (B반)")
    ax1.axhline(group1.mean(), color="steelblue", linestyle="--", alpha=0.8)
    ax1.axhline(group2.mean(), color="coral", linestyle="--", alpha=0.8)
    ax1.set_ylabel("점수")
    ax1.set_title("t검정: 두 집단 값 비교\n(점선 = 평균)")
    ax1.legend()
    ax1.set_xticks([])

    # [오른쪽] 평균만 막대 + p-value 표시
    ax2 = axes[1]
    means = [group1.mean(), group2.mean()]
    colors = ["steelblue", "coral"]
    bars = ax2.bar(["group1\n(A반)", "group2\n(B반)"], means, color=colors)
    ax2.set_ylabel("평균 점수")
    ax2.set_title(f"두 집단 평균 & p-value\np = {p_value:.4f} → {'차이 있음' if p_value < 0.05 else '차이 없음'}")
    for b, m in zip(bars, means):
        ax2.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.5, f"{m:.1f}", ha="center")

    plt.tight_layout()  # 겹치지 않게 레이아웃 조정
    # savefig = 지금까지 그린 fig 를 파일로 저장. SCRIPT_DIR 에 hypothesis_t_test.png 로 저장.
    plt.savefig(os.path.join(SCRIPT_DIR, "hypothesis_t_test.png"), dpi=100, bbox_inches="tight")
    print("\n  [시각화 저장] hypothesis_t_test.png")
    plt.close()
except Exception as e:
    print("  t검정 시각화 스킵:", e)

# =============================================================================
# Part 3: 카이제곱 — 코드 동작 원리
# =============================================================================
print("\n" + "=" * 60)
print("【 카이제곱: 코드 동작 원리 】")
print("=" * 60)

# [1] 두 범주형 변수
# 동작 원리: 한 행 = 한 사람. row_cat[i], col_cat[i] 가 i번째 사람의 "행 범주", "열 범주".
# 실전에서는 row_cat = df["성별"], col_cat = df["구매여부"] 처럼 DataFrame 열로 넣음.
row_cat = np.array([1, 1, 0, 0, 1, 0, 1, 0])   # 예: 남0 여1
col_cat = np.array([1, 0, 1, 0, 1, 1, 0, 0])   # 예: 미구매0 구매1

# [2] 분할표(교차표)
# 동작 원리: crosstab(행에쓸범주, 열에쓸범주) = (행범주, 열범주) 조합별로 "몇 명인지" 세서 표로 만듦.
# 예: (0,0) 인 사람 수, (0,1) 인 사람 수, (1,0), (1,1) → 2x2 표.
import pandas as pd
tab = pd.crosstab(row_cat, col_cat)
print("\n  분할표 (조합별 개수):")
print(tab)

# [3] 카이제곱 검정
# 동작 원리: chi2_contingency(분할표) = "두 변수가 서로 독립인가?" 검정.
# 독립이면 조합별 개수가 "기대도수"와 비슷해야 함. 차이가 크면 연관 있다고 봄.
# 반환: chi2(통계량), p_chi(p-value), dof(자유도), expected(기대도수 표).
chi2, p_chi, dof, expected = stats.chi2_contingency(tab)

print(f"\n  chi2 = {chi2:.4f}, p-value = {p_chi:.4f}")
if p_chi < 0.05:
    print("  → p < 0.05: 두 변수는 '연관이 있다' (독립 아님)")
else:
    print("  → p >= 0.05: 두 변수는 '독립이다' (연관 없음)")

# =============================================================================
# Part 4: 카이제곱 시각화 — 분할표를 막대/히트맵으로
# 동작 원리: tab.values = 분할표의 숫자만 있는 2차원 배열. imshow = 숫자 크기를 색으로 표시(히트맵).
# =============================================================================
try:
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    # [왼쪽] 분할표 히트맵: tab.values = (행,열) 셀 값. cmap="Blues" = 작은 값 연한 파랑, 큰 값 진한 파랑.
    ax1 = axes[0]
    im = ax1.imshow(tab.values, cmap="Blues")
    ax1.set_xticks(range(tab.shape[1]))
    ax1.set_yticks(range(tab.shape[0]))
    ax1.set_xticklabels(tab.columns.tolist())
    ax1.set_yticklabels(tab.index.tolist())
    ax1.set_xlabel("열 범주")
    ax1.set_ylabel("행 범주")
    ax1.set_title("카이제곱: 분할표(교차표)\n숫자 = 조합별 개수")
    for i in range(tab.shape[0]):
        for j in range(tab.shape[1]):
            ax1.text(j, i, int(tab.values[i, j]), ha="center", va="center")

    # [오른쪽] 막대 그래프 (범주별 개수)
    ax2 = axes[1]
    tab.plot(kind="bar", ax=ax2, color=["steelblue", "coral"])
    ax2.set_title(f"범주별 개수 & p-value\np = {p_chi:.4f} → {'연관 있음' if p_chi < 0.05 else '연관 없음'}")
    ax2.set_ylabel("개수")
    ax2.legend(title="열 범주")

    plt.tight_layout()
    plt.savefig(os.path.join(SCRIPT_DIR, "hypothesis_chi2.png"), dpi=100, bbox_inches="tight")
    print("\n  [시각화 저장] hypothesis_chi2.png")
    plt.close()
except Exception as e:
    print("  카이제곱 시각화 스킵:", e)

print("\n=== 가설검정 시각화 끝 ===")
