#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MyApp 메인 실행 파일
"""

from .services.user_service import UserService
from .services.product_service import ProductService
from .utils.helpers import format_currency, validate_email, generate_id

def main():
    """메인 함수"""
    print("🎉 MyApp - 파이썬 패키지 구조 예제")
    print("=" * 50)
    
    # 서비스 인스턴스 생성
    user_service = UserService()
    product_service = ProductService()
    
    # 사용자 생성 및 관리
    print("\n👤 사용자 관리")
    print("-" * 30)
    
    try:
        # 사용자 생성
        user1 = user_service.create_user("user001", "김철수", "kim@example.com", 25)
        user2 = user_service.create_user("user002", "이영희", "lee@example.com", 30)
        
        print(f"사용자 생성 완료: {user1.name}, {user2.name}")
        
        # 사용자 조회
        all_users = user_service.get_all_users()
        print(f"전체 사용자 수: {user_service.get_user_count()}")
        
        for user in all_users:
            print(f"  - {user}")
        
    except ValueError as e:
        print(f"사용자 생성 오류: {e}")
    
    # 상품 생성 및 관리
    print("\n🛍️ 상품 관리")
    print("-" * 30)
    
    try:
        # 상품 생성
        product1 = product_service.create_product(
            "prod001", "노트북", 1200000, "전자제품", 10
        )
        product2 = product_service.create_product(
            "prod002", "마우스", 25000, "전자제품", 50
        )
        product3 = product_service.create_product(
            "prod003", "책상", 150000, "가구", 5
        )
        
        print(f"상품 생성 완료: {product1.name}, {product2.name}, {product3.name}")
        
        # 상품 조회
        all_products = product_service.get_all_products()
        print(f"전체 상품 수: {product_service.get_product_count()}")
        
        for product in all_products:
            print(f"  - {product}")
        
        # 카테고리별 상품 조회
        electronics = product_service.get_products_by_category("전자제품")
        print(f"\n전자제품 카테고리 상품 수: {len(electronics)}")
        
        # 전체 상품 가치 계산
        total_value = product_service.get_total_value()
        print(f"전체 상품 가치: {format_currency(total_value)}")
        
    except ValueError as e:
        print(f"상품 생성 오류: {e}")
    
    # 유틸리티 함수 테스트
    print("\n🔧 유틸리티 함수 테스트")
    print("-" * 30)
    
    # 이메일 검증
    emails = ["test@example.com", "invalid-email", "user@domain.co.kr"]
    for email in emails:
        is_valid = validate_email(email)
        print(f"이메일 '{email}': {'유효' if is_valid else '무효'}")
    
    # ID 생성
    user_id = generate_id("USER_")
    product_id = generate_id("PROD_")
    print(f"생성된 사용자 ID: {user_id}")
    print(f"생성된 상품 ID: {product_id}")
    
    print("\n" + "=" * 50)
    print("🎊 MyApp 데모가 완료되었습니다!")
    print("이제 패키지 구조를 이해하셨나요? 🐍")

if __name__ == "__main__":
    main()
