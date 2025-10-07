# 🎯 Java 개발자를 위한 Python 기본 문법 완전 정복

## 목차
1. [print(f"...") - 문자열 포맷팅](#1-printf---문자열-포맷팅)
2. [\n, \t 등 - 이스케이프 시퀀스](#2-n-t-등---이스케이프-시퀀스)
3. [def __init__ - 생성자 메서드](#3-def-__init__---생성자-메서드)
4. [자주 보는 Python 기호들](#4-자주-보는-python-기호들)
5. [Java vs Python 비교표](#5-java-vs-python-비교표)

---

## 1. `print(f"...")` - 문자열 포맷팅

### ❓ `f`가 뭐죠?

**`f`는 "format"의 약자입니다!** 문자열 앞에 `f`를 붙이면 **변수를 문자열 안에 바로 넣을 수 있습니다.**

### Java vs Python 비교

#### Java 방식
```java
String name = "김철수";
int age = 25;
double height = 175.5;

// 방법 1: + 연산자
String message = "이름: " + name + ", 나이: " + age + "세";

// 방법 2: String.format()
String message = String.format("이름: %s, 나이: %d세", name, age);

// 방법 3: printf
System.out.printf("이름: %s, 나이: %d세\n", name, age);
```

#### Python 방식
```python
name = "김철수"
age = 25
height = 175.5

# ✅ 가장 권장: f-string (Python 3.6+)
message = f"이름: {name}, 나이: {age}세"
print(message)
# 출력: 이름: 김철수, 나이: 25세

# 변수뿐만 아니라 표현식도 가능!
print(f"내년 나이: {age + 1}세")
# 출력: 내년 나이: 26세

print(f"키: {height}cm, 미터로는 {height/100}m")
# 출력: 키: 175.5cm, 미터로는 1.755m
```

### f-string 상세 예제

```python
# 1. 기본 사용
name = "김철수"
print(f"안녕하세요, {name}님!")
# 출력: 안녕하세요, 김철수님!

# 2. 계산식 넣기
a = 10
b = 20
print(f"{a} + {b} = {a + b}")
# 출력: 10 + 20 = 30

# 3. 소수점 자릿수 지정
pi = 3.141592653589793
print(f"파이 값: {pi:.2f}")  # .2f = 소수점 2자리
# 출력: 파이 값: 3.14

# 4. 천 단위 구분
price = 1234567
print(f"가격: {price:,}원")
# 출력: 가격: 1,234,567원

# 5. 정렬
name = "김철수"
print(f"|{name:>10}|")  # 오른쪽 정렬 (10칸)
# 출력: |      김철수|

print(f"|{name:<10}|")  # 왼쪽 정렬
# 출력: |김철수      |

print(f"|{name:^10}|")  # 가운데 정렬
# 출력: |   김철수   |
```

### 다른 포맷팅 방법들

```python
name = "김철수"
age = 25

# 방법 1: f-string (최신, 가장 권장!)
message = f"이름: {name}, 나이: {age}"

# 방법 2: .format() (Python 2.7+)
message = "이름: {}, 나이: {}".format(name, age)
message = "이름: {0}, 나이: {1}".format(name, age)
message = "이름: {n}, 나이: {a}".format(n=name, a=age)

# 방법 3: % 포맷팅 (구식, 비추천)
message = "이름: %s, 나이: %d" % (name, age)
```

---

## 2. `\n`, `\t` 등 - 이스케이프 시퀀스

### ❓ `\n`이 뭐죠?

**백슬래시(`\`) + 문자** 조합으로 **특수한 기능**을 수행합니다.  
Java와 완전히 동일합니다!

### 자주 사용하는 이스케이프 시퀀스

| 시퀀스 | 의미 | Java와 동일? |
|--------|------|-------------|
| `\n` | 줄바꿈 (New line) | ✅ |
| `\t` | 탭 (Tab) | ✅ |
| `\\` | 백슬래시 자체 | ✅ |
| `\'` | 작은따옴표 | ✅ |
| `\"` | 큰따옴표 | ✅ |
| `\r` | 캐리지 리턴 | ✅ |
| `\b` | 백스페이스 | ✅ |

### 실제 예제

```python
# 1. \n - 줄바꿈
print("첫 번째 줄\n두 번째 줄\n세 번째 줄")
# 출력:
# 첫 번째 줄
# 두 번째 줄
# 세 번째 줄

# 2. \t - 탭
print("이름\t나이\t직업")
print("김철수\t25\t개발자")
print("이영희\t30\t디자이너")
# 출력:
# 이름    나이    직업
# 김철수  25      개발자
# 이영희  30      디자이너

# 3. \\ - 백슬래시 출력
print("파일 경로: C:\\Users\\Documents\\file.txt")
# 출력: 파일 경로: C:\Users\Documents\file.txt

# 4. \', \" - 따옴표 출력
print("그는 \"안녕\"이라고 말했다")
# 출력: 그는 "안녕"이라고 말했다

print('It\'s a beautiful day')
# 출력: It's a beautiful day

# 5. 여러 개 조합
print("=" * 50)
print("이름:\t김철수\n나이:\t25세\n직업:\t개발자")
print("=" * 50)
# 출력:
# ==================================================
# 이름:	김철수
# 나이:	25세
# 직업:	개발자
# ==================================================
```

### Java 비교

```java
// Java
System.out.println("첫 번째 줄\n두 번째 줄");
System.out.println("이름\t나이");
System.out.println("경로: C:\\Users\\file.txt");

// Python (똑같음!)
print("첫 번째 줄\n두 번째 줄")
print("이름\t나이")
print("경로: C:\\Users\\file.txt")
```

### 원시 문자열 (Raw String)

```python
# 이스케이프 시퀀스를 무시하고 싶을 때 (정규식 등에서 유용)
path = r"C:\Users\Documents\new_file.txt"
print(path)
# 출력: C:\Users\Documents\new_file.txt

# r이 없으면
path = "C:\Users\Documents\new_file.txt"
# \n이 줄바꿈으로 해석되어 오류 발생!
```

---

## 3. `def __init__` - 생성자 메서드

### ❓ `__init__`이 뭐죠?

**Java의 생성자(Constructor)와 똑같습니다!**  
객체가 생성될 때 자동으로 실행되는 메서드입니다.

### Java vs Python 비교

#### Java 방식
```java
public class User {
    private String name;
    private int age;
    
    // 생성자 (클래스명과 동일)
    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public void introduce() {
        System.out.println("이름: " + this.name);
        System.out.println("나이: " + this.age);
    }
}

// 사용
User user = new User("김철수", 25);
user.introduce();
```

#### Python 방식
```python
class User:
    # 생성자 (항상 __init__)
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"이름: {self.name}")
        print(f"나이: {self.age}")

# 사용
user = User("김철수", 25)  # new 키워드 없음!
user.introduce()
```

### `__init__` 상세 설명

```python
class User:
    # def: 함수 정의 키워드
    # __init__: 생성자 이름 (항상 고정!)
    # self: Java의 this (자기 자신 참조)
    # name, age: 매개변수
    def __init__(self, name, age):
        self.name = name    # self.name = 인스턴스 변수
        self.age = age
        print("User 객체가 생성되었습니다!")

# 객체 생성 시 자동으로 __init__ 호출됨
user = User("김철수", 25)
# 출력: User 객체가 생성되었습니다!

print(user.name)  # 김철수
print(user.age)   # 25
```

### `self`란?

```python
class User:
    def __init__(self, name):
        # self.name: 인스턴스 변수 (객체마다 다름)
        # name: 매개변수
        self.name = name
    
    def say_hello(self):
        # self를 통해 인스턴스 변수에 접근
        print(f"안녕하세요, {self.name}입니다!")

# self는 자동으로 전달됨
user1 = User("김철수")
user1.say_hello()  # 안녕하세요, 김철수입니다!

user2 = User("이영희")
user2.say_hello()  # 안녕하세요, 이영희입니다!
```

### Java vs Python 비교표

| 항목 | Java | Python |
|------|------|--------|
| 생성자 이름 | 클래스명과 동일 | `__init__` (고정) |
| this/self | `this` | `self` |
| new 키워드 | 필요 | 불필요 |
| 타입 선언 | 필요 | 불필요 |

```java
// Java
public class User {
    private String name;
    
    public User(String name) {  // 생성자
        this.name = name;
    }
}
User user = new User("김철수");
```

```python
# Python
class User:
    def __init__(self, name):  # 생성자
        self.name = name

user = User("김철수")  # new 없음!
```

---

## 4. 자주 보는 Python 기호들

### 언더스코어(_) 사용법

```python
# 1. __method__: 매직 메서드 (특수 메서드)
class User:
    def __init__(self):        # 생성자
        pass
    
    def __str__(self):         # toString()과 유사
        return "User 객체"
    
    def __repr__(self):        # 개발자용 문자열 표현
        return "User()"

# 2. _variable: 내부용 (Java의 private 관례)
class User:
    def __init__(self):
        self._internal = "내부용"  # 외부에서 사용하지 말 것을 권장
        self.public = "공개용"

# 3. __variable: 이름 맹글링 (강한 private)
class User:
    def __init__(self):
        self.__private = "진짜 private"

# 4. _: 임시 변수 (값이 중요하지 않을 때)
for _ in range(5):
    print("반복!")

# 5. 숫자 구분
big_number = 1_000_000  # 1000000과 동일 (가독성)
```

### 콜론(:) 사용법

```python
# 1. 함수/클래스 정의 시
def my_function():  # ← 콜론!
    print("함수 본문")

class MyClass:      # ← 콜론!
    pass

# 2. 조건문/반복문
if age > 18:        # ← 콜론!
    print("성인")

for i in range(5):  # ← 콜론!
    print(i)

# 3. 딕셔너리 (Java의 Map)
user = {
    "name": "김철수",  # key: value
    "age": 25
}

# 4. 슬라이싱
text = "Hello World"
print(text[0:5])    # Hello (0부터 5 전까지)
print(text[:5])     # Hello (처음부터 5 전까지)
print(text[6:])     # World (6부터 끝까지)
```

### 들여쓰기 (Indentation)

```python
# Python은 들여쓰기로 코드 블록 구분! (중괄호 없음!)

# Java
if (age > 18) {
    System.out.println("성인");
    System.out.println("투표 가능");
}

# Python (들여쓰기 필수!)
if age > 18:
    print("성인")
    print("투표 가능")
# 들여쓰기 안 맞으면 오류!
```

### 별표(*) 사용법

```python
# 1. 곱셈
print(3 * 4)        # 12

# 2. 거듭제곱
print(2 ** 3)       # 8 (2의 3승)

# 3. 문자열 반복
print("=" * 50)     # ================================================== (=을 50개)

# 4. 리스트 언패킹
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))  # add(1, 2, 3)과 동일

# 5. 딕셔너리 언패킹
def greet(name, age):
    print(f"{name}님은 {age}세입니다")

data = {"name": "김철수", "age": 25}
greet(**data)  # greet(name="김철수", age=25)와 동일
```

---

## 5. Java vs Python 비교표

### 기본 문법

| 기능 | Java | Python |
|------|------|--------|
| 변수 선언 | `String name = "김철수";` | `name = "김철수"` |
| 상수 | `final int MAX = 100;` | `MAX = 100` (관례상 대문자) |
| 출력 | `System.out.println("Hi");` | `print("Hi")` |
| 주석 | `// 한 줄`, `/* 여러 줄 */` | `# 한 줄`, `"""여러 줄"""` |
| 문자열 연결 | `"Hello " + name` | `f"Hello {name}"` |
| null | `null` | `None` |
| true/false | `true`, `false` | `True`, `False` |

### 클래스

| 기능 | Java | Python |
|------|------|--------|
| 클래스 정의 | `public class User { }` | `class User:` |
| 생성자 | `public User() { }` | `def __init__(self):` |
| 메서드 | `public void method() { }` | `def method(self):` |
| this/self | `this.name` | `self.name` |
| 객체 생성 | `new User()` | `User()` |
| toString | `public String toString() { }` | `def __str__(self):` |

### 조건문

```java
// Java
if (age > 18) {
    System.out.println("성인");
} else if (age > 13) {
    System.out.println("청소년");
} else {
    System.out.println("어린이");
}
```

```python
# Python
if age > 18:
    print("성인")
elif age > 13:
    print("청소년")
else:
    print("어린이")
```

### 반복문

```java
// Java
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

String[] names = {"김철수", "이영희"};
for (String name : names) {
    System.out.println(name);
}
```

```python
# Python
for i in range(5):
    print(i)

names = ["김철수", "이영희"]
for name in names:
    print(name)
```

---

## 6. 실전 예제: 종합

```python
# 1. 클래스 정의
class User:
    # 클래스 변수 (모든 인스턴스가 공유)
    total_users = 0
    
    # 생성자
    def __init__(self, name, age, email):
        # 인스턴스 변수
        self.name = name
        self.age = age
        self.email = email
        User.total_users += 1
        print(f"✅ {name}님이 가입하셨습니다!")
    
    # 메서드
    def introduce(self):
        print("=" * 50)
        print(f"이름:\t{self.name}")
        print(f"나이:\t{self.age}세")
        print(f"이메일:\t{self.email}")
        print("=" * 50)
    
    def is_adult(self):
        return self.age >= 18
    
    # __str__: Java의 toString()
    def __str__(self):
        return f"User(name={self.name}, age={self.age})"

# 2. 객체 생성 및 사용
user1 = User("김철수", 25, "kim@example.com")
user2 = User("이영희", 17, "lee@example.com")

# 3. 메서드 호출
user1.introduce()

# 4. 조건문
if user1.is_adult():
    print(f"{user1.name}님은 성인입니다.\n")
else:
    print(f"{user1.name}님은 미성년자입니다.\n")

if user2.is_adult():
    print(f"{user2.name}님은 성인입니다.\n")
else:
    print(f"{user2.name}님은 미성년자입니다.\n")

# 5. 클래스 변수 접근
print(f"총 사용자 수: {User.total_users}명")

# 6. 리스트 반복
users = [user1, user2]
print("\n전체 사용자 목록:")
print("-" * 50)
for i, user in enumerate(users, 1):
    print(f"{i}. {user.name} ({user.age}세)")
```

**출력:**
```
✅ 김철수님이 가입하셨습니다!
✅ 이영희님이 가입하셨습니다!
==================================================
이름:	김철수
나이:	25세
이메일:	kim@example.com
==================================================
김철수님은 성인입니다.

이영희님은 미성년자입니다.

총 사용자 수: 2명

전체 사용자 목록:
--------------------------------------------------
1. 김철수 (25세)
2. 이영희 (17세)
```

---

## 7. 꿀팁 모음

### print() 함수 옵션

```python
# 1. 줄바꿈 없이 출력 (end 옵션)
print("로딩 중", end="")
print(".", end="")
print(".", end="")
print(".")
# 출력: 로딩 중...

# 2. 구분자 변경 (sep 옵션)
print("김철수", "이영희", "박민수", sep=", ")
# 출력: 김철수, 이영희, 박민수

print(2025, 1, 15, sep="-")
# 출력: 2025-1-15

# 3. 여러 값 한번에 출력
name = "김철수"
age = 25
print("이름:", name, "나이:", age)
# 출력: 이름: 김철수 나이: 25
```

### 문자열 곱하기 (반복)

```python
# 구분선 쉽게 만들기
print("=" * 50)
print("제목")
print("=" * 50)

# 공백 만들기
print(" " * 10 + "중앙 정렬")

# 패턴 만들기
print("*-" * 20)  # *-*-*-*-*-... (40개)
```

---

이제 Python 기본 문법이 명확해지셨나요? 😊

**다음 단계:**
1. 이 문서를 천천히 읽어보기
2. 각 예제 코드를 직접 실행해보기
3. 궁금한 부분이 있으면 질문하기!

