#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Flask + Pydantic = Java Spring Boot Bean Validation 스타일!

설치 필요: pip install pydantic
"""

from flask import Flask, request, jsonify
from pydantic import BaseModel, EmailStr, Field, validator, ValidationError
from typing import Optional
import sys
from pathlib import Path

# 경로 설정
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from myapp.services.user_service import UserService
from myapp.services.product_service import ProductService

app = Flask(__name__)

# 서비스 인스턴스
user_service = UserService()
product_service = ProductService()


# ============================================
# DTO 정의 (Java Bean Validation 스타일)
# ============================================

class UserCreateDto(BaseModel):
    """
    사용자 생성 DTO
    
    Java 비교:
    
    public class UserCreateDto {
        @NotNull(message = "사용자 ID는 필수입니다")
        @Size(min = 3, max = 50)
        @Pattern(regexp = "^[a-zA-Z0-9]+$")
        private String userId;
        
        @NotBlank
        @Size(min = 2, max = 100)
        private String name;
        
        @Email(message = "유효한 이메일 형식이 아닙니다")
        @NotNull
        private String email;
        
        @Min(0)
        @Max(120)
        private Integer age;
    }
    """
    user_id: str = Field(
        ...,  # ... = required (필수)
        min_length=3,
        max_length=50,
        description="사용자 ID"
    )
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="이름"
    )
    email: EmailStr = Field(
        ...,
        description="이메일 주소"
    )
    age: Optional[int] = Field(
        None,
        ge=0,  # greater or equal (>= 0)
        le=120,  # less or equal (<= 120)
        description="나이"
    )
    
    # 커스텀 검증 (Java의 커스텀 validator와 동일)
    @validator('user_id')
    def user_id_alphanumeric(cls, v):
        """user_id는 영문자와 숫자만 가능"""
        if not v.isalnum():
            raise ValueError('user_id는 영문자와 숫자만 가능합니다')
        return v
    
    @validator('name')
    def name_not_empty(cls, v):
        """이름은 공백일 수 없음"""
        if not v.strip():
            raise ValueError('이름은 공백일 수 없습니다')
        return v.strip()
    
    class Config:
        # JSON 스키마 예시 생성
        schema_extra = {
            "example": {
                "user_id": "user123",
                "name": "김철수",
                "email": "kim@example.com",
                "age": 25
            }
        }


class UserUpdateDto(BaseModel):
    """
    사용자 업데이트 DTO (모든 필드 선택적)
    
    Java 비교:
    public class UserUpdateDto {
        @Size(min = 2, max = 100)
        private String name;
        
        @Email
        private String email;
        
        @Min(0) @Max(120)
        private Integer age;
    }
    """
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(None, ge=0, le=120)


class ProductCreateDto(BaseModel):
    """상품 생성 DTO"""
    product_id: str = Field(..., min_length=3, max_length=50)
    name: str = Field(..., min_length=2, max_length=200)
    price: float = Field(..., gt=0, description="가격 (0보다 커야 함)")
    category: str = Field(..., min_length=2, max_length=100)
    stock: int = Field(..., ge=0, description="재고 수량")
    
    @validator('price')
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('가격은 0보다 커야 합니다')
        return round(v, 2)  # 소수점 2자리로 반올림


# ============================================
# User API (자동 검증!)
# ============================================

@app.route('/api/v1/users', methods=['POST'])
def create_user():
    """
    사용자 생성 - 자동 검증!
    
    Java 비교:
    @PostMapping("/api/v1/users")
    public User createUser(@Valid @RequestBody UserCreateDto dto) {
        return userService.createUser(dto);
    }
    """
    try:
        # Pydantic으로 자동 검증! (Java의 @Valid처럼)
        dto = UserCreateDto(**request.get_json())
        
        # 여기 도달했다면 이미 모든 검증 통과!
        user = user_service.create_user(
            user_id=dto.user_id,
            name=dto.name,
            email=dto.email,
            age=dto.age
        )
        
        return jsonify({
            'user_id': user.user_id,
            'name': user.name,
            'email': user.email,
            'age': user.age,
            'is_active': user.is_active
        }), 201
        
    except ValidationError as e:
        # 검증 실패 시 (Java의 BindingResult처럼)
        return jsonify({
            'message': '입력 데이터 검증 실패',
            'errors': e.errors()
        }), 400
    
    except ValueError as e:
        # 비즈니스 로직 오류
        return jsonify({'error': str(e)}), 400


@app.route('/api/v1/users', methods=['GET'])
def get_all_users():
    """모든 사용자 조회"""
    users = user_service.get_all_users()
    return jsonify([
        {
            'user_id': user.user_id,
            'name': user.name,
            'email': user.email,
            'age': user.age,
            'is_active': user.is_active
        }
        for user in users
    ]), 200


@app.route('/api/v1/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """특정 사용자 조회"""
    user = user_service.get_user(user_id)
    
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify({
        'user_id': user.user_id,
        'name': user.name,
        'email': user.email,
        'age': user.age,
        'is_active': user.is_active
    }), 200


@app.route('/api/v1/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """
    사용자 업데이트 - 자동 검증!
    
    Java 비교:
    @PutMapping("/api/v1/users/{id}")
    public User updateUser(@PathVariable String id, 
                          @Valid @RequestBody UserUpdateDto dto)
    """
    try:
        # 자동 검증
        dto = UserUpdateDto(**request.get_json())
        
        # 업데이트할 데이터만 추출 (None이 아닌 값만)
        update_data = {
            k: v for k, v in dto.dict().items() 
            if v is not None
        }
        
        user = user_service.update_user(user_id, **update_data)
        
        return jsonify({
            'user_id': user.user_id,
            'name': user.name,
            'email': user.email,
            'age': user.age,
            'is_active': user.is_active
        }), 200
        
    except ValidationError as e:
        return jsonify({
            'message': '입력 데이터 검증 실패',
            'errors': e.errors()
        }), 400
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 404


@app.route('/api/v1/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """사용자 삭제"""
    success = user_service.delete_user(user_id)
    
    if success:
        return '', 204
    else:
        return jsonify({'error': 'User not found'}), 404


# ============================================
# Product API
# ============================================

@app.route('/api/v1/products', methods=['POST'])
def create_product():
    """
    상품 생성 - 자동 검증!
    """
    try:
        dto = ProductCreateDto(**request.get_json())
        
        product = product_service.create_product(
            product_id=dto.product_id,
            name=dto.name,
            price=dto.price,
            category=dto.category,
            stock=dto.stock
        )
        
        return jsonify({
            'product_id': product.product_id,
            'name': product.name,
            'price': product.price,
            'category': product.category,
            'stock': product.stock
        }), 201
        
    except ValidationError as e:
        return jsonify({
            'message': '입력 데이터 검증 실패',
            'errors': e.errors()
        }), 400
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/v1/products', methods=['GET'])
def get_all_products():
    """모든 상품 조회"""
    category = request.args.get('category')
    
    if category:
        products = product_service.get_products_by_category(category)
    else:
        products = product_service.get_all_products()
    
    return jsonify([
        {
            'product_id': p.product_id,
            'name': p.name,
            'price': p.price,
            'category': p.category,
            'stock': p.stock
        }
        for p in products
    ]), 200


# ============================================
# 예외 처리
# ============================================

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500


# ============================================
# Health Check
# ============================================

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'UP',
        'users_count': user_service.get_user_count(),
        'products_count': product_service.get_product_count()
    }), 200


# ============================================
# API 문서 (Swagger 대신 간단한 정보)
# ============================================

@app.route('/', methods=['GET'])
def api_info():
    """API 정보"""
    return jsonify({
        'name': 'MyApp API with Pydantic Validation',
        'version': '1.0.0',
        'description': 'Java Bean Validation 스타일의 Python Flask API',
        'endpoints': {
            'users': {
                'POST /api/v1/users': 'Create user (auto-validated)',
                'GET /api/v1/users': 'Get all users',
                'GET /api/v1/users/{id}': 'Get user by id',
                'PUT /api/v1/users/{id}': 'Update user (auto-validated)',
                'DELETE /api/v1/users/{id}': 'Delete user'
            },
            'products': {
                'POST /api/v1/products': 'Create product (auto-validated)',
                'GET /api/v1/products': 'Get all products'
            },
            'health': 'GET /health'
        },
        'validation': 'Powered by Pydantic (like Java Bean Validation)'
    }), 200


if __name__ == '__main__':
    print("=" * 70)
    print("🚀 Flask + Pydantic 서버 시작")
    print("=" * 70)
    print("\n✨ Java Bean Validation 스타일의 자동 검증이 적용되었습니다!")
    print("\n📋 테스트 예시:")
    print("\n# 1. 유효한 데이터로 사용자 생성")
    print('curl -X POST http://localhost:5000/api/v1/users \\')
    print('  -H "Content-Type: application/json" \\')
    print('  -d \'{"user_id":"user123","name":"김철수","email":"kim@example.com","age":25}\'')
    print("\n# 2. 유효하지 않은 데이터 (검증 실패 확인)")
    print('curl -X POST http://localhost:5000/api/v1/users \\')
    print('  -H "Content-Type: application/json" \\')
    print('  -d \'{"user_id":"u1","name":"","email":"invalid","age":999}\'')
    print("\n" + "=" * 70 + "\n")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )

