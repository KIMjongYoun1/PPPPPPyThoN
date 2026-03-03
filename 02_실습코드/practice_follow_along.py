# -*- coding: utf-8 -*-
"""
[따라치기] - 파이썬 처음이면 여기부터

이 파일은 "빈칸 채우기"가 아니라, 이미 써져 있는 코드를
한 줄 한 줄 그대로 따라 치면서 익히는 용도예요.

사용법:
  1. 이 파일을 열고, 아래 A~C 블록을 본문 그대로 따라 친다.
  2. 다 치면 저장하고 터미널에서: python practice_follow_along.py
  3. 출력이 예상과 같으면 성공.

같은 폴더에 sample.csv 가 있어야 C편이 동작해요.
"""

import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(SCRIPT_DIR, "sample.csv")

# =============================================================================
# A편: 변수와 출력 (따라 치기)
# =============================================================================
# 아래 세 줄을 그대로 따라 쳐 보세요.

name = "김철수"
age = 25
print(f"제 이름은 {name}이고, 나이는 {age}세입니다.")

name ="KimjongYoun"
aget = 34
print(f"myName is {name} and Age is {age}")

# =============================================================================
# B편: 리스트와 for (따라 치기)
# =============================================================================
# 아래 블록을 그대로 따라 쳐 보세요.

numbers = [10, 20, 30]
result = []
for n in numbers:
    result.append(n + 5)
print("더한 결과:", result)

numbers = [10, 20, 30]
result = []
for n in numbers:
    result.append(n + 5)
print("Plus 5 Result is", result)

# =============================================================================
# C편: 파일 읽기 (따라 치기)
# =============================================================================
# 아래 블록을 그대로 따라 쳐 보세요. sample.csv 를 열어서 헤더와 행을 나눕니다.

with open(CSV_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

header_list = lines[0].strip().split(",")
rows_list = [line.strip().split(",") for line in lines[1:]]

print("헤더:", header_list)
print("데이터 행 개수:", len(rows_list))
print("첫 번째 행:", rows_list[0] if rows_list else "없음")

with open(CSV_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

header_list = lines[0].strip().split(",")
rows_list = [line.strip().split(",") for line in lines[1:]]

print("Header", header_list)
print("HangCount", len(rows_list))
print("FirstRow", rows_list[0] if rows_list else "Nohave")


# =============================================================================
# D편: 반환값 두 개 받기 (따라 치기)
# =============================================================================

def get_two():
    return 100, 200

a, b = get_two()
print("a, b =", a, b)

print("\n=== 따라치기 끝 === ")

def get_two():
        return 100, 200

a, b = get_two()
print("a, b =" ,a,b)

print("\n=== 따라치기 끝 === ")