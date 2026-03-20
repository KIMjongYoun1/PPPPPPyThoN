# ============================================================
# 19. WorldCup 월드컵 Q21~Q30 (정답)
# ============================================================

import pandas as pd

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
df = pd.read_csv(f"{BASE}/worldcup/worldcupgoals.csv")

# Q23용: Years 4자리 체크
df["yearLst"] = df.Years.str.split("-")

def checkFour(x):
    for value in x:
        if len(str(value)) != 4:
            return False
    return True

df["check"] = df["yearLst"].apply(checkFour)

# Q21: 나라별 골득점 상위 5
q21 = df.groupby("Country").sum().sort_values("Goals", ascending=False).head(5)
print("Q21:", q21)

# Q22: 골득점 선수 가장 많은 나라 상위 5
q22 = df.groupby("Country").size().sort_values(ascending=False).head(5)
print("Q22:", q22)

# Q23: Years 4자리 아닌 케이스 건수
q23 = len(df[df.check == False])
print("Q23:", q23)

# Q24: df2 (예외 제외) 행 수
df2 = df[df.check == True].reset_index(drop=True)
q24 = df2.shape[0]
print("Q24:", q24)

# Q25: LenCup 추가, 4회 출전 선수 수
df2["LenCup"] = df2["yearLst"].str.len()
q25 = df2["LenCup"].value_counts()[4]
print("Q25:", q25)

# Q26: Yugoslavia 2회 출전 선수 수
q26 = len(df2[(df2.LenCup == 2) & (df2.Country == "Yugoslavia")])
print("Q26:", q26)

# Q27: 2002년 출전 선수 수
q27 = len(df2[df2.Years.str.contains("2002")])
print("Q27:", q27)

# Q28: 이름에 'carlos' 포함 (대소문자 무시)
q28 = len(df2[df2.Player.str.lower().str.contains("carlos")])
print("Q28:", q28)

# Q29: 출전 1회 선수 중 최다 득점
q29 = df2[df2.LenCup == 1].sort_values("Goals", ascending=False).Player.values[0]
print("Q29:", q29)

# Q30: 출전 1회 선수 가장 많은 국가
q30 = df2[df2.LenCup == 1].Country.value_counts().index[0]
print("Q30:", q30)
