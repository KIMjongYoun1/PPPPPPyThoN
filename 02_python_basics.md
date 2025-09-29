# 파이썬 기본 문법

## 1. 파이썬의 특징

### 자바/리액트 개발자를 위한 파이썬 특징
- **인터프리터 언어**: 컴파일 과정 없이 바로 실행
- **동적 타입**: 변수 타입을 미리 선언하지 않음
- **들여쓰기 기반**: 중괄호 대신 들여쓰기로 코드 블록 구분
- **간결한 문법**: 같은 기능을 더 적은 코드로 작성

## 2. 변수와 데이터 타입

### 변수 선언
```python
# 자바와 달리 타입 선언 불필요
name = "김철수"           # 문자열
age = 25                 # 정수
height = 175.5           # 실수
is_student = True        # 불린
```

### 기본 데이터 타입
```python
# 숫자 타입
integer_num = 42
float_num = 3.14
complex_num = 3 + 4j

# 문자열
single_quote = 'Hello'
double_quote = "World"
triple_quote = """여러 줄
문자열입니다"""

# 불린
is_true = True
is_false = False

# None (자바의 null과 유사)
empty_value = None
```

### 타입 확인
```python
print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
```

## 3. 문자열 다루기

### 문자열 포맷팅
```python
name = "철수"
age = 25

# f-string (Python 3.6+, 가장 권장)
message = f"안녕하세요, {name}님! 나이는 {age}세입니다."

# format() 메서드
message = "안녕하세요, {}님! 나이는 {}세입니다.".format(name, age)

# % 포맷팅 (구식)
message = "안녕하세요, %s님! 나이는 %d세입니다." % (name, age)

print(message)
```

### 문자열 메서드
```python
text = "  Hello World  "

print(text.strip())           # "Hello World" (공백 제거)
print(text.upper())           # "  HELLO WORLD  "
print(text.lower())           # "  hello world  "
print(text.replace("World", "Python"))  # "  Hello Python  "
print(text.split())           # ['Hello', 'World']
print(len(text))              # 15
```

## 4. 숫자 연산

### 기본 연산자
```python
a = 10
b = 3

print(a + b)    # 13 (덧셈)
print(a - b)    # 7  (뺄셈)
print(a * b)    # 30 (곱셈)
print(a / b)    # 3.333... (나눗셈, 항상 float 반환)
print(a // b)   # 3  (정수 나눗셈)
print(a % b)    # 1  (나머지)
print(a ** b)   # 1000 (거듭제곱)
```

### 복합 할당 연산자
```python
x = 10
x += 5    # x = x + 5
x -= 3    # x = x - 3
x *= 2    # x = x * 2
x /= 4    # x = x / 4
print(x)  # 6.0
```

## 5. 입력과 출력

### 출력 (print)
```python
# 기본 출력
print("Hello, World!")

# 여러 값 출력
name = "철수"
age = 25
print("이름:", name, "나이:", age)

# 구분자와 끝 문자 설정
print("Python", "is", "awesome", sep="-", end="!\n")

# 포맷팅과 함께
print(f"이름: {name}, 나이: {age}")
```

### 입력 (input)
```python
# 사용자 입력 받기
name = input("이름을 입력하세요: ")
age = input("나이를 입력하세요: ")

# 입력은 항상 문자열로 받아짐
print(f"안녕하세요, {name}님! 나이는 {age}세입니다.")
print(type(age))  # <class 'str'>

# 숫자로 변환
age_int = int(age)
age_float = float(age)
```

## 6. 주석

```python
# 한 줄 주석

"""
여러 줄 주석
(문서화 문자열로도 사용)
"""

def function():
    """함수 설명 (docstring)"""
    pass
```

## 7. 들여쓰기와 코드 블록

### 들여쓰기 규칙
```python
# 올바른 들여쓰기 (4칸 또는 탭)
if True:
    print("들여쓰기된 코드")
    if True:
        print("더 깊은 들여쓰기")

# 잘못된 들여쓰기 (오류 발생)
if True:
print("들여쓰기 오류")  # IndentationError
```

### 자바와의 비교
```java
// 자바
if (condition) {
    System.out.println("중괄호 사용");
    if (anotherCondition) {
        System.out.println("중첩된 블록");
    }
}
```

```python
# 파이썬
if condition:
    print("들여쓰기 사용")
    if another_condition:
        print("중첩된 블록")
```

## 8. 변수 스코프

```python
# 전역 변수
global_var = "전역"

def function():
    # 지역 변수
    local_var = "지역"
    print(global_var)  # 전역 변수 접근 가능
    print(local_var)

# global 키워드로 전역 변수 수정
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)  # 1
```

## 9. 상수

```python
# 파이썬에는 상수 키워드가 없지만, 관례적으로 대문자 사용
PI = 3.14159
MAX_SIZE = 100

# 실제로는 변경 가능하지만, 관례적으로 변경하지 않음
```

## 10. 실습 예제

### 계산기 프로그램
```python
def simple_calculator():
    print("간단한 계산기")
    
    num1 = float(input("첫 번째 숫자: "))
    operator = input("연산자 (+, -, *, /): ")
    num2 = float(input("두 번째 숫자: "))
    
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
            print("0으로 나눌 수 없습니다!")
            return
    else:
        print("잘못된 연산자입니다!")
        return
    
    print(f"결과: {num1} {operator} {num2} = {result}")

# 실행
simple_calculator()
```

### 문자열 처리 프로그램
```python
def text_processor():
    text = input("텍스트를 입력하세요: ")
    
    print(f"원본: {text}")
    print(f"길이: {len(text)}")
    print(f"대문자: {text.upper()}")
    print(f"소문자: {text.lower()}")
    print(f"단어 수: {len(text.split())}")
    print(f"역순: {text[::-1]}")

# 실행
text_processor()
```

## 11. 자바/리액트 개발자를 위한 팁

### 자바와의 주요 차이점
1. **세미콜론 불필요**: 파이썬은 줄바꿈으로 문장 구분
2. **타입 선언 불필요**: 동적 타입 언어
3. **중괄호 대신 들여쓰기**: 코드 블록 구분
4. **변수명 규칙**: snake_case 사용 (자바는 camelCase)

### 리액트와의 공통점
1. **템플릿 리터럴**: f-string은 JavaScript의 template literal과 유사
2. **함수형 스타일**: 람다, map, filter 등 지원
3. **동적 타입**: TypeScript 없이도 동작

### 다음 학습 단계
1. 데이터 구조 (리스트, 딕셔너리, 튜플)
2. 제어 구조 (조건문, 반복문)
3. 함수 정의와 사용
4. 예외 처리

---

**주의사항**
- 들여쓰기는 일관성 있게 사용 (4칸 권장)
- 변수명은 의미있게 작성
- 주석을 적절히 활용하여 코드 가독성 향상
