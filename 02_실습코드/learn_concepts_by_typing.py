# -*- coding: utf-8 -*-
"""
[직접 치면서 배우기] 개념 + 메서드 동작 + 시험/실무 대비 심화

Part 1: 기초 (1~8)  →  Part 2: 심화·시험 출제 가능 (9~16)

사용법: 1단계부터 순서대로 "따라 칠 코드"를 직접 타이핑하고 실행해 보며,
       [개념]/[메서드] 설명으로 동작을 이해한다.
같은 폴더에 sample.csv 있으면 파일 읽기·pandas 단계가 동작함.
pandas, numpy, scipy 는 pip install pandas numpy scipy 로 설치.
"""

import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(SCRIPT_DIR, "sample.csv")

# =============================================================================
# === Part 1: 기초 ===
# =============================================================================

# -----------------------------------------------------------------------------
# 1단계: 변수와 f-string
# -----------------------------------------------------------------------------
# [개념] f"문자열 {변수}" = 변수 값을 문자열에 끼워 넣기. 시험에서 출력 형식 지정 시 자주 씀.
# [메서드] print(값) = 콘솔 출력. f"{값:.4f}" = 소수 넷째 자리까지.

# ---------- 따라 칠 코드 ----------
name = "김철수"
age = 25
print(f"제 이름은 {name}이고, 나이는 {age}세입니다.")
acc = 0.87654321
print(f"정확도: {acc:.4f}")   # 0.8765 (시험에서 "소수 넷째 자리까지" 요구 시)
# ----------------------------------
name = "KimjongYoun"
age = 34
print(f"Myname is {name} and Age is {age}")
acc = 0.89762631
print(f"정확도 :  {acc:.4f}")


# -----------------------------------------------------------------------------
# 2단계: 리스트, 인덱스, 슬라이스, len()
# -----------------------------------------------------------------------------
# [개념] 리스트 = 순서 있는 값들의 모음. 인덱스 0부터. 슬라이스 [시작:끝] 에서 끝은 미포함.
# [메서드] len(리스트)=요소 개수. 리스트[1:]=두 번째~끝. 리스트[:3]=처음~인덱스 2까지.

# ---------- 따라 칠 코드 ----------
nums = [10, 20, 30, 40, 50]
print(len(nums), nums[0], nums[1:4], nums[1:])
# ----------------------------------

nums = [10, 20, 30, 40, 50]
print(len(nums), nums[0], nums[2:4], nums[1:])


# -----------------------------------------------------------------------------
# 3단계: for 반복과 append()
# -----------------------------------------------------------------------------
# [개념] for 변수 in 리스트: 로 요소를 하나씩 꺼냄. append(값)=리스트 맨 뒤에 추가.

# ---------- 따라 칠 코드 ----------
numbers = [10, 20, 30]
result = []
for n in numbers:
    result.append(n + 5)
print("result =", result)
# ----------------------------------

numbers = [22, 98, 99]
result = []
for suc in numbers:
    result.append(suc -87)
print("result =", result)

# -----------------------------------------------------------------------------
# 4단계: 리스트 컴프리헌션
# -----------------------------------------------------------------------------
# [개념] [표현식 for 변수 in 반복대상] = 반복 결과를 리스트로 만듦. 조건 넣을 땐 for 뒤에 if.

# ---------- 따라 칠 코드 ----------
doubled = [x * 2 for x in [1, 2, 3]]
evens = [x for x in [1, 2, 3, 4, 5] if x % 2 == 0]
print("doubled =", doubled, ", evens =", evens)
rows_list = [line.strip().split(",") for line in ["a,b,c", "1,2,3"]]
print("rows_list =", rows_list)
# ----------------------------------

doubled = [x * 2 for x in [1, 2, 3]]
evens = [x for x in [1,2,3,4,5] if x % 2 == 0]
print("doubled =", doubled, ", evens = ", evens)
row_list = [line.strip().split(",") for line in ["a,b,c", "1,2,3"]]
print("row_list =", row_list)

# -----------------------------------------------------------------------------
# 5단계: strip(), split()
# -----------------------------------------------------------------------------
# [개념] strip()=앞뒤 공백/줄바꿈 제거. split(구분자)=구분자로 잘라 리스트로. 원본 불변.

# ---------- 따라 칠 코드 ----------
s = "  김철수,25,서울  \n"
cells = s.strip().split(",")
print("cells =", cells)
# ----------------------------------

ss = "    kimJong,34,서울 \n"
cells = s.strip().split(",")
print("cells = ", cells)

# -----------------------------------------------------------------------------
# 6단계: 파일 읽기 (open, readlines)
# -----------------------------------------------------------------------------
# [개념] f.readlines()=한 줄(행)씩 리스트. lines[0]=헤더, lines[1:]=데이터 행.

# ---------- 따라 칠 코드 ----------
with open(CSV_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()
header_list = lines[0].strip().split(",")
rows_list = [line.strip().split(",") for line in lines[1:]]
print("헤더(컬럼 목록):", header_list)
print("행 개수:", len(rows_list))
# 컬럼이 뭔지 하나씩 보고 싶으면:
for i, col in enumerate(header_list):
    print(f"  컬럼 {i}: {col}")

# ---------- N번째 "열(컬럼)" 에 있는 모든 데이터 가져오기 ----------
# 시험에서는 컬럼 개수가 문제마다 다름. len(header_list) 로 총 컬럼 개수 확인.
total_cols = len(header_list)
print(f"  총 컬럼 개수 (header_list 길이): {total_cols}")
# N번째 열 가져올 때: 문제에서 "몇 번째 열" 인지 정해지면 n 번째 → 인덱스는 n-1
n_th = 3
col_idx = n_th - 1
if col_idx < total_cols:
    col_name = header_list[col_idx]
    col_all_values = [row[col_idx] for row in rows_list]  # row 는 for 가 만듦: 각 행마다 row 에 그 행이 들어감
    print(f"  {n_th}번째 컬럼 이름: {col_name}, 그 열의 모든 데이터 (행 {len(col_all_values)}개): {col_all_values}")

    # 그 열에 null(빈 값 등)이 있을 때 채우기 (표준편차 등 구할 때 보통 평균 대치 요구)
    null_set = {"", "null", "NULL", "NA", "nan", "NaN"}

    def is_null(v):
        return v.strip() in null_set or v.strip() == ""

    valid = [v for v in col_all_values if not is_null(v)]
    if valid:
        numeric_vals = []
        for x in valid:
            try:
                numeric_vals.append(float(x))
            except ValueError:
                pass
        if numeric_vals:
            fill_value = sum(numeric_vals) / len(numeric_vals)
            col_filled = []
            for v in col_all_values:  # v = for 가 만드는 변수. 매 반복마다 col_all_values 의 다음 값이 v 에 들어감 (Java 의 for(String v : list) 와 같음)
                if is_null(v):
                    col_filled.append(fill_value)
                else:
                    try:
                        col_filled.append(float(v))
                    except ValueError:
                        col_filled.append(v)
            print(f"  null 을 평균 {fill_value:.2f} 로 채운 결과 (표준편차 등 계산 시 흔히 요구): {col_filled}")
        else:
            fill_value = "0"
            col_filled = [fill_value if is_null(v) else v for v in col_all_values]
            print(f"  null 을 '{fill_value}' 로 채운 결과: {col_filled}")
    else:
        col_filled = col_all_values
        print("  (유효한 값 없음)")
else:
    print(f"  (컬럼이 {n_th}개 미만이라 {n_th}번째 열 없음. 시험에서는 n_th 만 문제 조건에 맞게 바꾸면 됨)")
# ----------------------------------

# -----------------------------------------------------------------------------
# 7단계: def 함수, 여러 값 반환
# -----------------------------------------------------------------------------
# [개념] def 이름(매개변수): 로 함수 정의. return a, b 하면 튜플 반환 → a, b = func() 로 받음.

# ---------- 따라 칠 코드 ----------
def add(a, b):
    return a + b

def get_two():
    return 100, 200

print(add(3, 5))
x, y = get_two()
print("x, y =", x, y)
# ----------------------------------

# -----------------------------------------------------------------------------
# 8단계: pandas DataFrame 기본
# -----------------------------------------------------------------------------
# [개념] df=pd.read_csv() 로 표 읽기. 열=df["이름"] 또는 df.iloc[:, j]. 행=df.loc[i] 또는 슬라이스.

# ---------- 따라 칠 코드 ----------
try:
    import pandas as pd
    df = pd.read_csv(CSV_PATH, encoding="utf-8")
    print("컬럼:", df.columns.tolist(), "shape:", df.shape)
    print("첫 열 일부:", df.iloc[:, 0].head().tolist())
except Exception as e:
    print("pandas/CSV 없음:", e)
# ----------------------------------

# =============================================================================
# === Part 2: 심화·시험 출제 가능 ===
# =============================================================================

# -----------------------------------------------------------------------------
# 9단계: enumerate, zip (인덱스와 값 함께, 두 리스트 묶기)
# -----------------------------------------------------------------------------
# [개념] enumerate(리스트)= (인덱스, 값) 쌍으로 반복. zip(리스트1, 리스트2)=같은 위치끼리 묶음.
# [시험] "인덱스와 함께 처리", "두 컬럼을 짝지어 연산" 할 때 유용.

# ---------- 따라 칠 코드 ----------
names = ["김", "이", "박"]
for i, n in enumerate(names):
    print(i, n)
ages = [20, 30, 40]
for name, age in zip(names, ages):
    print(f"{name}: {age}세")
# ----------------------------------

# -----------------------------------------------------------------------------
# 10단계: 딕셔너리, .get()
# -----------------------------------------------------------------------------
# [개념] 딕셔너리 = 키:값 쌍. d["키"]=값 접근(없으면 에러). d.get("키", 기본값)=없어도 안전.
# [시험] "키로 값 매핑", "기본값 처리" 시 자주 나옴.

# ---------- 따라 칠 코드 ----------
grade = {"A": 90, "B": 80, "C": 70}
print(grade["A"], grade.get("B"), grade.get("D", 0))
# ----------------------------------

# -----------------------------------------------------------------------------
# 11단계: try / except (예외 처리)
# -----------------------------------------------------------------------------
# [개념] try: 실행할 코드 except: 에러 나면 실행. 시험에서 "파일 없을 때", "결측 처리" 등.
# [메서드] except Exception as e: 로 에러 객체 e 사용 가능.

# ---------- 따라 칠 코드 ----------
try:
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        n_lines = len(f.readlines())
    print("파일 줄 수:", n_lines)
except FileNotFoundError:
    print("파일 없음")
except Exception as e:
    print("오류:", e)
# ----------------------------------

# -----------------------------------------------------------------------------
# 12단계: pandas 결측치 확인·처리 (시험 1유형 단골)
# -----------------------------------------------------------------------------
# [개념] 결측치=빈 칸(Missing Value). isnull()=결측이면 True. sum()으로 컬럼별 결측 개수.
# [메서드] df.isnull().sum() → 컬럼별 결측 개수. fillna(값)=결측을 해당 값으로 채움.

# ---------- 따라 칠 코드 ----------
try:
    import pandas as pd
    import numpy as np
    df = pd.read_csv(CSV_PATH, encoding="utf-8")
    print("결측치 개수:\n", df.isnull().sum())
    # 결측이 있으면 수치형은 평균, 범주형은 최빈값으로 채우는 패턴 (시험 자주 나옴)
    # df[숫자컬럼].fillna(df[숫자컬럼].mean(), inplace=True)
    # df[범주컬럼].fillna(df[범주컬럼].mode()[0], inplace=True)
except Exception as e:
    print("결측 예시 스킵:", e)
# ----------------------------------

# -----------------------------------------------------------------------------
# 13단계: pandas value_counts, 조건 필터
# -----------------------------------------------------------------------------
# [개념] value_counts()=각 값별 개수(빈도). df[df["컬럼"]==값]=조건 만족하는 행만.
# [시험] "최빈값 구하기", "특정 조건 행만 추출" 할 때 필수.

# ---------- 따라 칠 코드 ----------
try:
    import pandas as pd
    df = pd.read_csv(CSV_PATH, encoding="utf-8")
    # 첫 번째 컬럼이 범주형이라면
    col0 = df.columns[0]
    print("value_counts:\n", df[col0].value_counts())
    # 조건 필터: 예) 두 번째 컬럼이 30 이상인 행만
    if len(df.columns) >= 2 and pd.api.types.is_numeric_dtype(df.iloc[:, 1]):
        filtered = df[df.iloc[:, 1] >= 30]
        print("조건 필터 행 수:", len(filtered))
except Exception as e:
    print("value_counts 예시 스킵:", e)
# ----------------------------------

# -----------------------------------------------------------------------------
# 14단계: pandas 구간화 pd.cut (시험 1유형 단골)
# -----------------------------------------------------------------------------
# [개념] 연속값(나이 등)을 구간(20대, 30대 등)으로 나눔. bins=구간 경계, right=False=왼쪽 포함·오른쪽 미포함.
# [메서드] pd.cut(시리즈, bins=[20,30,40,50,200], right=False, labels=["20대","30대",...])

# ---------- 따라 칠 코드 ----------
try:
    import pandas as pd
    import numpy as np
    ages = pd.Series([23, 35, 42, 58, 29])
    age_group = pd.cut(ages, bins=[20, 30, 40, 50, 200], right=False, labels=["20대", "30대", "40대", "50대+"])
    print("나이 -> 연령대:\n", age_group.tolist())
except Exception as e:
    print("pd.cut 스킵:", e)
# ----------------------------------

# -----------------------------------------------------------------------------
# 15단계: pandas groupby, agg (집계)
# -----------------------------------------------------------------------------
# [개념] groupby(컬럼)=그 컬럼 값별로 묶음. agg({"열":"mean"})=그룹별 평균 등 집계.
# [시험] "직업별 평균 소득", "지역별 합계" 등 집계 문제에 자주 나옴.

# ---------- 따라 칠 코드 ----------
try:
    import pandas as pd
    df = pd.read_csv(CSV_PATH, encoding="utf-8")
    # 숫자 컬럼이 있는 경우 그룹별 평균 (첫 컬럼으로 그룹, 두 번째로 평균 예시)
    numeric = df.select_dtypes(include="number")
    if len(numeric.columns) >= 1 and len(df.columns) >= 1:
        by_col = df.columns[0]
        agg_col = numeric.columns[0]
        grouped = df.groupby(by_col)[agg_col].agg(["mean", "count"])
        print("groupby 집계:\n", grouped)
except Exception as e:
    print("groupby 예시 스킵:", e)
# ----------------------------------

# -----------------------------------------------------------------------------
# 16단계: 가설 검정 — t검정, 카이제곱, p-value 해석 (시험 3유형 단골)
# -----------------------------------------------------------------------------
# [개념] t검정=두 집단 평균 차이 검정. 카이제곱=두 범주형 변수 연관성. p-value<0.05면 "유의함"(차이/연관 있음).
# [메서드] stats.ttest_ind(그룹1, 그룹2) → (t통계량, p_value). chi2_contingency(분할표) → chi2, p, dof, expected.

# ---------- 따라 칠 코드 ----------
try:
    from scipy import stats
    import numpy as np
    group1 = np.array([100, 102, 98, 105, 97])
    group2 = np.array([108, 110, 106, 112, 104])
    t_stat, p_value = stats.ttest_ind(group1, group2)
    print(f"t검정: t={t_stat:.4f}, p-value={p_value:.4f}")
    if p_value < 0.05:
        print("결론: 유의수준 5%에서 두 집단 평균에 차이가 있다.")
    else:
        print("결론: 유의한 차이가 없다.")

    # 카이제곱: 분할표(교차표) 필요. pd.crosstab(행, 열) 로 만든 뒤 chi2_contingency에 넣음.
    import pandas as pd
    tab = pd.crosstab([1, 1, 0, 0, 1], [1, 0, 1, 0, 1])
    chi2, p_chi, dof, expected = stats.chi2_contingency(tab)
    print(f"카이제곱: chi2={chi2:.4f}, p-value={p_chi:.4f}")
except Exception as e:
    print("가설검정 스킵:", e)
# ----------------------------------

print("\n=== learn_concepts_by_typing (기초+심화) 끝 ===")
