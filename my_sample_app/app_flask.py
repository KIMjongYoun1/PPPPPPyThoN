#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Flask 웹 애플리케이션 - Spring Boot 스타일
"""

from flask import Flask, request, jsonify
from functools import wraps

# 현재 패키지에서 import
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from myapp.services.user_service import UserService
from myapp.services.product_service import ProductService
from myapp.utils.helpers import validate_email

# Flask 앱 생성 (Spring Boot의 @SpringBootApplication)
app = Flask(__name__)

# 서비스 인스턴스 (Spring의 @Autowired 역할)
user_service = UserService()
product_service = ProductService()


# ============================================
# 데코레이터 (어노테이션과 유사한 역할)
# ============================================

def validate_json(f):
    """JSON 검증 데코레이터 (Java의 @Valid와 유사)"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        return f(*args, **kwargs)
    return decorated_function


# ============================================
# User API - @RestController + @RequestMapping
# ============================================

@app.route('/api/v1/users', methods=['GET'])
def get_all_users():
    """
    모든 사용자 조회
    
    Java 비교:
    @GetMapping("/api/v1/users")
    public List<User> getAllUsers()
    """
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


@app.route('/api/v1/users', methods=['POST'])
@validate_json
def create_user():
    """
    사용자 생성
    
    Java 비교:
    @PostMapping("/api/v1/users")
    public User createUser(@RequestBody UserDto userDto)
    """
    data = request.get_json()
    
    # 필수 필드 검증
    required_fields = ['user_id', 'name', 'email']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'{field} is required'}), 400
    
    # 이메일 검증
    if not validate_email(data['email']):
        return jsonify({'error': 'Invalid email format'}), 400
    
    try:
        user = user_service.create_user(
            user_id=data['user_id'],
            name=data['name'],
            email=data['email'],
            age=data.get('age')
        )
        
        return jsonify({
            'user_id': user.user_id,
            'name': user.name,
            'email': user.email,
            'age': user.age,
            'is_active': user.is_active
        }), 201
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/v1/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    특정 사용자 조회
    
    Java 비교:
    @GetMapping("/api/v1/users/{id}")
    public User getUser(@PathVariable String id)
    """
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
@validate_json
def update_user(user_id):
    """
    사용자 정보 업데이트
    
    Java 비교:
    @PutMapping("/api/v1/users/{id}")
    public User updateUser(@PathVariable String id, @RequestBody UserDto userDto)
    """
    data = request.get_json()
    
    try:
        user = user_service.update_user(user_id, **data)
        return jsonify({
            'user_id': user.user_id,
            'name': user.name,
            'email': user.email,
            'age': user.age,
            'is_active': user.is_active
        }), 200
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 404


@app.route('/api/v1/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    사용자 삭제
    
    Java 비교:
    @DeleteMapping("/api/v1/users/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable String id)
    """
    success = user_service.delete_user(user_id)
    
    if success:
        return '', 204
    else:
        return jsonify({'error': 'User not found'}), 404


# ============================================
# Product API
# ============================================

@app.route('/api/v1/products', methods=['GET'])
def get_all_products():
    """모든 상품 조회"""
    # 쿼리 파라미터 처리 (@RequestParam)
    category = request.args.get('category')  # ?category=전자제품
    
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


@app.route('/api/v1/products', methods=['POST'])
@validate_json
def create_product():
    """상품 생성"""
    data = request.get_json()
    
    required_fields = ['product_id', 'name', 'price', 'category', 'stock']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'{field} is required'}), 400
    
    try:
        product = product_service.create_product(
            product_id=data['product_id'],
            name=data['name'],
            price=data['price'],
            category=data['category'],
            stock=data['stock']
        )
        
        return jsonify({
            'product_id': product.product_id,
            'name': product.name,
            'price': product.price,
            'category': product.category,
            'stock': product.stock
        }), 201
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


# ============================================
# 예외 처리 (Global Exception Handler)
# Java의 @ControllerAdvice와 유사
# ============================================

@app.errorhandler(404)
def not_found(error):
    """404 에러 핸들러"""
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """500 에러 핸들러"""
    return jsonify({'error': 'Internal server error'}), 500


# ============================================
# Health Check (Actuator와 유사)
# ============================================

@app.route('/health', methods=['GET'])
def health_check():
    """헬스 체크 엔드포인트"""
    return jsonify({
        'status': 'UP',
        'users_count': user_service.get_user_count(),
        'products_count': product_service.get_product_count()
    }), 200


# ============================================
# 메인 실행 (Spring Boot의 main 메서드)
# ============================================

if __name__ == '__main__':
    """
    Java 비교:
    
    @SpringBootApplication
    public class Application {
        public static void main(String[] args) {
            SpringApplication.run(Application.class, args);
        }
    }
    """
    # 개발 모드로 실행
    app.run(
        host='0.0.0.0',  # 모든 IP에서 접근 가능
        port=5000,       # 포트 번호
        debug=True       # 디버그 모드 (자동 재시작)
    )

