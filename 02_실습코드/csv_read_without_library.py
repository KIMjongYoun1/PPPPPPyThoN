# -*- coding: utf-8 -*-
"""
CSV를 라이브러리 없이 읽는 방법 (Python 기본 기능만 사용)

- pandas 없이: 내장 모듈 csv 또는 open() + split() 사용
- 설치 필요: 없음 (Python 설치만 있으면 됨)
"""

# =============================================================================
# 방법 1: 내장 모듈 csv 사용 (pip 설치 불필요)
# =============================================================================
# [원리] csv 모듈은 Python 설치 시 함께 포함된 표준 라이브러리. import만 하면 됨.

import csv
import os

# [원리] 이 스크립트와 같은 폴더의 sample.csv 사용. 02_실습코드 폴더에서 실행하면 됨.
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'sample.csv')

# [원리] open(파일경로, 'r', encoding='utf-8'): 파일을 텍스트 모드로 열기. 한글은 utf-8 지정.
# with: 블록을 벗어나면 파일을 자동으로 닫아줌.
with open(csv_path, 'r', encoding='utf-8') as f:
    # [원리] csv.reader(f): 파일 객체를 넘기면 한 줄씩 리스트로 파싱. 쉼표로 열 구분.
    reader = csv.reader(f)
    # [원리] 첫 줄은 보통 헤더(컬럼명). next(reader)로 한 줄 읽고 헤더로 저장.
    header = next(reader)
    # [원리] 나머지 줄을 리스트의 리스트로 읽음. rows = [ [값1,값2,...], [값1,값2,...], ... ]
    rows = list(reader)

# [원리] header는 ['이름','나이','직업'] 형태. rows는 데이터 행들.
print("방법 1 (csv 모듈) - 헤더:", header)
print("방법 1 - 데이터 행 수:", len(rows))
if rows:
    print("방법 1 - 첫 행:", rows[0])

# =============================================================================
# 방법 2: open() + split() 만 사용 (csv 모듈도 안 쓸 때)
# =============================================================================
# [원리] CSV는 결국 "쉼표로 구분된 텍스트 파일". 한 줄씩 읽고 쉼표로 잘라도 됨.

with open(csv_path, 'r', encoding='utf-8') as f:
    # [원리] readlines(): 파일 전체를 한 줄씩 문자열 리스트로 읽음.
    lines = f.readlines()

# [원리] 첫 줄이 헤더. strip()으로 줄바꿈 제거 후 split(',')으로 쉼표 기준 분리.
header2 = lines[0].strip().split(',')
# [원리] 두 번째 줄부터가 데이터. 각 줄을 strip 후 split(',').
rows2 = [line.strip().split(',') for line in lines[1:]]

print("\n방법 2 (open+split) - 헤더:", header2)
print("방법 2 - 데이터 행 수:", len(rows2))
if rows2:
    print("방법 2 - 첫 행:", rows2[0])

# =============================================================================
# 값으로 접근하기 (컬럼명으로 찾으려면)
# =============================================================================
# [원리] 헤더 인덱스를 알면 "이름" 열만 뽑기 등 가능. 딕셔너리 리스트로 바꾸면 편함.

# [원리] 각 행을 {컬럼명: 값} 딕셔너리로 만듦. header[0]이 첫 번째 컬럼명, row[0]이 첫 번째 값.
data_as_dicts = []
for row in rows:
    # [원리] zip(header, row): (헤더1,값1), (헤더2,값2), ... → dict로 변환.
    data_as_dicts.append(dict(zip(header, row)))

# [원리] 이제 data_as_dicts[0]['나이'] 처럼 컬럼명으로 접근 가능.
if data_as_dicts:
    print("\n첫 행의 '나이' 컬럼:", data_as_dicts[0].get('나이'))

# =============================================================================
# 예제용 sample.csv가 없을 때를 위해 메모리에서 바로 예제 (실제 파일 없이)
# =============================================================================
# 아래는 "파일이 없어도" 문자열을 CSV처럼 파싱하는 예제.

csv_text = """이름,나이,직업
김철수,25,직장인
이영희,30,프리랜서
박민수,28,자영업"""

# [원리] 문자열을 줄 단위로 나누면 파일에서 읽은 것과 동일하게 처리 가능.
lines_in_memory = csv_text.strip().split('\n')
header_m = lines_in_memory[0].split(',')
rows_m = [line.split(',') for line in lines_in_memory[1:]]

print("\n(파일 없이 문자열만으로) 헤더:", header_m)
print("(파일 없이 문자열만으로) 데이터:", rows_m)
