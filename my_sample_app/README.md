# MyApp - 파이썬 패키지 구조 예제

파이썬 패키지 구조를 이해하기 위한 샘플 애플리케이션입니다.

## 📁 프로젝트 구조

```
my_sample_app/
├── src/
│   └── myapp/
│       ├── __init__.py
│       ├── main.py
│       ├── models/
│       │   ├── __init__.py
│       │   ├── user.py
│       │   └── product.py
│       ├── services/
│       │   ├── __init__.py
│       │   ├── user_service.py
│       │   └── product_service.py
│       └── utils/
│           ├── __init__.py
│           └── helpers.py
├── tests/
│   ├── __init__.py
│   └── test_models.py
├── requirements.txt
├── setup.py
└── README.md
```

## 🚀 실행 방법

### 1. 메인 애플리케이션 실행
```bash
cd my_sample_app
python3 -m src.myapp.main
```

### 2. 테스트 실행
```bash
cd my_sample_app
python3 tests/test_models.py
```

### 3. 패키지 설치 (개발 모드)
```bash
cd my_sample_app
pip install -e .
```

## 📦 패키지 사용 예제

```python
# 패키지에서 클래스 임포트
from myapp import User, Product, UserService, ProductService

# 서비스 인스턴스 생성
user_service = UserService()
product_service = ProductService()

# 사용자 생성
user = user_service.create_user("user001", "김철수", "kim@example.com", 25)

# 상품 생성
product = product_service.create_product("prod001", "노트북", 1200000, "전자제품", 10)
```

## 🧪 테스트

```bash
# 모든 테스트 실행
python3 tests/test_models.py

# pytest 사용 (설치된 경우)
pytest tests/
```

## 📚 학습 포인트

1. **패키지 구조**: `__init__.py` 파일의 역할
2. **모듈 임포트**: 상대 임포트와 절대 임포트
3. **서비스 패턴**: 비즈니스 로직 분리
4. **모델 클래스**: 데이터 모델 정의
5. **유틸리티 함수**: 공통 기능 모듈화

## 🔧 개발 환경 설정

```bash
# 가상환경 생성
python3 -m venv venv

# 가상환경 활성화
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# 의존성 설치
pip install -r requirements.txt
```
