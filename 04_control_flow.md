# 파이썬 제어 구조

## 1. 조건문 (if, elif, else)

### 기본 조건문
```python
# 기본 if 문
age = 20
if age >= 18:
    print("성인입니다.")

# if-else 문
score = 85
if score >= 90:
    print("A등급")
else:
    print("B등급 이하")

# if-elif-else 문
score = 75
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"등급: {grade}")
```

### 중첩 조건문
```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("운전 가능합니다.")
    else:
        print("면허가 필요합니다.")
else:
    print("미성년자는 운전할 수 없습니다.")
```

### 논리 연산자
```python
# and, or, not
age = 25
has_license = True
has_car = False

# and (모든 조건이 참)
if age >= 18 and has_license:
    print("운전 가능")

# or (하나라도 참)
if has_license or has_car:
    print("운전 관련 자격 있음")

# not (부정)
if not has_car:
    print("차가 없습니다")

# 복합 조건
if (age >= 18 and has_license) or has_car:
    print("운전 가능")
```

### 삼항 연산자 (조건부 표현식)
```python
# 기본 문법: 값1 if 조건 else 값2
age = 20
status = "성인" if age >= 18 else "미성년자"
print(status)

# 중첩 삼항 연산자
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(f"등급: {grade}")
```

## 2. 반복문

### for 반복문
```python
# 기본 for 문
fruits = ["사과", "바나나", "오렌지"]
for fruit in fruits:
    print(fruit)

# range() 사용
for i in range(5):        # 0부터 4까지
    print(i)

for i in range(1, 6):     # 1부터 5까지
    print(i)

for i in range(0, 10, 2): # 0부터 9까지 2씩 증가
    print(i)

# enumerate() - 인덱스와 값 함께
fruits = ["사과", "바나나", "오렌지"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 딕셔너리 반복
person = {"name": "김철수", "age": 25, "city": "서울"}
for key, value in person.items():
    print(f"{key}: {value}")
```

### while 반복문
```python
# 기본 while 문
count = 0
while count < 5:
    print(f"카운트: {count}")
    count += 1

# 사용자 입력 받기
while True:
    user_input = input("종료하려면 'quit' 입력: ")
    if user_input.lower() == "quit":
        break
    print(f"입력: {user_input}")

# 조건부 while 문
number = 0
while number < 10:
    if number % 2 == 0:
        print(f"짝수: {number}")
    number += 1
```

### 반복문 제어 (break, continue, else)
```python
# break - 반복문 종료
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# continue - 다음 반복으로 건너뛰기
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1, 3, 5, 7, 9

# else - 반복문이 정상적으로 완료되었을 때 실행
for i in range(5):
    print(i)
else:
    print("반복문이 정상적으로 완료되었습니다.")

# break로 종료되면 else 실행 안됨
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("이 메시지는 출력되지 않습니다.")
```

## 3. 함수 (Function)

### 함수 정의와 호출
```python
# 기본 함수 정의
def greet():
    print("안녕하세요!")

# 함수 호출
greet()

# 매개변수가 있는 함수
def greet_person(name):
    print(f"안녕하세요, {name}님!")

greet_person("김철수")

# 여러 매개변수
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  # 8

# 기본값 매개변수
def greet_with_title(name, title="님"):
    print(f"안녕하세요, {name}{title}!")

greet_with_title("김철수")           # 안녕하세요, 김철수님!
greet_with_title("김철수", "씨")     # 안녕하세요, 김철수씨!
```

### 가변 매개변수
```python
# *args - 가변 위치 인수
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))  # 15
print(sum_all(10, 20))         # 30

# **kwargs - 가변 키워드 인수
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="김철수", age=25, city="서울")

# 혼합 사용
def complex_function(required, *args, **kwargs):
    print(f"필수: {required}")
    print(f"위치 인수: {args}")
    print(f"키워드 인수: {kwargs}")

complex_function("필수값", 1, 2, 3, name="김철수", age=25)
```

### 람다 함수 (Lambda)
```python
# 기본 람다 함수
square = lambda x: x ** 2
print(square(5))  # 25

# 여러 매개변수
add = lambda x, y: x + y
print(add(3, 4))  # 7

# 내장 함수와 함께 사용
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# 필터링
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# 정렬
students = [("김철수", 85), ("이영희", 92), ("박민수", 78)]
students.sort(key=lambda x: x[1], reverse=True)  # 성적으로 내림차순 정렬
print(students)
```

### 함수의 스코프
```python
# 전역 변수와 지역 변수
global_var = "전역 변수"

def function_scope():
    local_var = "지역 변수"
    print(global_var)  # 전역 변수 접근 가능
    print(local_var)

function_scope()
# print(local_var)  # 오류: 지역 변수는 함수 밖에서 접근 불가

# global 키워드
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)  # 1

# nonlocal 키워드 (중첩 함수)
def outer_function():
    outer_var = "외부 함수 변수"
    
    def inner_function():
        nonlocal outer_var
        outer_var = "수정된 외부 함수 변수"
    
    inner_function()
    print(outer_var)

outer_function()
```

## 4. 실습 예제

### 계산기 프로그램
```python
def calculator():
    """간단한 계산기 프로그램"""
    
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "0으로 나눌 수 없습니다."
    
    operations = {
        "1": ("덧셈", add),
        "2": ("뺄셈", subtract),
        "3": ("곱셈", multiply),
        "4": ("나눗셈", divide)
    }
    
    while True:
        print("\n=== 계산기 ===")
        print("1. 덧셈")
        print("2. 뺄셈")
        print("3. 곱셈")
        print("4. 나눗셈")
        print("5. 종료")
        
        choice = input("선택하세요 (1-5): ")
        
        if choice == "5":
            print("계산기를 종료합니다.")
            break
        
        if choice in operations:
            try:
                num1 = float(input("첫 번째 숫자: "))
                num2 = float(input("두 번째 숫자: "))
                
                operation_name, operation_func = operations[choice]
                result = operation_func(num1, num2)
                print(f"{operation_name} 결과: {result}")
                
            except ValueError:
                print("올바른 숫자를 입력하세요.")
        else:
            print("잘못된 선택입니다.")

# 실행
calculator()
```

### 숫자 맞추기 게임
```python
import random

def number_guessing_game():
    """숫자 맞추기 게임"""
    
    def play_game():
        secret_number = random.randint(1, 100)
        attempts = 0
        max_attempts = 7
        
        print("1부터 100 사이의 숫자를 맞춰보세요!")
        print(f"최대 {max_attempts}번의 기회가 있습니다.")
        
        while attempts < max_attempts:
            try:
                guess = int(input(f"추측 (남은 기회: {max_attempts - attempts}): "))
                attempts += 1
                
                if guess == secret_number:
                    print(f"축하합니다! {attempts}번 만에 맞췄습니다!")
                    return True
                elif guess < secret_number:
                    print("더 큰 숫자입니다.")
                else:
                    print("더 작은 숫자입니다.")
                    
            except ValueError:
                print("올바른 숫자를 입력하세요.")
                attempts -= 1
        
        print(f"게임 오버! 정답은 {secret_number}였습니다.")
        return False
    
    # 메인 게임 루프
    while True:
        print("\n=== 숫자 맞추기 게임 ===")
        print("1. 게임 시작")
        print("2. 종료")
        
        choice = input("선택하세요 (1-2): ")
        
        if choice == "1":
            play_game()
        elif choice == "2":
            print("게임을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.")

# 실행
number_guessing_game()
```

### 성적 관리 시스템
```python
def grade_management_system():
    """성적 관리 시스템"""
    
    students = {}
    
    def add_student():
        name = input("학생 이름: ")
        try:
            grade = float(input("성적: "))
            if 0 <= grade <= 100:
                students[name] = grade
                print(f"{name} 학생이 추가되었습니다.")
            else:
                print("성적은 0-100 사이여야 합니다.")
        except ValueError:
            print("올바른 성적을 입력하세요.")
    
    def calculate_grade(score):
        """성적을 등급으로 변환"""
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
    
    def show_statistics():
        """통계 정보 표시"""
        if not students:
            print("등록된 학생이 없습니다.")
            return
        
        scores = list(students.values())
        avg_score = sum(scores) / len(scores)
        max_score = max(scores)
        min_score = min(scores)
        
        print(f"\n=== 성적 통계 ===")
        print(f"총 학생 수: {len(students)}")
        print(f"평균 성적: {avg_score:.2f}")
        print(f"최고 성적: {max_score}")
        print(f"최저 성적: {min_score}")
        
        # 등급별 분포
        grade_distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
        for score in scores:
            grade = calculate_grade(score)
            grade_distribution[grade] += 1
        
        print("\n등급별 분포:")
        for grade, count in grade_distribution.items():
            print(f"{grade}등급: {count}명")
    
    # 메인 메뉴
    while True:
        print("\n=== 성적 관리 시스템 ===")
        print("1. 학생 추가")
        print("2. 성적 조회")
        print("3. 전체 학생 목록")
        print("4. 통계 보기")
        print("5. 종료")
        
        choice = input("선택하세요 (1-5): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            name = input("조회할 학생 이름: ")
            if name in students:
                score = students[name]
                grade = calculate_grade(score)
                print(f"{name}: {score}점 ({grade}등급)")
            else:
                print("해당 학생을 찾을 수 없습니다.")
        elif choice == "3":
            if students:
                print("\n전체 학생 성적:")
                for name, score in sorted(students.items()):
                    grade = calculate_grade(score)
                    print(f"{name}: {score}점 ({grade}등급)")
            else:
                print("등록된 학생이 없습니다.")
        elif choice == "4":
            show_statistics()
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.")

# 실행
grade_management_system()
```

## 5. 자바/리액트 개발자를 위한 비교

### 자바와의 비교
```java
// 자바 조건문
if (age >= 18) {
    System.out.println("성인입니다.");
} else if (age >= 13) {
    System.out.println("청소년입니다.");
} else {
    System.out.println("어린이입니다.");
}

// 자바 반복문
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

// 자바 함수
public static int add(int a, int b) {
    return a + b;
}
```

```python
# 파이썬 조건문
if age >= 18:
    print("성인입니다.")
elif age >= 13:
    print("청소년입니다.")
else:
    print("어린이입니다.")

# 파이썬 반복문
for i in range(5):
    print(i)

# 파이썬 함수
def add(a, b):
    return a + b
```

### 리액트와의 비교
```javascript
// JavaScript 조건부 렌더링
const Component = ({ age }) => {
  if (age >= 18) {
    return <div>성인입니다.</div>;
  } else if (age >= 13) {
    return <div>청소년입니다.</div>;
  } else {
    return <div>어린이입니다.</div>;
  }
};

// JavaScript 배열 메서드
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(x => x * 2);
const evens = numbers.filter(x => x % 2 === 0);
```

```python
# 파이썬 리스트 컴프리헨션
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
```

## 6. 다음 학습 단계

1. 예외 처리 (try-except)
2. 파일 입출력
3. 객체지향 프로그래밍
4. 모듈과 패키지

---

**핵심 포인트**
- 조건문: if, elif, else로 분기 처리
- 반복문: for, while로 반복 실행
- 함수: 코드 재사용과 모듈화
- 람다: 간단한 함수 정의
- 스코프: 변수의 접근 범위 이해
