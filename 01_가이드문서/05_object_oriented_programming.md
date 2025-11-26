# 파이썬 객체지향 프로그래밍

## 1. 클래스와 객체 기본

### 클래스 정의와 객체 생성
```python
# 기본 클래스 정의
class Person:
    # 클래스 변수 (모든 인스턴스가 공유)
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        # 인스턴스 변수 (각 객체마다 독립적)
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"안녕하세요, 저는 {self.name}이고 {self.age}세입니다."
    
    def have_birthday(self):
        self.age += 1
        print(f"{self.name}의 생일! 이제 {self.age}세입니다.")

# 객체 생성
person1 = Person("김철수", 25)
person2 = Person("이영희", 30)

# 메서드 호출
print(person1.introduce())  # 안녕하세요, 저는 김철수이고 25세입니다.
person1.have_birthday()     # 김철수의 생일! 이제 26세입니다.

# 속성 접근
print(person1.name)         # 김철수
print(Person.species)       # Homo sapiens
```

### 자바와의 비교
```java
// 자바 클래스
public class Person {
    private String name;
    private int age;
    public static String species = "Homo sapiens";
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public String introduce() {
        return "안녕하세요, 저는 " + name + "이고 " + age + "세입니다.";
    }
    
    public void haveBirthday() {
        age++;
        System.out.println(name + "의 생일! 이제 " + age + "세입니다.");
    }
}
```

```python
# 파이썬 클래스
class Person:
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"안녕하세요, 저는 {self.name}이고 {self.age}세입니다."
    
    def have_birthday(self):
        self.age += 1
        print(f"{self.name}의 생일! 이제 {self.age}세입니다.")
```

## 2. 캡슐화 (Encapsulation)

### 접근 제어
```python
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.__balance = initial_balance  # private (이중 언더스코어)
        self._last_transaction = None     # protected (단일 언더스코어)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._last_transaction = f"입금: {amount}"
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._last_transaction = f"출금: {amount}"
            return True
        return False
    
    def get_balance(self):
        return self.__balance
    
    def get_last_transaction(self):
        return self._last_transaction

# 사용 예제
account = BankAccount("123456", 1000)
print(account.get_balance())  # 1000

account.deposit(500)
print(account.get_balance())  # 1500

# 직접 접근 시도 (권장하지 않음)
# print(account.__balance)  # AttributeError
print(account._BankAccount__balance)  # 1500 (name mangling)
```

### 프로퍼티 (Property)
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("반지름은 0 이상이어야 합니다.")
        self._radius = value
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2
    
    @property
    def circumference(self):
        return 2 * 3.14159 * self._radius

# 사용 예제
circle = Circle(5)
print(f"반지름: {circle.radius}")        # 5
print(f"면적: {circle.area:.2f}")        # 78.54
print(f"둘레: {circle.circumference:.2f}") # 31.42

circle.radius = 10
print(f"새 반지름: {circle.radius}")      # 10
```

## 3. 상속 (Inheritance)

### 기본 상속
```python
# 부모 클래스
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "일반적인 동물 소리"
    
    def move(self):
        return f"{self.name}이(가) 움직입니다."

# 자식 클래스
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canis lupus")  # 부모 클래스 초기화
        self.breed = breed
    
    def make_sound(self):  # 메서드 오버라이딩
        return "멍멍!"
    
    def fetch(self):  # 새로운 메서드
        return f"{self.name}이(가) 공을 가져옵니다."

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Felis catus")
        self.color = color
    
    def make_sound(self):
        return "야옹!"
    
    def climb(self):
        return f"{self.name}이(가) 나무를 올라갑니다."

# 사용 예제
dog = Dog("멍멍이", "골든리트리버")
cat = Cat("야옹이", "검은색")

print(dog.make_sound())  # 멍멍!
print(cat.make_sound())  # 야옹!
print(dog.fetch())       # 멍멍이이(가) 공을 가져옵니다.
print(cat.climb())       # 야옹이이(가) 나무를 올라갑니다.
```

### 다중 상속
```python
class Flyable:
    def fly(self):
        return "날고 있습니다."

class Swimmable:
    def swim(self):
        return "수영하고 있습니다."

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name, "Anas platyrhynchos")
    
    def make_sound(self):
        return "꽥꽥!"

# 사용 예제
duck = Duck("도날드")
print(duck.make_sound())  # 꽥꽥!
print(duck.fly())         # 날고 있습니다.
print(duck.swim())        # 수영하고 있습니다.
```

## 4. 다형성 (Polymorphism)

### 메서드 오버라이딩
```python
class Shape:
    def area(self):
        raise NotImplementedError("서브클래스에서 구현해야 합니다.")
    
    def perimeter(self):
        raise NotImplementedError("서브클래스에서 구현해야 합니다.")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

# 다형성 활용
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Rectangle(2, 8)
]

for shape in shapes:
    print(f"면적: {shape.area():.2f}, 둘레: {shape.perimeter():.2f}")
```

## 5. 특수 메서드 (Magic Methods)

### 주요 특수 메서드들
```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):  # str() 함수나 print()에서 사용
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):  # 개발자용 표현
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):  # len() 함수에서 사용
        return self.pages
    
    def __eq__(self, other):  # == 연산자
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False
    
    def __lt__(self, other):  # < 연산자
        if isinstance(other, Book):
            return self.pages < other.pages
        return NotImplemented
    
    def __add__(self, other):  # + 연산자
        if isinstance(other, Book):
            return Book(
                f"{self.title} & {other.title}",
                f"{self.author} & {other.author}",
                self.pages + other.pages
            )
        return NotImplemented

# 사용 예제
book1 = Book("파이썬 프로그래밍", "김개발", 300)
book2 = Book("자바 프로그래밍", "이코딩", 250)

print(book1)                    # '파이썬 프로그래밍' by 김개발
print(len(book1))               # 300
print(book1 == book2)           # False
print(book1 < book2)            # False (300 < 250)
print(book1 + book2)            # '파이썬 프로그래밍 & 자바 프로그래밍' by 김개발 & 이코딩
```

## 6. 실습 예제

### 도서관 관리 시스템
```python
class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False
        self.borrower = None
    
    def __str__(self):
        status = "대출 중" if self.is_borrowed else "대출 가능"
        return f"'{self.title}' by {self.author} ({self.year}) - {status}"
    
    def borrow(self, borrower_name):
        if not self.is_borrowed:
            self.is_borrowed = True
            self.borrower = borrower_name
            return True
        return False
    
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            self.borrower = None
            return True
        return False

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = set()
    
    def add_book(self, book):
        self.books.append(book)
        print(f"도서 '{book.title}'이 추가되었습니다.")
    
    def register_member(self, member_name):
        self.members.add(member_name)
        print(f"회원 '{member_name}'이 등록되었습니다.")
    
    def search_books(self, keyword):
        found_books = []
        for book in self.books:
            if (keyword.lower() in book.title.lower() or 
                keyword.lower() in book.author.lower()):
                found_books.append(book)
        return found_books
    
    def borrow_book(self, isbn, member_name):
        if member_name not in self.members:
            print("등록되지 않은 회원입니다.")
            return False
        
        for book in self.books:
            if book.isbn == isbn:
                if book.borrow(member_name):
                    print(f"'{book.title}'이 {member_name}님에게 대출되었습니다.")
                    return True
                else:
                    print("이미 대출 중인 도서입니다.")
                    return False
        
        print("해당 도서를 찾을 수 없습니다.")
        return False
    
    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.return_book():
                    print(f"'{book.title}'이 반납되었습니다.")
                    return True
                else:
                    print("대출되지 않은 도서입니다.")
                    return False
        
        print("해당 도서를 찾을 수 없습니다.")
        return False
    
    def show_all_books(self):
        if not self.books:
            print("등록된 도서가 없습니다.")
            return
        
        print(f"\n=== {self.name} 도서 목록 ===")
        for book in self.books:
            print(book)
    
    def show_available_books(self):
        available_books = [book for book in self.books if not book.is_borrowed]
        
        if not available_books:
            print("대출 가능한 도서가 없습니다.")
            return
        
        print("\n=== 대출 가능한 도서 ===")
        for book in available_books:
            print(book)

# 사용 예제
def library_system():
    library = Library("중앙도서관")
    
    # 도서 추가
    book1 = Book("978-1234567890", "파이썬 프로그래밍", "김개발", 2023)
    book2 = Book("978-0987654321", "자바 완벽 가이드", "이코딩", 2022)
    book3 = Book("978-1122334455", "데이터베이스 설계", "박데이터", 2023)
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    # 회원 등록
    library.register_member("김철수")
    library.register_member("이영희")
    
    # 도서 검색
    print("\n=== 도서 검색 ===")
    python_books = library.search_books("파이썬")
    for book in python_books:
        print(book)
    
    # 도서 대출
    print("\n=== 도서 대출 ===")
    library.borrow_book("978-1234567890", "김철수")
    library.borrow_book("978-0987654321", "이영희")
    
    # 도서 목록 확인
    library.show_all_books()
    
    # 대출 가능한 도서 확인
    library.show_available_books()
    
    # 도서 반납
    print("\n=== 도서 반납 ===")
    library.return_book("978-1234567890")

# 실행
library_system()
```

### 은행 계좌 시스템
```python
class BankAccount:
    def __init__(self, account_number, owner_name, initial_balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.__balance = initial_balance
        self.transaction_history = []
    
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transaction_history.append(f"입금: +{amount:,}원 (잔액: {self.__balance:,}원)")
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.transaction_history.append(f"출금: -{amount:,}원 (잔액: {self.__balance:,}원)")
            return True
        return False
    
    def transfer(self, other_account, amount):
        if self.withdraw(amount):
            if other_account.deposit(amount):
                self.transaction_history.append(f"이체: -{amount:,}원 → {other_account.owner_name}")
                other_account.transaction_history.append(f"이체: +{amount:,}원 ← {self.owner_name}")
                return True
            else:
                # 이체 실패 시 출금 취소
                self.__balance += amount
                self.transaction_history.pop()
        return False
    
    def get_transaction_history(self):
        return self.transaction_history.copy()
    
    def __str__(self):
        return f"계좌번호: {self.account_number}, 소유자: {self.owner_name}, 잔액: {self.__balance:,}원"

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.next_account_number = 1000
    
    def create_account(self, owner_name, initial_balance=0):
        account_number = str(self.next_account_number)
        self.next_account_number += 1
        
        account = BankAccount(account_number, owner_name, initial_balance)
        self.accounts[account_number] = account
        return account
    
    def get_account(self, account_number):
        return self.accounts.get(account_number)
    
    def show_all_accounts(self):
        if not self.accounts:
            print("등록된 계좌가 없습니다.")
            return
        
        print(f"\n=== {self.name} 계좌 목록 ===")
        for account in self.accounts.values():
            print(account)

# 사용 예제
def bank_system():
    bank = Bank("우리은행")
    
    # 계좌 생성
    account1 = bank.create_account("김철수", 100000)
    account2 = bank.create_account("이영희", 50000)
    
    print("계좌가 생성되었습니다:")
    print(account1)
    print(account2)
    
    # 입금
    account1.deposit(50000)
    account2.deposit(25000)
    
    # 출금
    account1.withdraw(30000)
    
    # 이체
    account1.transfer(account2, 20000)
    
    # 거래 내역 확인
    print(f"\n{account1.owner_name}의 거래 내역:")
    for transaction in account1.get_transaction_history():
        print(f"  {transaction}")
    
    print(f"\n{account2.owner_name}의 거래 내역:")
    for transaction in account2.get_transaction_history():
        print(f"  {transaction}")
    
    # 최종 잔액 확인
    print(f"\n최종 잔액:")
    print(account1)
    print(account2)

# 실행
bank_system()
```

## 7. 자바/리액트 개발자를 위한 비교

### 자바와의 주요 차이점
1. **접근 제어**: private, protected, public 키워드 대신 언더스코어 사용
2. **생성자**: `__init__` 메서드 사용
3. **상속**: `super()` 함수로 부모 클래스 호출
4. **인터페이스**: 추상 클래스나 프로토콜 사용
5. **다중 상속**: 지원 (자바는 인터페이스만 다중 상속)

### 리액트와의 공통점
1. **컴포넌트**: 클래스는 React 컴포넌트와 유사한 역할
2. **상태 관리**: 인스턴스 변수로 상태 관리
3. **메서드**: 클래스 메서드는 React의 메서드와 유사
4. **상속**: React 컴포넌트 상속과 유사한 개념

## 8. 다음 학습 단계

1. 예외 처리 (try-except)
2. 모듈과 패키지
3. 파일 입출력
4. 데코레이터

---

## 9. 실무 팁 및 자주 묻는 질문

### 9.1 상속 vs 유틸리티 클래스 임포트

#### 차이점 비교

| 항목 | 상속 (Inheritance) | 유틸리티 클래스 임포트 (Import) |
|------|-------------------|-------------------------------|
| **관계** | is-a 관계 (Dog is an Animal) | 독립적 사용 또는 has-a 관계 |
| **연결** | 부모-자식 클래스 관계 | 단순히 함수/클래스 가져오기 |
| **목적** | 코드 확장과 다형성 | 코드 재사용 |
| **사용 빈도** | ⭐⭐⭐ (보통) | ⭐⭐⭐⭐⭐ (매우 흔함) |
| **실무 활용** | 프레임워크, 공통 기능 확장 | 일반적인 기능 재사용 |

#### 상속 사용 예제

```python
# 상속: "Dog는 Animal이다" (is-a 관계)
class Animal:
    def make_sound(self):
        return "일반적인 동물 소리"
    
    def move(self):
        return "움직입니다"

class Dog(Animal):  # ✅ 상속: Dog는 Animal이다
    def make_sound(self):
        return "멍멍!"  # 오버라이딩

# 사용
dog = Dog("멍멍이")
print(dog.make_sound())  # "멍멍!" (Animal의 메서드 사용)
print(dog.move())        # "움직입니다" (Animal의 메서드 사용)
```

#### 유틸리티 임포트 사용 예제

```python
# utils.py - 유틸리티 모듈
def format_currency(amount):
    return f"${amount:,.2f}"

def validate_email(email):
    import re
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))

# main.py - 여러 곳에서 사용
from utils import format_currency, validate_email

class User:
    def __init__(self, email, balance):
        if validate_email(email):  # ✅ 유틸리티 사용
            self.email = email
        self.balance = balance
    
    def get_formatted_balance(self):
        return format_currency(self.balance)  # ✅ 유틸리티 사용
```

#### 실무 권장 사항

**✅ 유틸리티를 우선 사용:**
- 일반적인 기능 (포맷팅, 검증, 계산 등)
- 여러 클래스에서 재사용할 기능
- 독립적인 기능

**✅ 상속은 필요한 경우에만:**
- 프레임워크가 상속을 요구할 때 (Django, Flask 등)
- 공통 기능을 여러 클래스에 확장해야 할 때
- 다형성이 필요한 경우

### 9.2 언더스코어(`_`)와 접근 제어

#### 언더스코어 갯수별 의미

| 언더스코어 | 의미 | 접근 범위 | 예시 |
|-----------|------|----------|------|
| **없음** | Public (공개) | 어디서나 접근 가능 | `self.account_number` |
| **`_` 1개** | Protected (보호) | 클래스 내부 + 하위 클래스 | `self._last_transaction` |
| **`__` 2개** | Private (비공개) | 클래스 내부에서만 | `self.__balance` |

#### 실제 사용 예제

```python
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        # Public (언더스코어 없음)
        self.account_number = account_number
        # → 어디서나 접근 가능
        
        # Protected (언더스코어 1개)
        self._last_transaction = None
        # → 클래스 내부와 하위 클래스에서 접근 가능
        # → 외부에서도 접근 가능하지만 권장하지 않음
        
        # Private (언더스코어 2개)
        self.__balance = initial_balance
        # → 클래스 내부에서만 접근 가능
        # → 외부에서 직접 접근 불가

# 사용
account = BankAccount("123456", 1000)

# ✅ Public - 직접 접근 가능
print(account.account_number)  # "123456" ✅

# ⚠️ Protected - 접근 가능하지만 권장하지 않음
print(account._last_transaction)  # None (작동하지만 피해야 함)

# ❌ Private - 직접 접근 불가
# print(account.__balance)  # AttributeError! ❌

# ✅ Public 메서드를 통해서만 접근
print(account.get_balance())  # 1000 ✅
```

#### 중요 사항

- **순서와 무관:** 언더스코어 갯수로 결정됨 (선언 순서 무관)
- **Java 비교:** `public`, `protected`, `private`와 유사한 개념
- **key/value와 무관:** 접근 제어자일 뿐, 딕셔너리 key/value와는 다름

### 9.3 연산자 우선순위

#### Python 연산자

| 연산자 | 의미 | 우선순위 |
|--------|------|----------|
| `**` | 거듭제곱 (제곱) | 높음 |
| `*`, `/` | 곱하기, 나누기 | 중간 |
| `+`, `-` | 더하기, 빼기 | 낮음 |

#### 계산 순서 예제

```python
# 예제: 원의 면적 계산
3.14159 * 4 ** 2
# 계산 순서:
# 1. 4 ** 2 = 16 (먼저 계산 - 제곱)
# 2. 3.14159 * 16 = 50.27 (그 다음 계산 - 곱하기)

# 공식: c * a ** b
# = c * (a ** b)
# 1. a ** b 먼저 계산
# 2. c * (결과) 그 다음 계산
```

#### 실제 사용

```python
class Circle:
    def area(self):
        # 원의 면적 = π × 반지름²
        return 3.14159 * self.radius ** 2
        #                  ↑
        #                  먼저 계산: self.radius ** 2
        #                  그 다음: 3.14159 * (결과)

circle = Circle(4)
print(circle.area())  # 50.27
```

### 9.4 객체 생성과 인자 전달 플로우

#### 단계별 설명

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# 1단계: 객체 생성
rect = Rectangle(5, 3)
#        ↓
# __init__(self, width=5, height=3) 실행
#        ↓
# self.width = 5 저장
# self.height = 3 저장

# 2단계: 메서드 호출
result = rect.area()
#        ↓
# area(self=rect) 실행
#        ↓
# self.width = 5 (저장된 값 사용)
# self.height = 3 (저장된 값 사용)
#        ↓
# return 5 * 3 = 15 반환
```

#### 인자 전달 과정

```python
# 호출
account = BankAccount("12345", 1000)
#                     ↑       ↑
#                  계좌번호  초기 잔액

# 내부 동작
def __init__(self, account_number, initial_balance=0):
    # account_number = "12345" (첫 번째 인자)
    # initial_balance = 1000 (두 번째 인자)
    
    self.account_number = account_number
    # → self.account_number = "12345" 저장
    
    self.__balance = initial_balance
    # → self.__balance = 1000 저장
```

#### 매개변수 이름

- **자유롭게 정할 수 있음:** `radius`, `r`, `param` 등 모두 가능
- **의미 있는 이름 권장:** `radius` > `param` > `r`
- **Java와 동일:** Java도 매개변수 이름을 자유롭게 정할 수 있음

### 9.5 `raise` vs `return`

#### 차이점

| 항목 | `return` | `raise` |
|------|----------|---------|
| **의미** | 값을 반환하고 함수 종료 | 예외를 발생시키고 함수 종료 |
| **결과** | 정상 종료 | 에러 발생 |
| **호출자** | 반환값을 받음 | 예외를 처리해야 함 |
| **Java 비교** | `return` | `throw` |

#### 사용 예제

```python
# return - 값을 반환
def add(a, b):
    result = a + b
    return result  # ✅ 값을 반환하고 정상 종료

# raise - 예외 발생
def divide(a, b):
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다!")  # ❌ 예외 발생
    return a / b

# 사용
try:
    result = divide(10, 0)  # 예외 발생
except ValueError as e:  # 예외 처리
    print(f"에러: {e}")  # "에러: 0으로 나눌 수 없습니다!"
```

#### `raise` → `except` 흐름

```python
def check_age(age):
    if age < 0:
        raise ValueError("나이는 0 이상이어야 합니다!")  # 예외 발생
    return True

try:
    check_age(-5)  # 예외 발생
    print("검증 통과!")  # 실행 안 됨
except ValueError as e:  # 바로 여기로 점프!
    print(f"검증 실패: {e}")  # 실행됨
```

### 9.6 오버라이딩 vs 오버로딩

#### 비교표

| 항목 | 오버라이딩 (Overriding) | 오버로딩 (Overloading) |
|------|------------------------|------------------------|
| **의미** | 덮어쓰기 | 중복 정의 |
| **관계** | 상속 관계 (부모-자식) | 같은 클래스 내 |
| **메서드 이름** | 같음 | 같음 |
| **매개변수** | 같음 | 다름 (개수/타입) |
| **Python 지원** | ✅ 지원 | ❌ 직접 지원 안 함 |
| **Java 지원** | ✅ 지원 | ✅ 지원 |

#### 오버라이딩 예제

```python
# 부모 클래스
class Animal:
    def make_sound(self):
        return "일반적인 동물 소리"

# 자식 클래스
class Dog(Animal):
    def make_sound(self):  # ✅ 오버라이딩 (덮어쓰기)
        return "멍멍!"  # 부모 클래스의 make_sound()를 덮어씀

# 사용
animal = Animal()
dog = Dog()

print(animal.make_sound())  # "일반적인 동물 소리" ← 부모 클래스
print(dog.make_sound())     # "멍멍!" ← 자식 클래스 (덮어쓴 것)
```

#### 오버로딩 (Python에서는 직접 지원 안 함)

```python
# Python은 오버로딩 직접 지원 안 함
# 대신 기본값 인자나 *args 사용

class Calculator:
    def add(self, a, b, c=None):  # 기본값 인자 사용
        if c is None:
            return a + b  # 2개 인자
        else:
            return a + b + c  # 3개 인자

calc = Calculator()
print(calc.add(1, 2))      # 3 (2개 인자)
print(calc.add(1, 2, 3))   # 6 (3개 인자)
```

### 9.7 객체 생성 시 인자 전달

#### Java vs Python

**Java:**
```java
Circle circle = new Circle(5);
//        ↑      ↑   ↑      ↑
//      변수   할당 new  클래스명
//                  (5를 생성자로 전달)
```

**Python:**
```python
circle = Circle(5)
#      ↑   ↑      ↑
#    변수 할당 클래스명
#            (5를 __init__로 전달)
```

#### 핵심 이해

- `Circle`은 클래스 이름이지 인자가 아님
- `5`만 인자로 전달되어 `radius` 매개변수로 받음
- Java와 Python은 동일한 동작 (문법만 다름)

### 9.8 다형성 이해하기

#### 핵심 개념

**다형성 = 같은 메서드 이름, 다른 동작**

```python
class Shape:
    def area(self):
        raise NotImplementedError()

class Rectangle(Shape):
    def area(self):
        return self.width * self.height  # 사각형 계산

class Circle(Shape):
    def area(self):
        return 3.14159 * self.radius ** 2  # 원 계산

# 다형성 활용
shapes = [
    Rectangle(5, 3),   # shape[0]
    Circle(4),         # shape[1]
    Rectangle(2, 8)    # shape[2]
]

for shape in shapes:
    # 같은 area() 메서드지만 다른 계산!
    print(shape.area())
    # 15.00 (Rectangle.area() 실행)
    # 50.27 (Circle.area() 실행)
    # 16.00 (Rectangle.area() 실행)
```

#### 데이터 흐름

```
1. Rectangle(5, 3) 호출
   ↓
2. __init__(self, width=5, height=3) 실행
   ↓
3. self.width = 5 저장
   self.height = 3 저장
   ↓
4. rect.area() 호출
   ↓
5. area() 메서드에서 self.width(5)와 self.height(3) 사용
   ↓
6. return 5 * 3 = 15 반환
```

---

**핵심 포인트**
- 클래스: 객체의 청사진
- 상속: 코드 재사용과 확장
- 캡슐화: 데이터 보호와 인터페이스 제공
- 다형성: 같은 인터페이스로 다른 동작
- 특수 메서드: 연산자 오버로딩과 내장 함수 지원
- 실무 팁: 유틸리티를 우선 사용, 상속은 필요한 경우에만
