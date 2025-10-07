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

### 문자열 포맷팅 (String Formatting)

#### 💡 핵심 개념
문자열 안에 **변수 값을 넣는 방법**입니다.  
Java의 `String.format()`, `System.out.printf()`, 또는 `+` 연산자와 같은 역할입니다.

#### 🔹 방법 1: f-string (✅ 가장 권장!)

```python
name = "철수"
age = 25

# f-string: 문자열 앞에 f를 붙이고, {} 안에 변수를 직접 씀
message = f"안녕하세요, {name}님! 나이는 {age}세입니다."
print(message)
# 출력: 안녕하세요, 철수님! 나이는 25세입니다.
```

**Java 비교:**
```java
// Java 방식
String name = "철수";
int age = 25;

// 방법 1: + 연산자 (번거로움!)
String message = "안녕하세요, " + name + "님! 나이는 " + age + "세입니다.";

// 방법 2: String.format() (f-string과 유사)
String message = String.format("안녕하세요, %s님! 나이는 %d세입니다.", name, age);
```

**왜 f-string이 좋은가?**
- ✅ 읽기 쉬움: `{name}` 보면 바로 이해
- ✅ 타이핑 적음: `+` 연산자보다 훨씬 간결
- ✅ 실수 적음: 변수 순서 헷갈릴 일 없음

**f-string 상세 예제:**
```python
# 1. 변수 바로 넣기
name = "김철수"
print(f"이름: {name}")  # 이름: 김철수

# 2. 계산식도 가능!
age = 25
print(f"내년 나이: {age + 1}세")  # 내년 나이: 26세
print(f"10년 후: {age + 10}세")   # 10년 후: 35세

# 3. 여러 변수 사용
price = 1000
quantity = 5
print(f"가격: {price}원 × {quantity}개 = {price * quantity}원")
# 출력: 가격: 1000원 × 5개 = 5000원

# 4. 소수점 자릿수 지정
pi = 3.141592653589793
print(f"파이: {pi}")        # 파이: 3.141592653589793
print(f"파이: {pi:.2f}")    # 파이: 3.14 (소수점 2자리)
print(f"파이: {pi:.4f}")    # 파이: 3.1416 (소수점 4자리)

# 5. 천 단위 구분 (콤마)
big_num = 1234567890
print(f"금액: {big_num:,}원")  # 금액: 1,234,567,890원

# 6. 정렬 (왼쪽, 오른쪽, 가운데)
name = "김철수"
print(f"|{name:>10}|")  # |      김철수| (오른쪽 정렬, 10칸)
print(f"|{name:<10}|")  # |김철수      | (왼쪽 정렬)
print(f"|{name:^10}|")  # |   김철수   | (가운데 정렬)
```

#### 🔹 방법 2: format() 메서드

```python
name = "철수"
age = 25

# {} 안에 순서대로 값이 들어감
message = "안녕하세요, {}님! 나이는 {}세입니다.".format(name, age)
print(message)
# 출력: 안녕하세요, 철수님! 나이는 25세입니다.
```

**format() 상세 예제:**
```python
# 1. 기본 사용 (순서대로)
print("이름: {}, 나이: {}".format("김철수", 25))
# 출력: 이름: 김철수, 나이: 25

# 2. 인덱스 지정 (순서 바꿀 수 있음)
print("나이: {1}, 이름: {0}".format("김철수", 25))
# 출력: 나이: 25, 이름: 김철수

# 3. 이름 지정 (가독성 좋음)
print("이름: {name}, 나이: {age}".format(name="김철수", age=25))
# 출력: 이름: 김철수, 나이: 25

# 4. 같은 값 여러 번 사용
print("{0}님 환영합니다! {0}님의 등급은 VIP입니다.".format("김철수"))
# 출력: 김철수님 환영합니다! 김철수님의 등급은 VIP입니다.
```

**Java 비교:**
```java
// Java String.format()과 거의 동일!
String.format("이름: %s, 나이: %d", "김철수", 25);
// Python format()
"이름: {}, 나이: {}".format("김철수", 25)
```

#### 🔹 방법 3: % 포맷팅 (구식, 비추천)

```python
name = "철수"
age = 25

# C언어 스타일 (옛날 방식)
message = "안녕하세요, %s님! 나이는 %d세입니다." % (name, age)
print(message)
# 출력: 안녕하세요, 철수님! 나이는 25세입니다.
```

**% 포맷팅 설명:**
```python
# %s: 문자열 (string)
# %d: 정수 (decimal)
# %f: 실수 (float)

# 예제
print("문자열: %s" % "안녕")        # 문자열: 안녕
print("정수: %d" % 100)            # 정수: 100
print("실수: %f" % 3.14)           # 실수: 3.140000
print("실수: %.2f" % 3.14159)      # 실수: 3.14 (소수점 2자리)

# 여러 값
print("이름: %s, 나이: %d" % ("김철수", 25))
# 출력: 이름: 김철수, 나이: 25
```

**Java printf와 동일!**
```java
// Java
System.out.printf("이름: %s, 나이: %d\n", "김철수", 25);

// Python (똑같음!)
print("이름: %s, 나이: %d" % ("김철수", 25))
```

**왜 비추천?**
- ❌ 타입을 정확히 맞춰야 함 (%s, %d, %f 헷갈림)
- ❌ 여러 값 쓸 때 괄호 필요 `% (a, b, c)`
- ❌ f-string보다 가독성 떨어짐

#### 📊 세 가지 방법 비교

```python
name = "김철수"
age = 25
score = 95.5

# 1. f-string (가장 권장!) ✅
print(f"이름: {name}, 나이: {age}, 점수: {score:.1f}")

# 2. format() (괜찮음) 👍
print("이름: {}, 나이: {}, 점수: {:.1f}".format(name, age, score))

# 3. % 포맷팅 (구식) 👎
print("이름: %s, 나이: %d, 점수: %.1f" % (name, age, score))

# 모두 같은 출력:
# 이름: 김철수, 나이: 25, 점수: 95.5
```

#### 💡 실전 팁

**1. 디버깅할 때 (변수명도 같이 출력)**
```python
name = "김철수"
age = 25

# f-string의 꿀팁: = 붙이면 변수명도 출력!
print(f"{name=}")     # name='김철수'
print(f"{age=}")      # age=25
print(f"{age + 1=}")  # age + 1=26
```

**2. 여러 줄 문자열**
```python
name = "김철수"
age = 25
job = "개발자"

# 방법 1: + 연산자 (번거로움)
message = "이름: " + name + "\n" + \
          "나이: " + str(age) + "\n" + \
          "직업: " + job

# 방법 2: f-string (깔끔!)
message = f"""
이름: {name}
나이: {age}
직업: {job}
"""
print(message)
```

**3. Java 스타일과 비교**
```java
// Java - 번거로움!
String name = "김철수";
int age = 25;

String msg = "안녕하세요, " + name + "님! " + 
             "나이는 " + age + "세입니다.";

// Python - 간결!
name = "김철수"
age = 25
msg = f"안녕하세요, {name}님! 나이는 {age}세입니다."
```

#### 🎯 어떤 걸 사용해야 할까?

| 상황 | 추천 방법 |
|------|----------|
| **일반적인 경우** | `f-string` ✅ |
| **Python 3.5 이하** | `format()` |
| **복잡한 포맷팅** | `format()` |
| **옛날 코드 읽기** | `%` 이해만 하기 |

**결론: 무조건 f-string 사용하세요!** 🎉

```python
# ✅ 이렇게 쓰세요!
name = "김철수"
age = 25
print(f"안녕하세요, {name}님! {age}세입니다.")

# ❌ 이렇게 쓰지 마세요
print("안녕하세요, " + name + "님! " + str(age) + "세입니다.")
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
