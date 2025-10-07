#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Chapter 01: Python 환경 설정 - 정답
===================================

이 파일은 01_practice.py의 정답입니다.
연습 후 비교해보세요!
"""

print("=" * 60)
print("📚 Chapter 01: Python 환경 설정 - 정답")
print("=" * 60)

# ============================================
# 실습 1: Python 버전 확인
# ============================================

print("\n실습 1: Python 버전 확인")
print("-" * 60)

import sys

# ✅ 정답
print(f"Python version: {sys.version}")

# 또는
print(f"Python 버전: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")


# ============================================
# 실습 2: 변수와 print
# ============================================

print("\n실습 2: 변수와 print")
print("-" * 60)

# ✅ 정답
my_name = "김철수"
my_age = 25
my_job = "개발자"

# ✅ 정답
print(f"안녕하세요! 저는 {my_name}이고, {my_age}세입니다. {my_job}입니다.")

# 다른 방법들:
print(f"안녕하세요! 저는 {my_name}이고, {my_age}세 {my_job}입니다.")
print("안녕하세요! 저는 " + my_name + "이고, " + str(my_age) + "세입니다.")


# ============================================
# 실습 3: 주석 연습
# ============================================

print("\n실습 3: 주석 작성")
print("-" * 60)

# ✅ 정답 (주석 추가)
x = 10  # 첫 번째 숫자
y = 20  # 두 번째 숫자
result = x + y  # 두 숫자의 합
print(result)  # 결과 출력: 30


# ============================================
# 실습 4: 기본 연산
# ============================================

print("\n실습 4: 기본 연산")
print("-" * 60)

num1 = 15
num2 = 27

# ✅ 정답
sum_result = num1 + num2

# ✅ 정답
print(f"{num1} + {num2} = {sum_result}")

# 다른 방법:
print(f"{num1} + {num2} = {num1 + num2}")


# ============================================
# 실습 5: 타입 확인
# ============================================

print("\n실습 5: 변수 타입 확인")
print("-" * 60)

name = "김철수"
age = 25
height = 175.5
is_student = True

# ✅ 정답
print(f"name의 타입: {type(name)}")
print(f"age의 타입: {type(age)}")
print(f"height의 타입: {type(height)}")
print(f"is_student의 타입: {type(is_student)}")

# Java와 비교:
"""
Java:
String name = "김철수";      → <class 'str'>
int age = 25;                → <class 'int'>
double height = 175.5;       → <class 'float'>
boolean isStudent = true;    → <class 'bool'>
"""


# ============================================
# 실습 6: 문자열 기초
# ============================================

print("\n실습 6: 문자열 다루기")
print("-" * 60)

string1 = "큰따옴표 문자열"

# ✅ 정답
string2 = '작은따옴표 문자열'

print(f"string1: {string1}")
print(f"string2: {string2}")

first_name = "김"
last_name = "철수"

# ✅ 정답
full_name = first_name + last_name

# ✅ 정답
print(f"전체 이름: {full_name}")

# 다른 방법들:
full_name = f"{first_name}{last_name}"  # f-string 사용
full_name = "".join([first_name, last_name])  # join 사용


# ============================================
# 실습 7: 입력 받기
# ============================================

print("\n실습 7: 사용자 입력")
print("-" * 60)

# ✅ 정답 (실제 실행 시 주석 해제)
# user_name = input("이름을 입력하세요: ")

# 데모용 (input 없이 실행)
user_name = "이영희"  # 예시 값
print(f"입력된 이름: {user_name}")

# ✅ 정답
print(f"안녕하세요, {user_name}님!")


# ============================================
# 도전 과제: 간단한 계산기
# ============================================

print("\n" + "=" * 60)
print("🎯 도전 과제: 간단한 계산기 만들기 - 정답")
print("=" * 60)

# ✅ 정답 (실제 실행 시 주석 해제)
# num1 = int(input("첫 번째 숫자: "))
# num2 = int(input("두 번째 숫자: "))

# 데모용 (input 없이 실행)
num1 = 10
num2 = 5
print(f"입력된 숫자: {num1}, {num2}")

# ✅ 정답
print(f"\n사칙연산 결과:")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} × {num2} = {num1 * num2}")
print(f"{num1} ÷ {num2} = {num1 / num2}")

# 추가: 정수 나눗셈과 나머지
print(f"\n추가 연산:")
print(f"{num1} // {num2} = {num1 // num2}  (정수 나눗셈)")
print(f"{num1} % {num2} = {num1 % num2}  (나머지)")
print(f"{num1} ** {num2} = {num1 ** num2}  (거듭제곱)")


# ============================================
# 보너스: 파일 정보
# ============================================

print("\n" + "=" * 60)
print("📁 보너스: 파일 정보")
print("=" * 60)

print(f"현재 파일: {__file__}")
print(f"모듈 이름: {__name__}")

if __name__ == "__main__":
    print("\n✅ 이 파일이 직접 실행되었습니다!")
    print("(다른 파일에서 import 하면 이 부분은 실행 안 됨)")


# ============================================
# 추가 예제
# ============================================

print("\n" + "=" * 60)
print("🌟 추가 예제: 더 알아보기")
print("=" * 60)

# 1. 여러 변수 동시 선언
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# 2. 변수 값 교환
a, b = 10, 20
print(f"교환 전: a={a}, b={b}")
a, b = b, a  # Python의 강력한 기능!
print(f"교환 후: a={a}, b={b}")

# Java에서는:
# temp = a;
# a = b;
# b = temp;

# 3. 같은 값 할당
x = y = z = 100
print(f"x={x}, y={y}, z={z}")

# 4. 문자열 반복
print("=" * 30)  # = 기호 30개
print("Python! " * 3)  # Python! Python! Python!

# 5. 여러 줄 문자열
multi_line = """
첫 번째 줄
두 번째 줄
세 번째 줄
"""
print(multi_line)


# ============================================
# 완료 메시지
# ============================================

print("\n" + "=" * 60)
print("🎉 Chapter 01 정답 확인 완료!")
print("=" * 60)

print("""
✅ 정답 핵심 요약:

1. Python 버전: sys.version
2. 변수 선언: name = "값" (타입 선언 불필요)
3. 출력: print(f"...")
4. 타입 확인: type(변수)
5. 문자열 연결: "문자" + "열" 또는 f"{변수}"
6. 입력: input("메시지")
7. 타입 변환: int(), str(), float()

🎯 Java와의 주요 차이:
┌─────────────────────────────────────────┐
│ Java         │ Python                   │
├─────────────┼──────────────────────────┤
│ int x = 10; │ x = 10                   │
│ String s;   │ s = "문자열"             │
│ System.out  │ print()                  │
│ Scanner     │ input()                  │
│ Integer.parseInt() │ int()             │
└─────────────────────────────────────────┘

💡 기억하세요:
- Python은 간결함이 철학입니다!
- 타입 선언 없이도 작동합니다
- print()는 내장 함수입니다
- 세미콜론 불필요합니다

📚 다음 Chapter:
02_practice.py - 기본 문법 심화
""")



