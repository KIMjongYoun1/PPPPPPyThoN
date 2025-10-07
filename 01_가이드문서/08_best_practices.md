# 파이썬 코딩 스타일 및 모범 사례

## 1. PEP 8 코딩 스타일 가이드

### 들여쓰기와 공백
```python
# 좋은 예: 4칸 들여쓰기 사용
def calculate_total(items):
    total = 0
    for item in items:
        if item.price > 0:
            total += item.price * item.quantity
    return total

# 나쁜 예: 탭과 공백 혼용, 일관성 없는 들여쓰기
def calculate_total(items):
	total = 0
    for item in items:
    	if item.price > 0:
        	total += item.price * item.quantity
	return total
```

### 줄 길이와 줄바꿈
```python
# 좋은 예: 79자 이하로 제한
def process_user_data(user_id, user_name, user_email, user_phone, 
                     user_address, user_birth_date):
    """사용자 데이터를 처리합니다."""
    pass

# 긴 문자열 처리
long_string = (
    "이것은 매우 긴 문자열입니다. "
    "여러 줄에 걸쳐 작성할 때는 "
    "괄호를 사용하여 연결합니다."
)

# 나쁜 예: 너무 긴 줄
def process_user_data(user_id, user_name, user_email, user_phone, user_address, user_birth_date, user_gender, user_occupation):
    pass
```

### 공백 사용
```python
# 좋은 예: 연산자 주변에 공백
result = a + b * c
if condition and other_condition:
    do_something()

# 함수 호출 시 공백 없음
function_call(arg1, arg2, arg3)

# 나쁜 예: 불필요한 공백
result = a+b*c
if condition and other_condition :
    do_something ( )
```

## 2. 명명 규칙 (Naming Conventions)

### 변수와 함수명
```python
# 좋은 예: snake_case 사용
user_name = "김철수"
user_age = 25
is_student = True

def calculate_total_price():
    pass

def get_user_info():
    pass

# 나쁜 예: camelCase 또는 다른 스타일
userName = "김철수"
userAge = 25
isStudent = True

def calculateTotalPrice():
    pass

def GetUserInfo():
    pass
```

### 클래스명
```python
# 좋은 예: PascalCase 사용
class UserManager:
    pass

class DatabaseConnection:
    pass

class FileProcessor:
    pass

# 나쁜 예: snake_case 사용
class user_manager:
    pass

class database_connection:
    pass
```

### 상수명
```python
# 좋은 예: 대문자와 언더스코어
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
API_BASE_URL = "https://api.example.com"

# 나쁜 예: 소문자 사용
max_connections = 100
default_timeout = 30
```

### 특수 메서드와 변수
```python
class MyClass:
    # 공개 메서드
    def public_method(self):
        pass
    
    # 내부 사용 메서드 (단일 언더스코어)
    def _internal_method(self):
        pass
    
    # 특수 메서드 (이중 언더스코어)
    def __special_method__(self):
        pass
    
    # 이름 맹글링 (이중 언더스코어)
    def __private_method(self):
        pass
```

## 3. 함수와 클래스 설계

### 함수 설계 원칙
```python
# 좋은 예: 단일 책임, 명확한 이름, 적절한 크기
def calculate_discount_price(original_price, discount_percentage):
    """할인된 가격을 계산합니다.
    
    Args:
        original_price (float): 원래 가격
        discount_percentage (float): 할인율 (0-100)
    
    Returns:
        float: 할인된 가격
    
    Raises:
        ValueError: 할인율이 유효하지 않은 경우
    """
    if not 0 <= discount_percentage <= 100:
        raise ValueError("할인율은 0-100 사이여야 합니다.")
    
    discount_amount = original_price * (discount_percentage / 100)
    return original_price - discount_amount

# 나쁜 예: 여러 책임, 모호한 이름, 너무 긴 함수
def process_data(data, type, format, save, email, notify):
    # 100줄의 복잡한 로직...
    pass
```

### 클래스 설계 원칙
```python
# 좋은 예: 단일 책임, 명확한 인터페이스
class EmailValidator:
    """이메일 주소 유효성을 검증하는 클래스"""
    
    def __init__(self):
        self.pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    def is_valid(self, email):
        """이메일 주소가 유효한지 확인"""
        import re
        return bool(re.match(self.pattern, email))
    
    def validate_and_raise(self, email):
        """이메일을 검증하고 유효하지 않으면 예외 발생"""
        if not self.is_valid(email):
            raise ValueError(f"유효하지 않은 이메일 주소: {email}")

# 나쁜 예: 여러 책임을 가진 클래스
class UserManager:
    def __init__(self):
        self.users = []
        self.emails = []
        self.database = None
        self.email_service = None
    
    def add_user(self, user):
        # 사용자 추가
        pass
    
    def send_email(self, user, message):
        # 이메일 발송
        pass
    
    def save_to_database(self, user):
        # 데이터베이스 저장
        pass
    
    def validate_email(self, email):
        # 이메일 검증
        pass
```

## 4. 예외 처리 (Exception Handling)

### 적절한 예외 처리
```python
# 좋은 예: 구체적인 예외 처리
def read_config_file(filename):
    """설정 파일을 읽어서 딕셔너리로 반환"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            import json
            return json.load(f)
    except FileNotFoundError:
        print(f"설정 파일을 찾을 수 없습니다: {filename}")
        return {}
    except json.JSONDecodeError as e:
        print(f"JSON 형식 오류: {e}")
        return {}
    except PermissionError:
        print(f"파일 읽기 권한이 없습니다: {filename}")
        return {}
    except Exception as e:
        print(f"예상치 못한 오류: {e}")
        return {}

# 나쁜 예: 너무 광범위한 예외 처리
def read_config_file(filename):
    try:
        with open(filename, 'r') as f:
            import json
            return json.load(f)
    except:
        return {}
```

### 커스텀 예외 클래스
```python
# 커스텀 예외 정의
class ValidationError(Exception):
    """유효성 검증 실패 시 발생하는 예외"""
    pass

class DatabaseConnectionError(Exception):
    """데이터베이스 연결 실패 시 발생하는 예외"""
    pass

class InsufficientFundsError(Exception):
    """잔액 부족 시 발생하는 예외"""
    def __init__(self, current_balance, required_amount):
        self.current_balance = current_balance
        self.required_amount = required_amount
        super().__init__(f"잔액 부족: 현재 {current_balance}, 필요 {required_amount}")

# 사용 예제
def withdraw_money(account, amount):
    if account.balance < amount:
        raise InsufficientFundsError(account.balance, amount)
    account.balance -= amount
    return account.balance
```

## 5. 문서화 (Documentation)

### Docstring 작성
```python
def calculate_compound_interest(principal, rate, time, compound_frequency=12):
    """복리 계산 함수
    
    이 함수는 주어진 원금, 이자율, 기간, 복리 빈도를 사용하여
    복리 이자를 계산합니다.
    
    Args:
        principal (float): 원금 (양수)
        rate (float): 연이자율 (소수점 형태, 예: 0.05 = 5%)
        time (float): 투자 기간 (년)
        compound_frequency (int, optional): 연간 복리 횟수. 기본값은 12.
    
    Returns:
        float: 복리 계산 결과 (원금 + 이자)
    
    Raises:
        ValueError: principal이 음수이거나 rate가 유효하지 않은 경우
        TypeError: 인수의 타입이 올바르지 않은 경우
    
    Examples:
        >>> calculate_compound_interest(1000, 0.05, 1)
        1051.16
        >>> calculate_compound_interest(1000, 0.05, 1, 1)
        1050.0
    
    Note:
        이 함수는 단순 복리 계산만 수행하며, 세금이나 수수료는 고려하지 않습니다.
    """
    if not isinstance(principal, (int, float)):
        raise TypeError("원금은 숫자여야 합니다.")
    if not isinstance(rate, (int, float)):
        raise TypeError("이자율은 숫자여야 합니다.")
    if principal < 0:
        raise ValueError("원금은 0 이상이어야 합니다.")
    if rate < 0 or rate > 1:
        raise ValueError("이자율은 0과 1 사이여야 합니다.")
    
    import math
    amount = principal * (1 + rate / compound_frequency) ** (compound_frequency * time)
    return round(amount, 2)
```

### 클래스 Docstring
```python
class BankAccount:
    """은행 계좌를 나타내는 클래스
    
    이 클래스는 은행 계좌의 기본적인 기능을 제공합니다:
    - 입금 및 출금
    - 잔액 조회
    - 거래 내역 관리
    
    Attributes:
        account_number (str): 계좌번호
        owner_name (str): 계좌 소유자 이름
        balance (float): 현재 잔액
        transaction_history (list): 거래 내역
    
    Example:
        >>> account = BankAccount("123456", "김철수")
        >>> account.deposit(1000)
        >>> account.withdraw(500)
        >>> print(account.balance)
        500.0
    """
    
    def __init__(self, account_number, owner_name, initial_balance=0):
        """계좌 초기화
        
        Args:
            account_number (str): 계좌번호
            owner_name (str): 계좌 소유자 이름
            initial_balance (float, optional): 초기 잔액. 기본값은 0.
        """
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = initial_balance
        self.transaction_history = []
```

## 6. 코드 품질 향상

### 리스트 컴프리헨션 활용
```python
# 좋은 예: 리스트 컴프리헨션 사용
def get_even_squares(numbers):
    """짝수의 제곱을 반환"""
    return [x**2 for x in numbers if x % 2 == 0]

# 나쁜 예: 반복문 사용
def get_even_squares(numbers):
    result = []
    for x in numbers:
        if x % 2 == 0:
            result.append(x**2)
    return result
```

### 제너레이터 활용
```python
# 좋은 예: 제너레이터 사용 (메모리 효율적)
def fibonacci_generator(n):
    """피보나치 수열의 n번째 항까지 생성"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 사용
for num in fibonacci_generator(10):
    print(num)

# 나쁜 예: 리스트로 모든 값을 저장
def fibonacci_list(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
```

### 컨텍스트 매니저 활용
```python
# 좋은 예: with 문 사용
def read_file_safely(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None

# 나쁜 예: 수동으로 파일 닫기
def read_file_unsafe(filename):
    try:
        f = open(filename, 'r', encoding='utf-8')
        content = f.read()
        f.close()  # 예외 발생 시 파일이 닫히지 않을 수 있음
        return content
    except FileNotFoundError:
        return None
```

## 7. 성능 최적화

### 효율적인 데이터 구조 사용
```python
# 좋은 예: set을 사용한 빠른 검색
def find_common_elements(list1, list2):
    """두 리스트의 공통 요소 찾기"""
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 & set2)

# 나쁜 예: 중첩 반복문 사용
def find_common_elements_slow(list1, list2):
    result = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2 and item1 not in result:
                result.append(item1)
    return result
```

### 캐싱 활용
```python
from functools import lru_cache

# 좋은 예: 메모이제이션 사용
@lru_cache(maxsize=128)
def fibonacci(n):
    """피보나치 수열 계산 (캐싱 적용)"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 나쁜 예: 캐싱 없이 반복 계산
def fibonacci_slow(n):
    if n < 2:
        return n
    return fibonacci_slow(n-1) + fibonacci_slow(n-2)
```

## 8. 테스트 작성

### 단위 테스트 예제
```python
import unittest
from unittest.mock import patch, MagicMock

class TestBankAccount(unittest.TestCase):
    """BankAccount 클래스의 단위 테스트"""
    
    def setUp(self):
        """각 테스트 전에 실행"""
        self.account = BankAccount("123456", "김철수", 1000)
    
    def test_deposit_positive_amount(self):
        """양수 입금 테스트"""
        result = self.account.deposit(500)
        self.assertEqual(result, 1500)
        self.assertEqual(self.account.balance, 1500)
    
    def test_deposit_negative_amount(self):
        """음수 입금 테스트"""
        with self.assertRaises(ValueError):
            self.account.deposit(-100)
    
    def test_withdraw_sufficient_balance(self):
        """충분한 잔액으로 출금 테스트"""
        result = self.account.withdraw(300)
        self.assertEqual(result, 700)
        self.assertEqual(self.account.balance, 700)
    
    def test_withdraw_insufficient_balance(self):
        """잔액 부족 시 출금 테스트"""
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(1500)
    
    def test_transaction_history(self):
        """거래 내역 테스트"""
        self.account.deposit(200)
        self.account.withdraw(100)
        
        self.assertEqual(len(self.account.transaction_history), 2)
        self.assertIn("입금: 200", self.account.transaction_history[0])
        self.assertIn("출금: 100", self.account.transaction_history[1])

# 테스트 실행
if __name__ == "__main__":
    unittest.main()
```

## 9. 프로젝트 구조

### 권장 프로젝트 구조
```
my_project/
├── README.md                 # 프로젝트 설명
├── requirements.txt          # 의존성 목록
├── setup.py                 # 패키지 설치 설정
├── .gitignore               # Git 무시 파일
├── .env.example             # 환경 변수 예제
├── src/                     # 소스 코드
│   └── my_project/
│       ├── __init__.py
│       ├── main.py
│       ├── models/          # 데이터 모델
│       ├── services/        # 비즈니스 로직
│       ├── utils/           # 유틸리티 함수
│       └── config/          # 설정 파일
├── tests/                   # 테스트 코드
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_services.py
│   └── test_utils.py
├── docs/                    # 문서
│   ├── api.md
│   └── user_guide.md
├── scripts/                 # 스크립트
│   ├── setup.py
│   └── deploy.py
└── data/                    # 데이터 파일
    ├── sample.json
    └── config.json
```

### requirements.txt 예제
```txt
# 프로덕션 의존성
requests>=2.28.0
numpy>=1.21.0
pandas>=1.3.0
flask>=2.0.0

# 개발 의존성
pytest>=7.0.0
pytest-cov>=4.0.0
black>=22.0.0
flake8>=5.0.0
mypy>=0.950

# 테스트 의존성
pytest-mock>=3.7.0
```

## 10. 자바/리액트 개발자를 위한 팁

### 자바와의 차이점
```java
// 자바: 명시적 타입 선언
public class User {
    private String name;
    private int age;
    
    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public String getName() {
        return name;
    }
}
```

```python
# 파이썬: 동적 타입, 간결한 문법
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def name(self):
        return self._name
```

### 리액트와의 공통점
```javascript
// React: 함수형 컴포넌트
const UserCard = ({ user, onEdit }) => {
  const [isEditing, setIsEditing] = useState(false);
  
  return (
    <div className="user-card">
      <h3>{user.name}</h3>
      <p>Age: {user.age}</p>
    </div>
  );
};
```

```python
# 파이썬: 함수형 프로그래밍 스타일
def process_users(users, processor):
    return [processor(user) for user in users if user.is_active]

def create_user_card(user):
    return {
        'name': user.name,
        'age': user.age,
        'display': f"{user.name} ({user.age}세)"
    }
```

## 11. 도구와 라이브러리

### 코드 품질 도구
```bash
# 코드 포맷팅
pip install black
black your_code.py

# 린팅
pip install flake8
flake8 your_code.py

# 타입 체킹
pip install mypy
mypy your_code.py

# 테스트 커버리지
pip install pytest-cov
pytest --cov=your_module tests/
```

### 개발 환경 설정
```bash
# 가상환경 생성
python -m venv myenv
source myenv/bin/activate  # Linux/Mac
# myenv\Scripts\activate  # Windows

# 의존성 설치
pip install -r requirements.txt

# 개발용 패키지 설치
pip install -r requirements-dev.txt
```

## 12. 다음 단계

1. **고급 파이썬 기능**
   - 데코레이터
   - 제너레이터와 이터레이터
   - 메타클래스

2. **웹 개발**
   - Flask/Django 프레임워크
   - REST API 개발
   - 데이터베이스 연동

3. **데이터 분석**
   - NumPy, Pandas
   - Matplotlib, Seaborn
   - Jupyter Notebook

4. **머신러닝**
   - Scikit-learn
   - TensorFlow/PyTorch
   - 데이터 전처리

5. **DevOps**
   - Docker
   - CI/CD
   - 클라우드 배포

---

**핵심 포인트**
- PEP 8 스타일 가이드 준수
- 명확하고 의미있는 이름 사용
- 적절한 예외 처리
- 문서화와 테스트 작성
- 성능과 가독성의 균형
- 지속적인 학습과 개선
