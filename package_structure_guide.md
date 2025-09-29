# 파이썬 패키지 구조 이해 가이드

## 🎯 학습 목표

이 가이드를 통해 다음을 이해할 수 있습니다:
1. 파이썬 패키지 구조의 기본 원리
2. 자바와 파이썬의 아키텍처 차이점
3. 실제 프로젝트에서 사용하는 패키지 구조
4. 각 파일과 폴더의 역할

## 📁 현재 프로젝트 구조

```
/Users/ryankim/Python/
├── 📚 학습 자료들
│   ├── 01_python_setup.md
│   ├── 02_python_basics.md
│   ├── 03_data_structures.md
│   ├── 04_control_flow.md
│   ├── 05_object_oriented_programming.md
│   ├── 06_modules_packages.md          ← 패키지 구조 설명
│   ├── 07_practical_examples.md
│   └── 08_best_practices.md
├── 🐍 파이썬 파일들
│   ├── cursor_demo.py
│   ├── hello_world.py
│   └── package_structure_demo.py
├── 📦 예제 패키지
│   └── my_sample_app/                  ← 실제 패키지 구조 예제
└── 🔧 가상환경
    └── my_python_env/                  ← 파이썬 실행 환경
```

## 🔍 단계별 이해하기

### 1단계: 가상환경 vs 프로젝트 패키지 구분

#### 가상환경 (`my_python_env/`)
```
my_python_env/
├── bin/           # 파이썬 실행 파일들
├── lib/           # 설치된 패키지들
├── include/       # C 확장 모듈 헤더
└── pyvenv.cfg     # 가상환경 설정
```
**역할**: 파이썬 실행 환경을 격리하는 도구

#### 프로젝트 패키지 (`my_sample_app/`)
```
my_sample_app/
├── src/myapp/     # 실제 애플리케이션 코드
├── tests/         # 테스트 코드
├── requirements.txt
└── setup.py
```
**역할**: 실제 애플리케이션의 코드 구조

### 2단계: 패키지 구조 분석

#### 핵심 디렉토리별 역할

| 디렉토리 | 역할 | 자바 비교 |
|----------|------|-----------|
| `models/` | 데이터 모델 정의 | `entity/`, `model/` |
| `services/` | 비즈니스 로직 | `service/`, `business/` |
| `utils/` | 공통 유틸리티 | `util/`, `helper/` |
| `tests/` | 테스트 코드 | `test/` |

#### `__init__.py` 파일의 중요성

```python
# myapp/__init__.py
"""
패키지 초기화 파일
- 패키지를 파이썬 패키지로 인식하게 함
- 패키지의 공개 API 정의
- 패키지 메타데이터 설정
"""

# 패키지 정보
__version__ = "1.0.0"
__author__ = "Python Learner"

# 공개할 클래스들을 임포트
from .models.user import User
from .models.product import Product
from .services.user_service import UserService

# 공개 API 정의
__all__ = ['User', 'Product', 'UserService']
```

### 3단계: 계층별 코드 분석

#### Models 계층 (데이터 모델)
```python
# models/user.py
class User:
    """사용자 데이터 모델"""
    
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.created_at = datetime.now()
    
    def get_info(self):
        """사용자 정보 반환"""
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email
        }
```

**특징**:
- 데이터 구조 정의
- 비즈니스 로직 없음
- 단순한 데이터 저장소

#### Services 계층 (비즈니스 로직)
```python
# services/user_service.py
class UserService:
    """사용자 관련 비즈니스 로직"""
    
    def __init__(self):
        self.users = {}  # 메모리 저장소
    
    def create_user(self, user_id, name, email):
        """사용자 생성 로직"""
        if user_id in self.users:
            raise ValueError("이미 존재하는 사용자")
        
        user = User(user_id, name, email)
        self.users[user_id] = user
        return user
    
    def get_user(self, user_id):
        """사용자 조회 로직"""
        return self.users.get(user_id)
```

**특징**:
- 비즈니스 규칙 구현
- 데이터 검증
- 트랜잭션 관리

#### Utils 계층 (공통 기능)
```python
# utils/helpers.py
def format_currency(amount, currency="KRW"):
    """통화 포맷팅"""
    if currency == "KRW":
        return f"{amount:,.0f}원"
    return f"{amount:,.2f} {currency}"

def validate_email(email):
    """이메일 검증"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
```

**특징**:
- 재사용 가능한 함수들
- 특정 도메인에 종속되지 않음
- 순수 함수 (입력 → 출력)

### 4단계: 패키지 사용 방법

#### 임포트 방법 비교

```python
# 방법 1: __init__.py에서 정의한 클래스 직접 사용
from myapp import User, UserService

# 방법 2: 개별 모듈에서 임포트
from myapp.models.user import User
from myapp.services.user_service import UserService

# 방법 3: 패키지 단위 임포트
from myapp.models import user
from myapp.services import user_service
```

#### 실제 사용 예제

```python
# 서비스 인스턴스 생성
user_service = UserService()

# 사용자 생성
user = user_service.create_user("user001", "김철수", "kim@example.com")

# 유틸리티 함수 사용
from myapp.utils.helpers import format_currency
formatted_price = format_currency(1200000)  # "1,200,000원"
```

## 🏗️ 아키텍처 패턴 이해

### 계층형 아키텍처 (Layered Architecture)

```
┌─────────────────┐
│   main.py       │ ← 프레젠테이션 계층
├─────────────────┤
│   services/     │ ← 비즈니스 계층
├─────────────────┤
│   models/       │ ← 데이터 계층
├─────────────────┤
│   utils/        │ ← 유틸리티 계층
└─────────────────┘
```

### 의존성 방향

```
main.py → services/ → models/
    ↓         ↓
  utils/ ←────┘
```

**원칙**: 상위 계층이 하위 계층에만 의존

## 🔄 자바와의 주요 차이점

### 1. 패키지 정의
```java
// 자바: 폴더만 있으면 패키지
package com.example.myproject.service;
public class UserService { ... }
```

```python
# 파이썬: __init__.py 파일 필요
# myapp/services/__init__.py
from .user_service import UserService
```

### 2. 임포트 방식
```java
// 자바: 컴파일 타임에 결정
import com.example.myproject.service.UserService;
```

```python
# 파이썬: 런타임에 동적 임포트
from myapp.services.user_service import UserService
```

### 3. 네이밍 규칙
```java
// 자바: PascalCase
public class UserService { ... }
```

```python
# 파이썬: snake_case
class UserService:  # 클래스는 PascalCase
    def create_user(self):  # 메서드는 snake_case
        pass
```

## 📋 학습 체크리스트

### 기본 이해
- [ ] 가상환경과 프로젝트 패키지의 차이점 이해
- [ ] `__init__.py` 파일의 역할 이해
- [ ] 계층형 아키텍처의 개념 이해

### 구조 분석
- [ ] `models/` 디렉토리의 역할 이해
- [ ] `services/` 디렉토리의 역할 이해
- [ ] `utils/` 디렉토리의 역할 이해
- [ ] 각 계층 간의 의존성 관계 이해

### 실습
- [ ] 패키지에서 클래스 임포트하기
- [ ] 서비스 인스턴스 생성하고 사용하기
- [ ] 유틸리티 함수 사용하기

## 🎯 다음 단계

1. **코드 분석**: `my_sample_app/` 디렉토리의 각 파일을 열어보며 구조 이해
2. **문서 참조**: `06_modules_packages.md`에서 상세한 설명 확인
3. **실습**: 간단한 모델과 서비스 추가해보기
4. **확장**: 새로운 기능을 패키지에 추가해보기

## 💡 핵심 포인트

1. **패키지 ≠ 가상환경**: 패키지는 코드 구조, 가상환경은 실행 환경
2. **__init__.py 필수**: 파이썬에서 패키지로 인식하려면 반드시 필요
3. **계층 분리**: 각 계층은 명확한 책임을 가져야 함
4. **의존성 방향**: 상위 계층이 하위 계층에만 의존
5. **네이밍 규칙**: 파이썬은 snake_case, 자바는 camelCase

---

**이제 `my_sample_app/` 디렉토리를 열어서 실제 코드를 보며 구조를 이해해보세요!** 🐍
