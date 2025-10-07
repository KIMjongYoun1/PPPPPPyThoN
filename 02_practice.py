#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Chapter 02: Python 기본 문법 실습
=================================

학습 목표:
- 변수와 데이터 타입 완전 정복
- 문자열 메서드 활용
- 숫자 연산 (사칙연산, 거듭제곱 등)
- 리스트 기초
- 딕셔너리 기초

💡 각 TODO를 채워서 완성하세요!
"""

print("=" * 70)
print("📚 Chapter 02: Python 기본 문법 실습")
print("=" * 70)

# ============================================
# 실습 1: 데이터 타입 이해하기
# ============================================

print("\n실습 1: 데이터 타입 이해하기")
print("-" * 70)

# Python의 기본 데이터 타입
# Java: int x = 10;
# Python: x = 10  (타입 선언 불필요!)

# TODO: 아래 변수들을 선언하세요
# name: 문자열 (여러분의 이름)
# age: 정수 (여러분의 나이)
# height: 실수 (여러분의 키, cm)
# is_student: 불린 (학생이면 True, 아니면 False)

# 여기에 코드 작성 👇
name =  "김김김"
age = 20
height = 111.22
is_student = True



# TODO: 각 변수의 타입을 출력하세요
# 힌트: type(변수) 사용
# 출력 예시: name의 타입: <class 'str'>

# 여기에 코드 작성 👇
print("이름", type(name))
print("숫자", type(age))
print("실수", type(height))
print("불린", type(is_student))




# ============================================
# 실습 2: 문자열 메서드
# ============================================

print("\n실습 2: 문자열 메서드")
print("-" * 70)

text = "  Hello Python World  "

# TODO: 다음 문자열 메서드들을 사용해보세요
# 1. strip(): 양쪽 공백 제거
# 2. upper(): 대문자로 변환
# 3. lower(): 소문자로 변환
# 4. replace(): 문자열 치환
# 5. split(): 문자열 분리

# 여기에 코드 작성 👇
# cleaned = text.strip()
# print(f"공백 제거: {cleaned}")

print(f"공백제거: {text.strip()}")
print(f"대문자 {text.upper()}")
print(f"소문자: {text.lower()}")
print(f"문자열치환: {text.replace('Python', 'No')}")
print(f"문자열분리 {text.split()}")




# ============================================
# 실습 3: 숫자 연산
# ============================================

print("\n실습 3: 숫자 연산")
print("-" * 70)

a = 17
b = 5

# TODO: 다양한 연산을 수행하고 출력하세요
# 1. 덧셈: a + b
# 2. 뺄셈: a - b
# 3. 곱셈: a * b
# 4. 나눗셈: a / b (결과는 실수)
# 5. 정수 나눗셈: a // b (몫)
# 6. 나머지: a % b
# 7. 거듭제곱: a ** b

# 출력 예시: 17 + 5 = 22

# 여기에 코드 작성 👇
a = 22
b = 33
c = 223

print(f"덧셈 {a+b+c}")
print(f"뺄셈 {a-b-c}")
print(f"곱셈 {a*b*c}")
print(f"나눗셈 {a/b/c}")
print(f"정수나눗셈 {a//b//c}")
print(f"나머지 {a%b%c}")
print(f"거듭제곱 {a ** b}")







# ============================================
# 실습 4: 리스트 기초
# ============================================

print("\n실습 4: 리스트 기초")
print("-" * 70)

# 리스트 = Java의 ArrayList
# Python: 타입 제한 없음!

# TODO: 과일 리스트를 만드세요
# fruits = ["사과", "바나나", "오렌지"]

# 여기에 코드 작성 👇
fruits = ["사과", "바나나", "포더", "30년산"]

# TODO: 리스트 작업들을 수행하세요
# 1. 리스트 출력
# 2. 첫 번째 과일 출력 (인덱스 0)
# 3. 마지막 과일 출력 (인덱스 -1)
# 4. 과일 추가 (append)
# 5. 리스트 길이 출력 (len)

# 여기에 코드 작성 👇
print(f"{fruits}")
print(f"{fruits[0]}")
print(f"{fruits[-1]}")
fruits.append("키위")
print(f"{len(fruits)}")





# ============================================
# 실습 5: 딕셔너리 기초
# ============================================

print("\n실습 5: 딕셔너리 기초")
print("-" * 70)

# 딕셔너리 = Java의 HashMap
# {key: value} 형태

# TODO: 사용자 정보를 딕셔너리로 만드세요
# user = {
#     "name": "김철수",
#     "age": 25,
#     "city": "서울"
# }

# 여기에 코드 작성 👇
# Json(존슨?)
user = {
    "name" : "김철수",
    "Age" : "33",
    "city" : "서울"
}


# TODO: 딕셔너리 작업들을 수행하세요
# 1. 전체 딕셔너리 출력
# 2. 이름만 출력 (user["name"])
# 3. 나이만 출력
# 4. 새로운 키 추가 (job: "개발자")
# 5. 모든 키 출력 (user.keys())
# 6. 모든 값 출력 (user.values())

# 여기에 코드 작성 👇

print(f"{user['name']}")
print(f"{user['Age']}")
print(f"{user['city']}")
user["job"] = "개발자"
print(f"{user.keys()}")
print(f"{user.values()}")





# ============================================
# 실습 6: 문자열 슬라이싱
# ============================================

print("\n실습 6: 문자열 슬라이싱")
print("-" * 70)

text = "Python Programming"

# TODO: 슬라이싱을 사용해보세요
# 1. 처음 6글자: text[0:6] 또는 text[:6]
# 2. 7번째부터 끝까지: text[7:]
# 3. 마지막 11글자: text[-11:]
# 4. 전체 역순: text[::-1]

# 출력 예시: 처음 6글자: Python
# 띄어쓰기도 스트링으로잡음  글자수포함됨
# 여기에 코드 작성 👇
print(f"{text[0:8]}")
print(f"{text[7:]}")
print(f"{text[-7:]}")

print(f"{text[::-1]}")



# ============================================
# 실습 7: 타입 변환
# ============================================

print("\n실습 7: 타입 변환")
print("-" * 70)

# TODO: 다양한 타입 변환을 수행하세요

# 1. 문자열 → 정수
str_num = "123"
# int_num = int(str_num)

# 여기에 코드 작성 👇
int_num = int(str_num)

# 2. 정수 → 문자열
number = 456
# str_number = str(number)

# 여기에 코드 작성 👇
str_number = str(number)

# 3. 문자열 → 실수
str_float = "3.14"
# float_num = float(str_float)

# 여기에 코드 작성 👇
float_num = float(str_float)

# TODO: 변환된 값들을 출력하세요

print(f"{int_num}")
print(f"{str_number}")
print(f"{float_num}")


# ============================================
# 실습 8: None과 불린
# ============================================

print("\n실습 8: None과 불린")
print("-" * 70)

# None = Java의 null
# True/False = Java의 true/false (대문자로 시작!)

# TODO: None 사용해보기
result = 333
print(f"초기값: {result}")

# TODO: 조건문으로 None 체크
# if result is None:
#     print("값이 없습니다")

# 여기에 코드 작성 👇
if result is None:
    print("값이 없습니다")
else:
    print(f"값이 있습니다 {result}")

# TODO: 불린 값 사용
is_active = True
is_deleted = False

# 여기에 코드 작성 👇 (값 출력)
print(f"is_active: {is_active}")

# ============================================
# 도전 과제 1: 계산기 프로그램
# ============================================

print("\n" + "=" * 70)
print("🎯 도전 과제 1: 고급 계산기")
print("=" * 70)

# TODO: 사용자에게 두 숫자와 연산자를 입력받으세요
# num1 = float(input("첫 번째 숫자: "))
# num2 = float(input("두 번째 숫자: "))
# operator = input("연산자 (+, -, *, /): ")

# 데모용 (input 없이)
num1 = 10
num2 = 3
operator = "+"

print(f"\n입력: {num1} {operator} {num2}")

# TODO: 연산자에 따라 계산 결과를 출력하세요
# 힌트: if/elif 사용
# if operator == "+":
#     result = num1 + num2

# 여기에 코드 작성 👇
num1 = float(input("첫번째 숫자를 입력하세요" ))
operator = input("연산자를 입력하세요" )
num2 = float(input("두번째 숫자를 입력하세요" ))

if operator == "+":
    result =num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("잘못된 연산자입니다")
    result = None

if result is not None:
    print(f"{result}")

    




# ============================================
# 도전 과제 2: 학생 정보 관리
# ============================================

print("\n" + "=" * 70)
print("🎯 도전 과제 2: 학생 정보 관리")
print("=" * 70)

# TODO: 3명의 학생 정보를 리스트에 저장하세요
# 각 학생은 딕셔너리로 표현
# students = [
#     {"name": "김철수", "age": 20, "score": 85},
#     {"name": "이영희", "age": 22, "score": 92},
#     {"name": "박민수", "age": 21, "score": 78}
# ]

# 여기에 코드 작성 👇
students = [
        {
        "name" : "김철수",
        "age" : 20,
        "score" : 85
        }, {
            "name" : "이영희",
            "age" : 22,
            "score" : 92
        }, {
            "name" : "박민수",
            "age" : 21,
            "score" : 78
        }
]



# TODO: 다음 작업들을 수행하세요
# 1. 모든 학생 이름 출력
# 2. 평균 점수 계산
# 3. 가장 높은 점수 찾기
# 4. 점수가 80점 이상인 학생 이름 출력

# 여기에 코드 작성 👇
print(f"{students[0][1][2]['name']}")

for student in students:
    print(f"{student['name']}")
    
    
temp = 0
for student in students:
     temp += student['score']
print(f"{temp / len(students)}")

max_score = 0
for student in students:
    if student['score'] > max_score:
        max_score = student['score']
print(f"{max_score}")
    
for student in students:
        if student['score'] >= 80:
            print(f"{student['name']}")





# ============================================
# 도전 과제 3: 단어 분석기
# ============================================

print("\n" + "=" * 70)
print("🎯 도전 과제 3: 단어 분석기")
print("=" * 70)

sentence = "Python is an amazing programming language"

# TODO: 다음 작업들을 수행하세요
# 1. 문장을 단어로 분리 (split)
# 2. 총 단어 개수 출력
# 3. 각 단어의 길이 출력
# 4. 가장 긴 단어 찾기
# 5. 모든 단어를 대문자로 변환

# 여기에 코드 작성 👇

for word in sentence.split():
    
    
    count += 1
print(f"{sentence}")
print(f"{count}")



for word in sentence:
    print(f"{len(word)}")

for word in sentence:

    max_length = 0
    if len(word) > max_length:
        max_length = len(word)
        max_word = word
    
print(f"{max_word}")

for word in sentence:
    print(f"{word.upper()}")





# ============================================
# 완료 메시지
# ============================================

print("\n" + "=" * 70)
print("🎉 Chapter 02 실습 완료!")
print("=" * 70)

print("""
💡 배운 내용 정리:
✓ 데이터 타입 (str, int, float, bool, None)
✓ 문자열 메서드 (strip, upper, lower, replace, split)
✓ 숫자 연산 (+, -, *, /, //, %, **)
✓ 리스트 기초 (생성, 인덱싱, append, len)
✓ 딕셔너리 기초 (생성, 조회, 추가, keys, values)
✓ 슬라이싱 (문자열/리스트 자르기)
✓ 타입 변환 (int, str, float)
✓ None과 불린

🎯 다음 단계:
- 02_answer.py 와 비교하기
- 02_string_formatting_practice.py 실습하기
- Chapter 03 (자료구조)로 넘어가기

📚 Java와의 차이점:
- 타입 선언 불필요
- 리스트에 여러 타입 섞어도 됨
- 딕셔너리가 매우 강력
- 슬라이싱이 직관적
- None vs null
- True/False vs true/false (대소문자!)
""")

print("\n💪 잘 하고 있어요! 다음 챕터로 고고!")



