# ╔══════════════════════════════════════════════════════════════╗
# ║  [1유형-집계] 19. WorldCup 월드컵 Q21~Q30                      ║
# ╚══════════════════════════════════════════════════════════════╝
# ★ 열: Player, Goals, Years, Country
# ★ Years 처리 핵심: str.split("-") → 리스트 길이 = 출전 횟수
#   ※ 지문 판단법: "Q1. ~를 구하시오" 형태로 질문 여러 개 나열 → 1유형
#                  "예측하시오" 없음, submission 제출 없음 → print()로 출력
#                  import: pandas만
#
# [문자열 처리 암기]
#   str.split("구분자")  → 리스트로 분리
#   str.len()           → 리스트 길이 (출전 횟수)
#   str.contains("문자", case=False) → 포함 여부 (대소문자 무시)
#   str.lower()         → 소문자 변환


# ═══ import + 로드
# import pandas as pd
# BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
# df = pd.read_csv(f"{BASE}/worldcup/worldcupgoals.csv")


# ═══ 전처리: Years 유효성 검사 (4자리 연도만 유효)
# df["yearLst"] = df.Years.str.split("-")
# def checkFour(x):
#     for value in x:
#         if len(str(value)) != 4:
#             return False
#     return True
# df["check"] = df["yearLst"].apply(checkFour)


# ═══ Q21: 나라별 골 합 상위 5
# q21 = df.groupby("Country").sum().sort_values("Goals", ascending=False).head(5)
# print("Q21:", q21)


# ═══ Q22: 골 넣은 선수 가장 많은 나라 상위 5
# q22 = df.groupby("Country").size().sort_values(ascending=False).head(5)
# print("Q22:", q22)


# ═══ Q23: Years 4자리 아닌 케이스 수
# q23 = len(df[df.check == False])
# print("Q23:", q23)


# ═══ Q24: 유효한 행(4자리만) 수
# df2 = df[df.check == True].reset_index(drop=True)
# q24 = df2.shape[0]
# print("Q24:", q24)


# ═══ Q25: LenCup(출전횟수) 추가 후 4회 출전 선수 수
# df2["LenCup"] = df2["yearLst"].str.len()
# q25 = df2["LenCup"].value_counts()[4]
# print("Q25:", q25)


# ═══ Q26: Yugoslavia 2회 출전 선수 수
# q26 = len(df2[(df2.LenCup == 2) & (df2.Country == "Yugoslavia")])
# print("Q26:", q26)


# ═══ Q27: 2002년 출전 선수 수
# q27 = len(df2[df2.Years.str.contains("2002")])
# print("Q27:", q27)


# ═══ Q28: 이름에 'carlos' 포함 선수 수 (대소문자 무시)
# q28 = len(df2[df2.Player.str.lower().str.contains("carlos")])
# print("Q28:", q28)


# ═══ Q29: 출전 1회 선수 중 최다 득점 선수
# q29 = df2[df2.LenCup == 1].sort_values("Goals", ascending=False).Player.values[0]
# print("Q29:", q29)


# ═══ Q30: 출전 1회 선수 가장 많은 국가
# q30 = df2[df2.LenCup == 1].Country.value_counts().index[0]
# print("Q30:", q30)
