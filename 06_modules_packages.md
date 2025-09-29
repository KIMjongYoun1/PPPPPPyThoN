# 파이썬 모듈과 패키지

## 1. 모듈 (Module) 기본

### 모듈이란?
모듈은 파이썬 코드를 담고 있는 파일입니다. 자바의 클래스 파일이나 JavaScript의 모듈과 유사합니다.

### 모듈 생성과 사용
```python
# math_utils.py 파일 생성
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

# 상수
PI = 3.14159
E = 2.71828

# 클래스
class Calculator:
    def __init__(self):
        self.history = []
    
    def calculate(self, operation, a, b):
        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)
        else:
            result = "알 수 없는 연산"
        
        self.history.append(f"{operation}({a}, {b}) = {result}")
        return result
```

### 모듈 임포트 방법
```python
# main.py 파일에서 math_utils 모듈 사용

# 1. 전체 모듈 임포트
import math_utils

result = math_utils.add(5, 3)
print(result)  # 8

calc = math_utils.Calculator()
print(calc.calculate("add", 10, 5))  # 15

# 2. 특정 함수/클래스만 임포트
from math_utils import add, subtract, Calculator

result = add(5, 3)
calc = Calculator()

# 3. 별칭 사용
import math_utils as math
from math_utils import add as addition

result = math.add(5, 3)
result2 = addition(5, 3)

# 4. 모든 것 임포트 (권장하지 않음)
from math_utils import *
```

## 2. 패키지 (Package)

### 패키지 구조
```
my_package/
├── __init__.py          # 패키지 초기화 파일
├── math_utils.py        # 수학 유틸리티 모듈
├── string_utils.py      # 문자열 유틸리티 모듈
└── data_utils.py        # 데이터 유틸리티 모듈
```

### __init__.py 파일
```python
# my_package/__init__.py
"""
my_package - 유틸리티 함수들을 모아놓은 패키지
"""

# 패키지 버전
__version__ = "1.0.0"

# 패키지에서 자주 사용하는 함수들을 직접 임포트
from .math_utils import add, subtract, multiply, divide
from .string_utils import format_name, clean_text
from .data_utils import save_data, load_data

# __all__ 변수로 공개할 모듈/함수 정의
__all__ = [
    'add', 'subtract', 'multiply', 'divide',
    'format_name', 'clean_text',
    'save_data', 'load_data'
]
```

### 개별 모듈들
```python
# my_package/math_utils.py
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
        raise ValueError("0으로 나눌 수 없습니다.")

# my_package/string_utils.py
def format_name(first_name, last_name):
    return f"{last_name}, {first_name}"

def clean_text(text):
    return text.strip().lower()

# my_package/data_utils.py
import json

def save_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
```

### 패키지 사용
```python
# 패키지 사용 예제
import my_package

# __init__.py에서 임포트한 함수들 직접 사용
result = my_package.add(5, 3)
formatted = my_package.format_name("철수", "김")

# 개별 모듈 임포트
from my_package import math_utils, string_utils

result = math_utils.multiply(4, 5)
cleaned = string_utils.clean_text("  HELLO WORLD  ")

# 특정 함수만 임포트
from my_package.math_utils import divide
from my_package.data_utils import save_data

result = divide(10, 2)
save_data({"name": "김철수", "age": 25}, "data.json")
```

## 3. 내장 모듈 사용

### 자주 사용하는 내장 모듈들
```python
# os 모듈 - 운영체제 관련 기능
import os

print(os.getcwd())  # 현재 작업 디렉토리
print(os.listdir())  # 현재 디렉토리 파일 목록
os.makedirs("new_folder", exist_ok=True)  # 디렉토리 생성

# sys 모듈 - 시스템 관련 기능
import sys

print(sys.version)  # 파이썬 버전
print(sys.argv)     # 명령행 인수
sys.exit(0)         # 프로그램 종료

# datetime 모듈 - 날짜와 시간
from datetime import datetime, timedelta

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 2023-12-07 14:30:25

tomorrow = now + timedelta(days=1)
print(tomorrow.date())

# random 모듈 - 난수 생성
import random

print(random.randint(1, 10))  # 1-10 사이의 정수
print(random.choice(["사과", "바나나", "오렌지"]))  # 리스트에서 랜덤 선택
random.shuffle([1, 2, 3, 4, 5])  # 리스트 섞기

# json 모듈 - JSON 데이터 처리
import json

data = {"name": "김철수", "age": 25, "city": "서울"}
json_string = json.dumps(data, ensure_ascii=False)
print(json_string)

parsed_data = json.loads(json_string)
print(parsed_data["name"])

# urllib 모듈 - URL 처리
import urllib.request
import urllib.parse

# URL 인코딩
params = {"q": "파이썬 프로그래밍", "page": 1}
encoded_params = urllib.parse.urlencode(params)
print(encoded_params)  # q=%ED%8C%8C%EC%9D%B4%EC%8D%AC+%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D&page=1
```

## 4. 외부 패키지 설치와 사용

### pip를 사용한 패키지 설치
```bash
# 기본 설치
pip install requests

# 특정 버전 설치
pip install requests==2.28.1

# 최신 버전으로 업그레이드
pip install --upgrade requests

# 개발용 패키지 설치
pip install -e .

# requirements.txt에서 설치
pip install -r requirements.txt

# 가상환경에서 설치
python -m venv myenv
source myenv/bin/activate  # Linux/Mac
# myenv\Scripts\activate  # Windows
pip install requests
```

### 외부 패키지 사용 예제
```python
# requests 패키지 - HTTP 요청
import requests

# GET 요청
response = requests.get("https://api.github.com/users/octocat")
if response.status_code == 200:
    data = response.json()
    print(f"사용자: {data['login']}")
    print(f"이름: {data['name']}")

# POST 요청
data = {"name": "김철수", "age": 25}
response = requests.post("https://httpbin.org/post", json=data)
print(response.json())

# numpy 패키지 - 수치 계산
import numpy as np

# 배열 생성
arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)  # [2 4 6 8 10]

# 2차원 배열
matrix = np.array([[1, 2], [3, 4]])
print(matrix.shape)  # (2, 2)

# pandas 패키지 - 데이터 분석
import pandas as pd

# 데이터프레임 생성
data = {
    "이름": ["김철수", "이영희", "박민수"],
    "나이": [25, 30, 35],
    "도시": ["서울", "부산", "대구"]
}
df = pd.DataFrame(data)
print(df)

# 데이터 필터링
young_people = df[df["나이"] < 30]
print(young_people)
```

## 5. 실습 예제

### 프로젝트 구조
```
my_project/
├── main.py
├── requirements.txt
├── utils/
│   ├── __init__.py
│   ├── file_utils.py
│   ├── math_utils.py
│   └── string_utils.py
├── data/
│   └── sample.json
└── tests/
    ├── __init__.py
    └── test_utils.py
```

### 유틸리티 모듈들
```python
# utils/file_utils.py
import json
import os
from datetime import datetime

def read_json_file(filename):
    """JSON 파일을 읽어서 딕셔너리로 반환"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {filename}")
        return None
    except json.JSONDecodeError:
        print(f"JSON 형식이 올바르지 않습니다: {filename}")
        return None

def write_json_file(data, filename):
    """딕셔너리를 JSON 파일로 저장"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"파일 저장 중 오류 발생: {e}")
        return False

def get_file_info(filename):
    """파일 정보 반환"""
    if os.path.exists(filename):
        stat = os.stat(filename)
        return {
            "filename": filename,
            "size": stat.st_size,
            "modified": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
        }
    return None

# utils/math_utils.py
import math

def calculate_circle_area(radius):
    """원의 넓이 계산"""
    return math.pi * radius ** 2

def calculate_circle_circumference(radius):
    """원의 둘레 계산"""
    return 2 * math.pi * radius

def is_prime(n):
    """소수 판별"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    """피보나치 수열의 n번째 항"""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# utils/string_utils.py
import re

def clean_text(text):
    """텍스트 정리 (공백 제거, 소문자 변환)"""
    return re.sub(r'\s+', ' ', text.strip().lower())

def extract_numbers(text):
    """텍스트에서 숫자 추출"""
    numbers = re.findall(r'\d+', text)
    return [int(num) for num in numbers]

def is_valid_email(email):
    """이메일 형식 검증"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def format_phone_number(phone):
    """전화번호 포맷팅"""
    # 숫자만 추출
    numbers = re.sub(r'\D', '', phone)
    
    if len(numbers) == 11 and numbers.startswith('010'):
        return f"{numbers[:3]}-{numbers[3:7]}-{numbers[7:]}"
    elif len(numbers) == 10:
        return f"{numbers[:3]}-{numbers[3:6]}-{numbers[6:]}"
    else:
        return phone

# utils/__init__.py
from .file_utils import read_json_file, write_json_file, get_file_info
from .math_utils import calculate_circle_area, calculate_circle_circumference, is_prime, fibonacci
from .string_utils import clean_text, extract_numbers, is_valid_email, format_phone_number

__all__ = [
    'read_json_file', 'write_json_file', 'get_file_info',
    'calculate_circle_area', 'calculate_circle_circumference', 'is_prime', 'fibonacci',
    'clean_text', 'extract_numbers', 'is_valid_email', 'format_phone_number'
]
```

### 메인 프로그램
```python
# main.py
import utils
import os

def main():
    print("=== 유틸리티 함수 테스트 ===\n")
    
    # 수학 유틸리티 테스트
    print("1. 수학 유틸리티")
    radius = 5
    print(f"반지름 {radius}인 원의 넓이: {utils.calculate_circle_area(radius):.2f}")
    print(f"반지름 {radius}인 원의 둘레: {utils.calculate_circle_circumference(radius):.2f}")
    
    # 소수 판별
    numbers = [17, 25, 29, 100]
    for num in numbers:
        print(f"{num}은(는) {'소수' if utils.is_prime(num) else '합성수'}입니다.")
    
    # 피보나치 수열
    print(f"피보나치 수열의 10번째 항: {utils.fibonacci(10)}")
    
    # 문자열 유틸리티 테스트
    print("\n2. 문자열 유틸리티")
    text = "  Hello    World  Python  Programming  "
    print(f"원본: '{text}'")
    print(f"정리 후: '{utils.clean_text(text)}'")
    
    # 숫자 추출
    text_with_numbers = "가격은 1000원이고 할인율은 15%입니다."
    numbers = utils.extract_numbers(text_with_numbers)
    print(f"추출된 숫자: {numbers}")
    
    # 이메일 검증
    emails = ["test@example.com", "invalid-email", "user@domain.co.kr"]
    for email in emails:
        print(f"{email}: {'유효한' if utils.is_valid_email(email) else '유효하지 않은'} 이메일")
    
    # 전화번호 포맷팅
    phones = ["01012345678", "02-1234-5678", "010-1234-5678"]
    for phone in phones:
        print(f"{phone} → {utils.format_phone_number(phone)}")
    
    # 파일 유틸리티 테스트
    print("\n3. 파일 유틸리티")
    
    # 샘플 데이터 생성
    sample_data = {
        "users": [
            {"name": "김철수", "age": 25, "email": "kim@example.com"},
            {"name": "이영희", "age": 30, "email": "lee@example.com"},
            {"name": "박민수", "age": 35, "email": "park@example.com"}
        ],
        "created_at": "2023-12-07T14:30:00Z"
    }
    
    # JSON 파일 저장
    filename = "data/sample.json"
    os.makedirs("data", exist_ok=True)
    
    if utils.write_json_file(sample_data, filename):
        print(f"데이터가 {filename}에 저장되었습니다.")
        
        # 파일 정보 확인
        file_info = utils.get_file_info(filename)
        if file_info:
            print(f"파일 크기: {file_info['size']} bytes")
            print(f"수정 시간: {file_info['modified']}")
        
        # JSON 파일 읽기
        loaded_data = utils.read_json_file(filename)
        if loaded_data:
            print(f"읽어온 사용자 수: {len(loaded_data['users'])}")
            for user in loaded_data['users']:
                print(f"  - {user['name']} ({user['age']}세)")

if __name__ == "__main__":
    main()
```

### requirements.txt
```txt
# 프로젝트 의존성
requests>=2.28.0
numpy>=1.21.0
pandas>=1.3.0
```

## 6. 자바/리액트 개발자를 위한 비교

### 자바와의 비교
```java
// 자바 패키지
package com.example.utils;

public class MathUtils {
    public static int add(int a, int b) {
        return a + b;
    }
}

// 사용
import com.example.utils.MathUtils;
int result = MathUtils.add(5, 3);
```

```python
# 파이썬 모듈
# utils/math_utils.py
def add(a, b):
    return a + b

# 사용
import utils.math_utils
result = utils.math_utils.add(5, 3)

# 또는
from utils.math_utils import add
result = add(5, 3)
```

### 리액트와의 비교
```javascript
// JavaScript 모듈
// utils/mathUtils.js
export const add = (a, b) => a + b;

// 사용
import { add } from './utils/mathUtils';
const result = add(5, 3);
```

```python
# 파이썬 모듈
# utils/math_utils.py
def add(a, b):
    return a + b

# 사용
from utils.math_utils import add
result = add(5, 3)
```

## 7. 모범 사례

### 1. 모듈 구조화
```python
# 좋은 예: 명확한 책임 분리
# user_management/
# ├── __init__.py
# ├── user.py          # User 클래스
# ├── auth.py          # 인증 관련
# ├── database.py      # 데이터베이스 연결
# └── validators.py    # 입력 검증

# 나쁜 예: 모든 것이 하나의 파일에
# user_management.py   # 1000줄의 코드
```

### 2. __init__.py 활용
```python
# __init__.py에서 공개 API 정의
from .user import User
from .auth import login, logout
from .validators import validate_email

__all__ = ['User', 'login', 'logout', 'validate_email']
```

### 3. 상대 임포트 vs 절대 임포트
```python
# 절대 임포트 (권장)
from my_package.utils import math_utils

# 상대 임포트 (패키지 내부에서만)
from .utils import math_utils
from ..parent_package import something
```

## 8. 다음 학습 단계

1. 예외 처리 (try-except)
2. 파일 입출력
3. 데코레이터
4. 제너레이터

---

**핵심 포인트**
- 모듈: 코드 재사용과 조직화
- 패키지: 관련 모듈들의 그룹
- 임포트: 다양한 방법으로 모듈 사용
- __init__.py: 패키지 초기화와 API 정의
- pip: 외부 패키지 관리
