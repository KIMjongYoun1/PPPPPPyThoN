ㅡ린# 파이썬 데이터 구조

## 1. 리스트 (List)

리스트는 자바의 ArrayList와 유사한 동적 배열입니다.

### 리스트 생성과 기본 연산
```python
# 리스트 생성
numbers = [1, 2, 3, 4, 5]
fruits = ["사과", "바나나", "오렌지"]
mixed = [1, "문자열", True, 3.14]  # 다양한 타입 혼합 가능

# 빈 리스트
empty_list = []
empty_list2 = list()

print(numbers)  # [1, 2, 3, 4, 5]
print(len(numbers))  # 5
```

### 리스트 인덱싱과 슬라이싱
```python
numbers = [10, 20, 30, 40, 50]

# 인덱싱 (0부터 시작)
print(numbers[0])    # 10 (첫 번째)
print(numbers[-1])   # 50 (마지막)
print(numbers[-2])   # 40 (뒤에서 두 번째)

# 슬라이싱 [시작:끝:간격]
print(numbers[1:4])     # [20, 30, 40] (1번부터 3번까지)
print(numbers[:3])      # [10, 20, 30] (처음부터 2번까지)
print(numbers[2:])      # [30, 40, 50] (2번부터 끝까지)
print(numbers[::2])     # [10, 30, 50] (2칸씩 건너뛰기)
print(numbers[::-1])    # [50, 40, 30, 20, 10] (역순)
```

### 리스트 메서드
```python
fruits = ["사과", "바나나"]

# 요소 추가
fruits.append("오렌지")        # 끝에 추가
fruits.insert(1, "포도")       # 특정 위치에 삽입
fruits.extend(["딸기", "키위"]) # 여러 요소 추가

print(fruits)  # ['사과', '포도', '바나나', '오렌지', '딸기', '키위']

# 요소 제거
fruits.remove("포도")          # 값으로 제거
popped = fruits.pop()          # 마지막 요소 제거하고 반환
popped_at = fruits.pop(1)      # 특정 인덱스 요소 제거

# 검색과 정렬
print(fruits.index("바나나"))  # 인덱스 찾기
print("사과" in fruits)        # 포함 여부 확인
fruits.sort()                  # 정렬 (원본 변경)
fruits.reverse()               # 역순 정렬

# 기타
print(fruits.count("사과"))    # 개수 세기
fruits.clear()                 # 모든 요소 제거
```

### 리스트 컴프리헨션 (List Comprehension)
```python
# 기본 문법: [표현식 for 항목 in 반복가능객체 if 조건]

# 1부터 10까지의 제곱
squares = [x**2 for x in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 짝수만 필터링
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)  # [2, 4, 6, 8, 10]

# 문자열 처리
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']
```

## 2. 딕셔너리 (Dictionary)

딕셔너리는 자바의 HashMap과 유사한 키-값 쌍을 저장하는 자료구조입니다.

### 딕셔너리 생성과 기본 연산
```python
# 딕셔너리 생성
person = {
    "name": "김철수",
    "age": 25,
    "city": "서울"
}

# 빈 딕셔너리
empty_dict = {}
empty_dict2 = dict()

# 접근
print(person["name"])     # 김철수
print(person.get("age"))  # 25 (안전한 접근)
print(person.get("job", "무직"))  # 키가 없으면 기본값 반환

# 수정과 추가
person["age"] = 26        # 수정
person["job"] = "개발자"  # 추가
print(person)
```

### 딕셔너리 메서드
```python
person = {"name": "김철수", "age": 25, "city": "서울"}

# 키, 값, 항목 접근
print(person.keys())      # dict_keys(['name', 'age', 'city'])
print(person.values())    # dict_values(['김철수', 25, '서울'])
print(person.items())     # dict_items([('name', '김철수'), ...])

# 반복문과 함께 사용
for key in person.keys():
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key}: {value}")

# 제거
del person["city"]        # 키로 제거
age = person.pop("age")   # 제거하고 값 반환
person.clear()            # 모든 항목 제거
```

### 딕셔너리 컴프리헨션
```python
# 기본 문법: {키표현식: 값표현식 for 항목 in 반복가능객체 if 조건}

# 숫자의 제곱 딕셔너리
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 조건부 딕셔너리
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

## 3. 튜플 (Tuple)

튜플은 불변(immutable) 리스트로, 자바의 final 배열과 유사합니다.

### 튜플 생성과 사용
```python
# 튜플 생성
coordinates = (10, 20)
colors = ("빨강", "녹색", "파랑")
single_tuple = (42,)  # 단일 요소 튜플 (쉼표 필요)

# 빈 튜플
empty_tuple = ()
empty_tuple2 = tuple()

# 접근 (리스트와 동일)
print(coordinates[0])    # 10
print(coordinates[-1])   # 20

# 불변성 (수정 불가)
# coordinates[0] = 30  # TypeError 발생

# 언패킹 (Unpacking)
x, y = coordinates
print(f"x: {x}, y: {y}")  # x: 10, y: 20

# 여러 값 반환
def get_name_age():
    return "김철수", 25

name, age = get_name_age()
print(f"이름: {name}, 나이: {age}")
```

## 4. 집합 (Set)

집합은 중복을 허용하지 않는 자료구조로, 자바의 HashSet과 유사합니다.

### 집합 생성과 연산
```python
# 집합 생성
fruits = {"사과", "바나나", "오렌지"}
numbers = set([1, 2, 3, 4, 5])

# 빈 집합
empty_set = set()  # {}는 딕셔너리이므로 주의

# 집합 연산
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1 | set2)   # 합집합: {1, 2, 3, 4, 5, 6}
print(set1 & set2)   # 교집합: {3, 4}
print(set1 - set2)   # 차집합: {1, 2}
print(set1 ^ set2)   # 대칭차집합: {1, 2, 5, 6}

# 집합 메서드
fruits.add("포도")           # 요소 추가
fruits.remove("바나나")      # 요소 제거 (없으면 오류)
fruits.discard("키위")       # 요소 제거 (없어도 오류 없음)
fruits.clear()               # 모든 요소 제거
```

## 5. 문자열 (String)

문자열도 시퀀스 타입으로, 리스트와 유사한 연산이 가능합니다.

### 문자열 시퀀스 연산
```python
text = "Hello, Python!"

# 인덱싱과 슬라이싱
print(text[0])        # H
print(text[-1])       # !
print(text[7:13])     # Python

# 문자열은 불변
# text[0] = 'h'  # TypeError 발생

# 문자열 메서드
print(text.upper())           # HELLO, PYTHON!
print(text.lower())           # hello, python!
print(text.replace("Python", "World"))  # Hello, World!
print(text.split(", "))       # ['Hello', 'Python!']
print(" ".join(["Hello", "World"]))     # Hello World
```

## 6. 실습 예제

### 학생 성적 관리 시스템
```python
def student_grade_manager():
    students = {}
    
    while True:
        print("\n=== 학생 성적 관리 시스템 ===")
        print("1. 학생 추가")
        print("2. 성적 조회")
        print("3. 성적 수정")
        print("4. 전체 학생 목록")
        print("5. 종료")
        
        choice = input("선택하세요 (1-5): ")
        
        if choice == "1":
            name = input("학생 이름: ")
            grade = float(input("성적: "))
            students[name] = grade
            print(f"{name} 학생이 추가되었습니다.")
            
        elif choice == "2":
            name = input("조회할 학생 이름: ")
            if name in students:
                print(f"{name}의 성적: {students[name]}")
            else:
                print("해당 학생을 찾을 수 없습니다.")
                
        elif choice == "3":
            name = input("수정할 학생 이름: ")
            if name in students:
                new_grade = float(input("새 성적: "))
                students[name] = new_grade
                print(f"{name}의 성적이 {new_grade}로 수정되었습니다.")
            else:
                print("해당 학생을 찾을 수 없습니다.")
                
        elif choice == "4":
            if students:
                print("\n전체 학생 성적:")
                for name, grade in students.items():
                    print(f"{name}: {grade}")
            else:
                print("등록된 학생이 없습니다.")
                
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.")

# 실행
student_grade_manager()
```

### 데이터 분석 예제
```python
def analyze_sales_data():
    # 판매 데이터
    sales_data = [
        {"product": "노트북", "price": 1200000, "quantity": 5},
        {"product": "마우스", "price": 25000, "quantity": 20},
        {"product": "키보드", "price": 80000, "quantity": 15},
        {"product": "모니터", "price": 300000, "quantity": 8},
        {"product": "헤드셋", "price": 150000, "quantity": 12}
    ]
    
    # 총 매출 계산
    total_revenue = sum(item["price"] * item["quantity"] for item in sales_data)
    print(f"총 매출: {total_revenue:,}원")
    
    # 상품별 매출
    product_revenue = {item["product"]: item["price"] * item["quantity"] 
                      for item in sales_data}
    
    print("\n상품별 매출:")
    for product, revenue in sorted(product_revenue.items(), 
                                 key=lambda x: x[1], reverse=True):
        print(f"{product}: {revenue:,}원")
    
    # 평균 단가
    avg_price = sum(item["price"] for item in sales_data) / len(sales_data)
    print(f"\n평균 상품 단가: {avg_price:,.0f}원")
    
    # 고가 상품 (30만원 이상)
    expensive_products = [item["product"] for item in sales_data 
                         if item["price"] >= 300000]
    print(f"고가 상품: {', '.join(expensive_products)}")

# 실행
analyze_sales_data()
```

## 7. 자바/리액트 개발자를 위한 비교

### 자바와의 비교
```java
// 자바
List<String> fruits = new ArrayList<>();
fruits.add("사과");
fruits.add("바나나");

Map<String, Integer> scores = new HashMap<>();
scores.put("김철수", 95);
scores.put("이영희", 87);
```

```python
# 파이썬
fruits = ["사과", "바나나"]
scores = {"김철수": 95, "이영희": 87}
```

### 리액트와의 비교
```javascript
// JavaScript
const fruits = ["사과", "바나나"];
const scores = {"김철수": 95, "이영희": 87};

// 배열 메서드
const doubled = numbers.map(x => x * 2);
const evens = numbers.filter(x => x % 2 === 0);
```

```python
# 파이썬
fruits = ["사과", "바나나"]
scores = {"김철수": 95, "이영희": 87}

# 리스트 컴프리헨션
doubled = [x * 2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
```

## 8. 성능 고려사항

### 시간 복잡도
- **리스트**: 인덱싱 O(1), 검색 O(n), 삽입/삭제 O(n)
- **딕셔너리**: 검색/삽입/삭제 O(1) 평균
- **집합**: 검색/삽입/삭제 O(1) 평균
- **튜플**: 인덱싱 O(1), 불변

### 메모리 효율성
```python
# 리스트 vs 튜플
import sys

list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)

print(sys.getsizeof(list_data))   # 더 많은 메모리 사용
print(sys.getsizeof(tuple_data))  # 더 적은 메모리 사용
```

## 9. 다음 학습 단계

1. 제어 구조 (조건문, 반복문)
2. 함수 정의와 사용
3. 예외 처리
4. 파일 입출력

---

**핵심 포인트**
- 리스트: 동적 배열, 수정 가능
- 딕셔너리: 키-값 쌍, 빠른 검색
- 튜플: 불변 시퀀스, 안전한 데이터
- 집합: 중복 제거, 집합 연산
- 컴프리헨션: 간결하고 효율적인 데이터 생성
