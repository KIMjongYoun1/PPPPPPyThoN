"""
모델 테스트
"""

import sys
import os

# 상위 디렉토리의 src를 Python 경로에 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from myapp.models.user import User
from myapp.models.product import Product

def test_user_creation():
    """사용자 생성 테스트"""
    user = User("user001", "김철수", "kim@example.com", 25)
    
    assert user.user_id == "user001"
    assert user.name == "김철수"
    assert user.email == "kim@example.com"
    assert user.age == 25
    assert user.is_active == True
    
    print("✅ 사용자 생성 테스트 통과")

def test_user_activation():
    """사용자 활성화/비활성화 테스트"""
    user = User("user002", "이영희", "lee@example.com")
    
    # 비활성화
    user.deactivate()
    assert user.is_active == False
    
    # 활성화
    user.activate()
    assert user.is_active == True
    
    print("✅ 사용자 활성화 테스트 통과")

def test_product_creation():
    """상품 생성 테스트"""
    product = Product("prod001", "노트북", 1200000, "전자제품", 10)
    
    assert product.product_id == "prod001"
    assert product.name == "노트북"
    assert product.price == 1200000
    assert product.category == "전자제품"
    assert product.stock == 10
    
    print("✅ 상품 생성 테스트 통과")

def test_product_stock():
    """상품 재고 관리 테스트"""
    product = Product("prod002", "마우스", 25000, "전자제품", 50)
    
    # 재고 추가
    product.update_stock(10)
    assert product.stock == 60
    
    # 재고 감소
    product.update_stock(-5)
    assert product.stock == 55
    
    # 구매 가능 여부 확인
    assert product.is_available() == True
    
    # 재고 부족 테스트
    try:
        product.update_stock(-100)
        assert False, "재고 부족 예외가 발생해야 함"
    except ValueError:
        print("✅ 재고 부족 예외 처리 테스트 통과")

def run_tests():
    """모든 테스트 실행"""
    print("🧪 모델 테스트 시작")
    print("=" * 30)
    
    test_user_creation()
    test_user_activation()
    test_product_creation()
    test_product_stock()
    
    print("\n🎉 모든 모델 테스트 통과!")

if __name__ == "__main__":
    run_tests()
