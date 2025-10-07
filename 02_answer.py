#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Chapter 02: Python 기본 문법 - 정답
===================================

이 파일은 02_practice.py의 정답입니다.
각 코드에 초보자를 위한 상세한 설명이 포함되어 있습니다!

연습 후 비교해보세요!
"""

print("=" * 70)
print("📚 Chapter 02: Python 기본 문법 - 정답")
print("=" * 70)

# ============================================
# 실습 1: 데이터 타입 이해하기
# ============================================

print("\n실습 1: 데이터 타입 이해하기")
print("-" * 70)

# ✅ 정답
name = "김철수"      # str (문자열)
age = 25            # int (정수)
height = 175.5      # float (실수)
is_student = False  # bool (불린)

"""
💡 설명:
- Python은 타입을 자동으로 추론합니다
- Java: String name = "김철수";
- Python: name = "김철수"  (타입 선언 불필요!)

타입 자동 추론:
- 따옴표로 감싸면 → str
- 정수면 → int
- 소수점 있으면 → float
- True/False → bool (주의: 대문자로 시작!)
"""

# ✅ 정답
print(f"name의 타입: {type(name)}")        # <class 'str'>
print(f"age의 타입: {type(age)}")          # <class 'int'>
print(f"height의 타입: {type(height)}")    # <class 'float'>
print(f"is_student의 타입: {type(is_student)}")  # <class 'bool'>

"""
💡 type() 함수:
- 변수의 타입을 알려줍니다
- Java의 변수.getClass()와 유사
- 디버깅할 때 매우 유용!

자주 하는 실수:
❌ print(f"타입: type(name)")  # type() 밖에서 {}로 안 감쌈
✅ print(f"타입: {type(name)}") # type()을 {}로 감싸야 함
"""


# ============================================
# 실습 2: 문자열 메서드
# ============================================

print("\n실습 2: 문자열 메서드")
print("-" * 70)

text = "  Hello Python World  "

# ✅ 정답 1: strip() - 양쪽 공백 제거
cleaned = text.strip()
print(f"원본: '{text}'")
print(f"공백 제거: '{cleaned}'")

"""
💡 strip() 설명:
- 문자열 양쪽의 공백을 제거합니다
- Java: text.trim()
- Python: text.strip()

변형:
- lstrip(): 왼쪽 공백만 제거
- rstrip(): 오른쪽 공백만 제거
"""

# ✅ 정답 2: upper() - 대문자로 변환
uppercase = text.upper()
print(f"대문자: '{uppercase}'")

"""
💡 upper() 설명:
- 모든 문자를 대문자로 변환
- Java: text.toUpperCase()
- Python: text.upper()
"""

# ✅ 정답 3: lower() - 소문자로 변환
lowercase = text.lower()
print(f"소문자: '{lowercase}'")

# ✅ 정답 4: replace() - 문자열 치환
replaced = text.replace("Python", "Java")
print(f"치환: '{replaced}'")

"""
💡 replace() 설명:
- 문자열의 일부를 다른 문자열로 교체
- text.replace(찾을문자열, 바꿀문자열)
- 원본은 변경되지 않음! (새 문자열 반환)

Java 비교:
text.replace("Python", "Java")  # 똑같음!
"""

# ✅ 정답 5: split() - 문자열 분리
words = text.split()  # 공백 기준으로 분리
print(f"단어 분리: {words}")

"""
💡 split() 설명:
- 문자열을 리스트로 분리
- split() → 공백 기준 분리
- split(',') → 쉼표 기준 분리

예시:
"a,b,c".split(',') → ['a', 'b', 'c']
"Hello World".split() → ['Hello', 'World']

Java 비교:
text.split(" ")  # Java
text.split()     # Python (공백은 생략 가능)
"""


# ============================================
# 실습 3: 숫자 연산
# ============================================

print("\n실습 3: 숫자 연산")
print("-" * 70)

a = 17
b = 5

# ✅ 정답
print(f"{a} + {b} = {a + b}")      # 덧셈: 22
print(f"{a} - {b} = {a - b}")      # 뺄셈: 12
print(f"{a} * {b} = {a * b}")      # 곱셈: 85
print(f"{a} / {b} = {a / b}")      # 나눗셈: 3.4 (항상 float!)
print(f"{a} // {b} = {a // b}")    # 정수 나눗셈: 3 (몫)
print(f"{a} % {b} = {a % b}")      # 나머지: 2
print(f"{a} ** {b} = {a ** b}")    # 거듭제곱: 17^5 = 1419857

"""
💡 Python 숫자 연산 핵심:

1. 나눗셈 (/)
   - 항상 float 반환!
   - Java: 10 / 3 = 3 (정수)
   - Python: 10 / 3 = 3.3333... (실수)

2. 정수 나눗셈 (//)
   - Java의 정수 나눗셈과 동일
   - 17 // 5 = 3 (몫만)

3. 거듭제곱 (**)
   - Java: Math.pow(17, 5)
   - Python: 17 ** 5 (훨씬 간단!)

4. 나머지 (%)
   - Java와 동일: 17 % 5 = 2

자주 하는 실수:
❌ 17 ^ 5  # XOR 연산자 (거듭제곱 아님!)
✅ 17 ** 5 # 거듭제곱
"""


# ============================================
# 실습 4: 리스트 기초
# ============================================

print("\n실습 4: 리스트 기초")
print("-" * 70)

# ✅ 정답
fruits = ["사과", "바나나", "오렌지"]

"""
💡 리스트 기본:
- Java의 ArrayList와 유사
- 대괄호 []로 생성
- 여러 타입 섞어도 됨!

Java 비교:
List<String> fruits = new ArrayList<>();
fruits.add("사과");

Python:
fruits = ["사과", "바나나", "오렌지"]  # 한 줄로 끝!
"""

# ✅ 정답: 리스트 작업들
print(f"전체 리스트: {fruits}")
print(f"첫 번째 과일: {fruits[0]}")     # 인덱스 0
print(f"마지막 과일: {fruits[-1]}")     # 인덱스 -1 (마지막)

fruits.append("포도")                   # 끝에 추가
print(f"추가 후: {fruits}")
print(f"과일 개수: {len(fruits)}")

"""
💡 리스트 인덱싱:
- 0부터 시작 (Java와 동일)
- 음수 인덱스 가능! (Python의 강력한 기능)
  - fruits[-1]: 마지막 요소
  - fruits[-2]: 뒤에서 두 번째
  
예시:
fruits = ["사과", "바나나", "오렌지"]
         [  0  ,    1   ,    2   ]  ← 양수 인덱스
         [ -3  ,   -2   ,   -1   ]  ← 음수 인덱스

Java에는 없는 기능:
❌ list.get(list.size() - 1)  // Java (마지막 요소)
✅ fruits[-1]                  # Python (훨씬 간단!)
"""

# 추가 메서드들
print("\n📌 리스트 추가 메서드:")
fruits.insert(1, "수박")  # 인덱스 1에 삽입
print(f"삽입 후: {fruits}")

fruits.remove("바나나")   # 특정 값 제거
print(f"제거 후: {fruits}")

"""
리스트 주요 메서드:
- append(값): 끝에 추가
- insert(위치, 값): 특정 위치에 삽입
- remove(값): 특정 값 제거
- pop(): 마지막 요소 제거하고 반환
- len(리스트): 길이
- clear(): 모두 제거

Java ArrayList vs Python list:
list.add(x)      → append(x)
list.get(i)      → list[i]
list.size()      → len(list)
list.remove(i)   → del list[i]
"""


# ============================================
# 실습 5: 딕셔너리 기초
# ============================================

print("\n실습 5: 딕셔너리 기초")
print("-" * 70)

# ✅ 정답
user = {
    "name": "김철수",
    "age": 25,
    "city": "서울"
}

"""
💡 딕셔너리 기본:
- Java의 HashMap과 유사
- {key: value} 형태
- key로 빠르게 조회

Java 비교:
Map<String, Object> user = new HashMap<>();
user.put("name", "김철수");
user.put("age", 25);

Python:
user = {"name": "김철수", "age": 25}  # 한 줄로 끝!

주의사항:
- key는 고유해야 함
- value는 어떤 타입이든 가능
- 순서 보장됨 (Python 3.7+)
"""

# ✅ 정답: 딕셔너리 작업들
print(f"전체 딕셔너리: {user}")
print(f"이름: {user['name']}")
print(f"나이: {user['age']}")

user["job"] = "개발자"  # 새 키 추가
print(f"추가 후: {user}")

print(f"모든 키: {user.keys()}")      # dict_keys(['name', 'age', 'city', 'job'])
print(f"모든 값: {user.values()}")    # dict_values(['김철수', 25, '서울', '개발자'])

"""
💡 딕셔너리 조회 방법:

방법 1: 대괄호 [] (권장!)
user["name"]  # "김철수"
user["xyz"]   # ❌ KeyError 발생! (키가 없으면)

방법 2: get() (안전!)
user.get("name")      # "김철수"
user.get("xyz")       # None (키가 없어도 에러 안 남!)
user.get("xyz", "기본값")  # "기본값" (키가 없으면)

Java 비교:
user.get("name")       # Java와 똑같음!
user.getOrDefault("xyz", "기본값")  # Java
user.get("xyz", "기본값")           # Python

추가 메서드:
- keys(): 모든 키
- values(): 모든 값
- items(): (키, 값) 쌍
- pop(키): 키 제거하고 값 반환
- clear(): 모두 제거
"""


# ============================================
# 실습 6: 문자열 슬라이싱
# ============================================

print("\n실습 6: 문자열 슬라이싱")
print("-" * 70)

text = "Python Programming"

# ✅ 정답
print(f"원본: '{text}'")
print(f"처음 6글자: '{text[0:6]}'")    # Python
print(f"처음 6글자: '{text[:6]}'")     # Python (0 생략 가능)
print(f"7번째부터 끝: '{text[7:]}'")    # Programming
print(f"마지막 11글자: '{text[-11:]}'") # Programming
print(f"전체 역순: '{text[::-1]}'")     # gnimmargorP nohtyP

"""
💡 슬라이싱 문법: text[start:end:step]

start: 시작 인덱스 (포함)
end: 끝 인덱스 (미포함!)
step: 간격

예시:
text = "Python Programming"
       [0123456789...]

text[0:6]   → "Python" (0부터 6 전까지)
text[:6]    → "Python" (처음부터 6 전까지)
text[7:]    → "Programming" (7부터 끝까지)
text[:]     → "Python Programming" (전체 복사)
text[::2]   → "Pto rgamn" (2칸씩 건너뛰기)
text[::-1]  → 역순!

음수 인덱스:
text[-11:]  → "Programming" (뒤에서 11번째부터)
text[:-5]   → "Python Programm" (끝 5글자 제외)

Java에는 없는 기능!
Java: text.substring(0, 6)
Python: text[:6]  (훨씬 간단!)

자주 하는 실수:
❌ text[0:6] → 0~6번째 (7글자)  # 잘못된 생각!
✅ text[0:6] → 0~5번째 (6글자)  # end는 미포함!
"""


# ============================================
# 실습 7: 타입 변환
# ============================================

print("\n실습 7: 타입 변환")
print("-" * 70)

# ✅ 정답 1: 문자열 → 정수
str_num = "123"
int_num = int(str_num)
print(f"문자열 '{str_num}' → 정수 {int_num}")
print(f"타입: {type(int_num)}")

# ✅ 정답 2: 정수 → 문자열
number = 456
str_number = str(number)
print(f"정수 {number} → 문자열 '{str_number}'")
print(f"타입: {type(str_number)}")

# ✅ 정답 3: 문자열 → 실수
str_float = "3.14"
float_num = float(str_float)
print(f"문자열 '{str_float}' → 실수 {float_num}")
print(f"타입: {type(float_num)}")

"""
💡 타입 변환 함수:

int(x)    → 정수로 변환
str(x)    → 문자열로 변환
float(x)  → 실수로 변환
bool(x)   → 불린으로 변환

Java 비교:
Integer.parseInt("123")  → int("123")
String.valueOf(456)      → str(456)
Double.parseDouble("3.14") → float("3.14")

주의사항:
❌ int("3.14")     # ValueError! (소수점 포함)
✅ int(float("3.14"))  # 3 (두 단계로)
✅ int(3.14)       # 3 (직접 변환)

❌ int("abc")      # ValueError! (숫자 아님)
✅ int("123")      # 123

불린 변환 규칙:
bool(0)      → False
bool(1)      → True
bool("")     → False (빈 문자열)
bool("abc")  → True
bool([])     → False (빈 리스트)
bool([1,2])  → True
"""


# ============================================
# 실습 8: None과 불린
# ============================================

print("\n실습 8: None과 불린")
print("-" * 70)

# ✅ 정답
result = None
print(f"초기값: {result}")

# ✅ 정답
if result is None:
    print("값이 없습니다")

"""
💡 None:
- Java의 null과 같음
- "값이 없음"을 표현
- 대문자 N으로 시작!

Java vs Python:
String x = null;  // Java
x = None          # Python

None 체크 방법:
❌ if result == None:   # 작동하지만 권장 안 함
✅ if result is None:   # 권장!

❌ if not result:       # None뿐만 아니라 0, "", [] 등도 False
✅ if result is None:   # None만 체크
"""

# ✅ 정답
is_active = True
is_deleted = False

print(f"활성화: {is_active}")
print(f"삭제됨: {is_deleted}")

"""
💡 불린 (Boolean):
- True / False (대문자로 시작!)
- Java: true / false (소문자)
- Python: True / False (대문자)

자주 하는 실수:
❌ is_active = true   # NameError! (소문자 X)
✅ is_active = True   # 대문자!

불린 연산:
and → 그리고 (Java의 &&)
or  → 또는 (Java의 ||)
not → 부정 (Java의 !)

예시:
True and False  → False
True or False   → True
not True        → False
"""


# ============================================
# 도전 과제 1: 계산기 프로그램
# ============================================

print("\n" + "=" * 70)
print("🎯 도전 과제 1: 고급 계산기 - 정답")
print("=" * 70)

num1 = 10
num2 = 3
operator = "+"

print(f"\n입력: {num1} {operator} {num2}")

# ✅ 정답
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "0으로 나눌 수 없습니다"
else:
    result = "잘못된 연산자"

print(f"결과: {result}")

"""
💡 if/elif/else:
- Java의 if/else if/else와 동일
- 콜론(:) 필수!
- 들여쓰기로 블록 구분 (중괄호 없음!)

Java:
if (condition) {
    // code
} else if (condition2) {
    // code
}

Python:
if condition:
    # code
elif condition2:
    # code

주의: 0으로 나누기
10 / 0  → ZeroDivisionError!
그래서 미리 체크해야 함
"""


# ============================================
# 도전 과제 2: 학생 정보 관리
# ============================================

print("\n" + "=" * 70)
print("🎯 도전 과제 2: 학생 정보 관리 - 정답")
print("=" * 70)

# ✅ 정답
students = [
    {"name": "김철수", "age": 20, "score": 85},
    {"name": "이영희", "age": 22, "score": 92},
    {"name": "박민수", "age": 21, "score": 78}
]

# ✅ 정답 1: 모든 학생 이름
print("\n모든 학생 이름:")
for student in students:
    print(f"  - {student['name']}")

"""
💡 for 루프:
- Java의 for-each와 유사
- 콜론(:) 필수!

Java:
for (Student s : students) {
    System.out.println(s.getName());
}

Python:
for student in students:
    print(student['name'])
"""

# ✅ 정답 2: 평균 점수
total_score = 0
for student in students:
    total_score += student['score']

average = total_score / len(students)
print(f"\n평균 점수: {average:.2f}")

"""
더 간단한 방법:
total = sum(s['score'] for s in students)
average = total / len(students)

또는:
scores = [s['score'] for s in students]
average = sum(scores) / len(scores)
"""

# ✅ 정답 3: 가장 높은 점수
highest_score = students[0]['score']
for student in students:
    if student['score'] > highest_score:
        highest_score = student['score']

print(f"가장 높은 점수: {highest_score}")

"""
더 간단한 방법:
highest = max(s['score'] for s in students)
"""

# ✅ 정답 4: 80점 이상 학생
print("\n80점 이상 학생:")
for student in students:
    if student['score'] >= 80:
        print(f"  - {student['name']}: {student['score']}점")


# ============================================
# 도전 과제 3: 단어 분석기
# ============================================

print("\n" + "=" * 70)
print("🎯 도전 과제 3: 단어 분석기 - 정답")
print("=" * 70)

sentence = "Python is an amazing programming language"

# ✅ 정답 1: 단어 분리
words = sentence.split()
print(f"단어 분리: {words}")

# ✅ 정답 2: 총 단어 개수
print(f"총 단어 개수: {len(words)}")

# ✅ 정답 3: 각 단어의 길이
print("\n각 단어의 길이:")
for word in words:
    print(f"  {word}: {len(word)}글자")

# ✅ 정답 4: 가장 긴 단어
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(f"\n가장 긴 단어: {longest_word} ({len(longest_word)}글자)")

"""
더 간단한 방법:
longest = max(words, key=len)
"""

# ✅ 정답 5: 모든 단어를 대문자로
uppercase_words = [word.upper() for word in words]
print(f"\n대문자 변환: {uppercase_words}")

"""
💡 리스트 컴프리헨션:
- Python의 강력한 기능!
- 리스트를 간결하게 생성

일반 방법:
uppercase_words = []
for word in words:
    uppercase_words.append(word.upper())

리스트 컴프리헨션:
uppercase_words = [word.upper() for word in words]

훨씬 간결하고 빠름!
"""


# ============================================
# 완료 메시지
# ============================================

print("\n" + "=" * 70)
print("🎉 Chapter 02 정답 확인 완료!")
print("=" * 70)

print("""
✅ 정답 핵심 요약:

1. 데이터 타입
   str, int, float, bool, None
   type() 함수로 확인

2. 문자열 메서드
   strip(), upper(), lower(), replace(), split()

3. 숫자 연산
   +, -, *, / (항상 float), // (정수 나눗셈), %, **

4. 리스트
   [값1, 값2, ...]
   인덱싱: list[0], list[-1]
   메서드: append(), insert(), remove()

5. 딕셔너리
   {키: 값, ...}
   조회: dict["키"] 또는 dict.get("키")
   메서드: keys(), values(), items()

6. 슬라이싱
   text[start:end:step]
   text[:6], text[7:], text[::-1]

7. 타입 변환
   int(), str(), float(), bool()

8. None과 불린
   None (null), True/False (대문자!)

💡 Java와의 주요 차이:
┌─────────────────────────────────────────┐
│ Java         │ Python                   │
├─────────────┼──────────────────────────┤
│ null         │ None                     │
│ true/false   │ True/False               │
│ list.get(i)  │ list[i]                  │
│ map.get(k)   │ dict["k"]                │
│ list.size()  │ len(list)                │
│ str.substring │ str[start:end]          │
└─────────────────────────────────────────┘

🎯 다음 Chapter:
03_practice.py - 자료구조 심화
(리스트, 딕셔너리, 튜플, 셋 완전 정복!)
""")



