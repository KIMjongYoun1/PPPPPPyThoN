"""
MyApp - 샘플 파이썬 애플리케이션

이 패키지는 파이썬 패키지 구조를 이해하기 위한 예제입니다.
"""

__version__ = "1.0.0"
__author__ = "Python Learner"

# 패키지에서 자주 사용하는 클래스들을 직접 임포트
from .models.user import User
from .models.product import Product
from .services.user_service import UserService
from .services.product_service import ProductService

# __all__ 변수로 공개할 모듈/클래스 정의
__all__ = [
    'User',
    'Product', 
    'UserService',
    'ProductService'
]
