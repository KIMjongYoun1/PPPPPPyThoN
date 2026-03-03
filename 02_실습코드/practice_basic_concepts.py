# -*- coding: utf-8 -*-
"""
[기본 개념 실습] - 강의 전 스스로 채워보기

사용법:
  1. 아래 각 실습의 "여기에 작성" 부분을 채운다.
  2. 터미널에서 실행: python practice_basic_concepts.py
  3. 맨 아래 "=== 검사용 출력 ===" 부분이 출력되면, 그 결과 전체를 복사해서
     채팅에 "검사해줘" 라고 붙여넣으면 됨.

필요: 02_실습코드 폴더에 sample.csv 가 있어야 함.
"""

import os

# 이 파일과 같은 폴더의 sample.csv 경로 (수정하지 마세요)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(SCRIPT_DIR, "sample.csv")

# =============================================================================
# 실습 1: 변수와 f-string
# =============================================================================
# 목표: 이름(name)과 나이(age) 변수에 값을 넣고, f-string으로
#       "제 이름은 OOO이고, 나이는 OO세입니다." 를 출력하는 변수 sentence 를 만든다.

name = None   # 여기에 문자열로 이름 넣기 (예: "김철수")
age = None    # 여기에 숫자로 나이 넣기 (예: 25)
sentence = None   # 여기에 f-string으로 "제 이름은 {name}이고, 나이는 {age}세입니다." 형태로 넣기

name = "JyKim"
age = 34
sentence = print(f"Myname", {name} and "Age", {age})

# print(sentence)  # 확인용 (주석 해제해서 실행해보기)

# =============================================================================
# 실습 2: 리스트와 for
# =============================================================================
# 목표: 숫자 리스트 [10, 20, 30]을 만들고, for로 돌면서 각 값에 5를 더한 결과를
#       더한_결과 리스트에 넣는다. (더한_결과 = [15, 25, 35] 가 되면 됨)

list_numbers = [10, 20, 30]
result = []

for plus in list_numbers:
    result.append(plus + 5)
print("Plust + 5 result =", plus)

숫자리스트 = None   # [10, 20, 30]
더한_결과 = None    # for 문으로 각 값+5 를 append

# =============================================================================
# 실습 3: CSV 읽기 (pandas 없이 - open + split)
# =============================================================================
# 목표: CSV_PATH 파일을 open해서 읽고, 첫 줄을 헤더, 나머지를 데이터 행으로 나눈다.
#       헤더는 리스트 header_list, 데이터 행들은 리스트의 리스트 rows_list 로 담는다.
# 참고: f.readlines() 로 만든 lines = 파일의 "가로 한 줄(행)"씩 담은 리스트.

header_list = None   # 파일 첫 줄을 strip().split(',') 한 결과
rows_list = None      # 나머지 줄들을 strip().split(',') 해서 리스트로 모은 것

# with open(CSV_PATH, 'r', encoding='utf-8') as f:
#     lines = f.readlines()
# header_list = ...
# rows_list = ...

with open(CSV_PATH, "r", encoding = "utf-8") as Fe:
    lines = Fe.readlines()
header_list = lines[0].strip().split(",")

# =============================================================================
# 실습 4: pandas 로 CSV 읽기 (pandas 쓸 수 있으면)
# =============================================================================
# 목표: pandas로 CSV_PATH 를 읽어서 DataFrame df 로 만든다.
#       pandas를 import 하고, pd.read_csv(CSV_PATH, encoding='utf-8') 사용.

df = None
try:
    import pandas as pd
    # df = pd.read_csv(...)  여기에 작성
    read = pd.read_csv(CSV_PATH, encoding = "utf-8")
    pass
except Exception:
    pass   # pandas 없으면 건너뜀

# =============================================================================
# 실습 5: 결측치 확인 (pandas 사용 시)
# =============================================================================
# 목표: df가 있을 때, 결측치 개수를 컬럼별로 세서 missing_counts 에 넣는다.
#       df.isnull().sum() 사용.

missing_counts = None
if df is not None:
    # missing_counts = ...""
    missing_counts = df.isnull().sum()
    print("Missing Counts =", missing_counts)
    pass

# =============================================================================
# 실습 6: 반환값 두 개 받기
# =============================================================================
# 목표: (100, 200) 을 반환하는 함수 get_two()를 정의하고,
#       a, b = get_two() 로 받아서 a는 100, b는 200 이 되게 한다.

def get_two():
    # return (100, 200)  또는 return 100, 200
    return None, None   # 여기 수정

a, b = get_two()   # a=100, b=200 이 되어야 함

def get_two():
    return 300, 2000
print(f"a,b = ", a,b)
# =============================================================================
# 검사용 출력 (이 부분을 실행한 결과 전체를 복사해서 채팅에 붙여넣으면 검사 가능)
# =============================================================================
def run_checks():
    results = []
    results.append("[실습1] sentence = " + str(sentence))
    results.append("[실습2] 더한_결과 = " + str(더한_결과))
    results.append("[실습3] header_list = " + str(header_list))
    results.append("[실습3] rows_list 개수 = " + str(len(rows_list) if rows_list else 0))
    results.append("[실습4] df 있음? = " + str(df is not None))
    if df is not None:
        results.append("[실습4] df 컬럼 = " + str(list(df.columns)))
    results.append("[실습5] missing_counts = " + str(missing_counts))
    results.append("[실습6] a, b = " + str((a, b)))
    return results

if __name__ == "__main__":
    print("=== 검사용 출력 ===")
    for line in run_checks():
        print(line)
    print("=== 끝 ===")
