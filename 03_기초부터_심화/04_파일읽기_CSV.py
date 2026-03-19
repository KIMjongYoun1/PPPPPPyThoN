# ============================================================
# 04. 파일 읽기 — CSV (중급)
# ============================================================
#
# [교수님 말]
# open(파일경로, "r") 로 파일을 열고, readlines() 로 한 줄씩 문자열 리스트로 읽어.
# with open(...) as f: 쓰면 블록 끝에서 자동으로 파일을 닫아서 안전해.
# CSV는 보통 첫 줄이 헤더(열 이름), 나머지가 데이터야. split(",") 로 쉼표 기준 나누면 돼.
#
# [import — 각 모듈 역할]
# os: 파일·폴더 경로 처리, 존재 여부 확인 (os.path.exists, os.path.join 등).
# open(): 파이썬 내장. 파일 열기. "r"=읽기, encoding="utf-8" 로 한글 처리.
# ============================================================

# ---------- 따라 칠 코드 (1): 텍스트 파일 한 줄씩 읽기 ----------
# (실제 파일이 없으면 아래는 건너뛰고 (2)로 해도 됨)
# with open("sample.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
# for line in lines:
#     print(line.strip())

# [수정 필요] readlines(0) 아님 → readlines() 로 바꿀 것.
# readlines(숫자) 는 "0번째 줄"이 아니라 버퍼 크기 힌트라서, 전체 줄을 받으려면 인자 없이 readlines() 호출.
with open("sample.txt", "r", encoding="utf-8") as Sample:
    lines = Sample.readlines()   # 전체 줄이 리스트로 들어감. lines[0]이 첫 줄(헤더), lines[1:]이 데이터.

# [수정 필요] 0번째 줄만 header에 넣으려면: header = lines[0] 하고, 나머지는 data_rows = lines[1:]
# 지금은 for 로 "매 줄마다" 돌면서 변수 이름만 Header 라고 했을 뿐, 실제로 header 변수에 첫 줄이 들어가진 않음.
header = lines[0] if lines else ""   # 0번째 줄 = 헤더
data_row = lines[1:]

# 두 for 를 하나로: (이름, 순회할 것) 짝을 리스트에 넣고 한 번에 순회
for label, seq in [("header", header), ("data_row", data_row)]:
    for item in seq:
        print(f"{label}: {item}")

# [수정 필요] print(lines.strip()) 는 틀림. lines 는 리스트라 .strip() 없음. 반복되는 "한 줄"을 출력하려면 line.strip()
for line in lines:
    print(line.strip())

# ---------- 따라 칠 코드 (2): CSV처럼 문자열로 연습 ----------
# CSV 한 줄 = "이름,나이,점수" 형태라고 가정
line1 = "이름,나이,점수"
line2 = "철수,25,80"
header = line1.split(",")
row = line2.split(",")
print("헤더:", header)
print("한 행:", row)

line1 = "이름,나이,점수"
line2 = "철수, 25, 99"
header = line1.split(",")
row = line2.split(",")
print(f"헤더: {header}, 한행 : {row}")

# ---------- 따라 칠 코드 (3): 여러 행 리스트로 묶기 ----------
raw_lines = [
    "이름,나이,점수",
    "철수,25,80",
    "영희,23,90",
]
rows = []
for line in raw_lines:
    rows.append(line.split(","))
header = rows[0]
data_rows = rows[1:]
print("헤더:", header)
print("데이터 행 수:", len(data_rows))

raw_lines = [
    "이름,나이,점수",
    "철수, 25, 90",
    "영희, 27, 65"
]
row = []
for line in raw_lines:
    row.append(line.split(","))
header = row[0]
data_rows = row[1:]
print(f"헤더: {header}")
print(f"데이터 갯수 : {len(data_rows)}")

# ---------- 따라 칠 코드 (4): 특정 열만 추출 (예: 점수=인덱스 2) ----------
scores = []
for row in data_rows:
    scores.append(int(row[2]))
print("점수들:", scores)
print("평균:", sum(scores) / len(scores))

scores = []
for row2 in data_rows:
    scores.append(int(row2[2]))

print(f"점수 : {scores}")
print(f"평균 : {sum(scores) / len(scores)}")

# ---------- 예제 ----------
# 02_실습코드에 sample.csv 가 있으면 그 경로로 열어서
# 첫 5줄만 출력해 보세요. (상위 폴더의 sample.csv: "../02_실습코드/sample.csv" 등)

import os
sample_path = os.path.join(os.path.dirname(__file__), "..", "02_실습코드", "sample.csv")
if os.path.exists(sample_path):
    with open(sample_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for i, line in enumerate(lines[:5]):
        print(f"{i+1}: {line.strip()}")
else:
    print("sample.csv 없음. raw_lines로 연습한 내용만 사용하세요.")


import os
sample_path = os.path.join(os.path.dirname(__file__), "..", "02_실습코드", "sample.csv")
if os.path.exists(sample_path):
    with open(sample_path, "r", encoding = "utf-8") as f:
        lines = f.readlines()
    for i, line in enumerate(lines[:5]):
        print(f"{i+1}: {line.strip()}")
else:
    print("sample.csv 없음. raw_lines로 연습한 내용만 사용하세요.")



