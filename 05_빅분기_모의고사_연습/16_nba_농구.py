# ╔══════════════════════════════════════════════════════════════╗
# ║  [1유형-집계] 16. NBA 농구 통계 Q1~Q10                         ║
# ╚══════════════════════════════════════════════════════════════╝
# ★ ⚠️ 구분자 sep=";" + 인코딩 encoding="latin-1" → read_csv에 명시
#   ※ 지문 판단법: "Q1. ~를 구하시오" 형태로 질문 여러 개 나열 → 1유형
#                  "예측하시오" 없음, submission 제출 없음 → print()로 출력
#                  import: pandas만
#
# [1유형 핵심 패턴]
#   그룹집계: groupby("열")["열"].mean/sum() → sort_values → head(N)
#   행 개수:  groupby().size() / .value_counts()
#   최대팀:   groupby().mean/sum().idxmax()
#   상위N명:  .nlargest(N, "열") / sort_values().head(N)
#   필터:     df[df["열"] >= 값] / df.loc[조건, "열"]


# ═══ import + 로드
# import pandas as pd
# BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
# df = pd.read_csv(f"{BASE}/nba/nba.csv", encoding="latin-1", sep=";")


# ═══ Q1: 팀별 평균 PTS 상위 5팀
# groupby("Tm")["PTS"].mean() → sort_values(False) → head(5)
# q1 = df.groupby("Tm")["PTS"].mean().sort_values(ascending=False).head(5)
# print("Q1:", q1)


# ═══ Q2: 포지션별 선수 수 (많은 순)
# groupby().size() = 그룹별 행 개수
# q2 = df.groupby("Pos").size().sort_values(ascending=False)
# print("Q2:", q2)


# ═══ Q3: PTS 상위 10명 Player와 PTS
# .nlargest(N, "열") → 빠르게 상위N 추출
# q3 = df.nlargest(10, "PTS")[["Player", "PTS"]]
# print("Q3:", q3)


# ═══ Q4: 팀별 Age 평균 가장 높은 팀명
# groupby().mean().idxmax() → 최대값의 인덱스(=팀명) 반환
# q4 = df.groupby("Tm")["Age"].mean().idxmax()
# print("Q4:", q4)


# ═══ Q5: MP >= 30 선수 명수
# (조건).sum() = True 개수
# q5 = (df["MP"] >= 30).sum()
# print("Q5:", q5)


# ═══ Q6: 팀별 AST 합 최대 팀명
# q6 = df.groupby("Tm")["AST"].sum().idxmax()
# print("Q6:", q6)


# ═══ Q7: STL 평균 상위 5명
# q7 = df.groupby("Player")["STL"].mean().nlargest(5).index.tolist()
# print("Q7:", q7)


# ═══ Q8: G >= 80인 선수만 PTS 평균
# 조건 필터 먼저 → 집계
# q8 = df.loc[df["G"] >= 80, "PTS"].mean()
# print("Q8:", q8)


# ═══ Q9: eFG% >= 0.55 선수 수
# q9 = (df["eFG%"] >= 0.55).sum()
# print("Q9:", q9)


# ═══ Q10: 각 팀에서 PTS 최대 선수 1명씩
# groupby().idxmax() → 인덱스 목록 → df.loc[...]
# q10 = df.loc[df.groupby("Tm")["PTS"].idxmax()][["Tm", "Player", "PTS"]]
# print("Q10:", q10)
