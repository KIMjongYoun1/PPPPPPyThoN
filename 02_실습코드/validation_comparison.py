#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Java Bean Validation vs Python 검증 방식 비교
"""

# ============================================
# 방법 1: 수동 검증 (Flask 기본)
# ============================================

def validate_user_manual(data):
    """
    수동 검증 - 매우 번거로움!
    Java와 비교하면 원시적인 방법
    """
    errors = []
    
    # 필수 필드 검증
    if 'user_id' not in data:
        errors.append("user_id는 필수입니다")
    
    if 'name' not in data:
        errors.append("name은 필수입니다")
    elif len(data['name']) < 2 or len(data['name']) > 50:
        errors.append("name은 2-50자 사이여야 합니다")
    
    if 'email' not in data:
        errors.append("email은 필수입니다")
    elif '@' not in data['email']:
        errors.append("유효한 이메일 형식이 아닙니다")
    
    if 'age' in data:
        if not isinstance(data['age'], int):
            errors.append("age는 숫자여야 합니다")
        elif data['age'] < 0 or data['age'] > 120:
            errors.append("age는 0-120 사이여야 합니다")
    
    return errors


# ============================================
# 방법 2: Pydantic 사용 (Java Bean Validation과 동일!)
# ============================================

"""
먼저 설치 필요: pip install pydantic

from pydantic import BaseModel, EmailStr, Field, validator

class UserDto(BaseModel):
    '''
    Java 비교:
    
    public class UserDto {
        @NotNull
        @Size(min=3, max=50)
        private String userId;
        
        @NotBlank
        private String name;
        
        @Email
        private String email;
        
        @Min(0) @Max(120)
        private Integer age;
    }
    '''
    user_id: str = Field(..., min_length=3, max_length=50, description="사용자 ID")
    name: str = Field(..., min_length=2, max_length=100, description="이름")
    email: EmailStr  # 자동으로 이메일 형식 검증!
    age: int = Field(None, ge=0, le=120, description="나이")
    
    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('이름은 공백일 수 없습니다')
        return v.strip()
    
    @validator('user_id')
    def user_id_alphanumeric(cls, v):
        if not v.isalnum():
            raise ValueError('user_id는 영문자와 숫자만 가능합니다')
        return v


# Flask에서 사용:
@app.route('/api/v1/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    try:
        # 자동 검증! (Java의 @Valid처럼)
        user_dto = UserDto(**data)
        
        # 여기 도달했다면 검증 통과!
        user = user_service.create_user(
            user_id=user_dto.user_id,
            name=user_dto.name,
            email=user_dto.email,
            age=user_dto.age
        )
        return jsonify(user_dto.dict()), 201
        
    except ValidationError as e:
        # 검증 실패 시 자동으로 에러 반환 (Java처럼!)
        return jsonify({'errors': e.errors()}), 400
"""


# ============================================
# 방법 3: dataclasses + 커스텀 검증
# ============================================

from dataclasses import dataclass
from typing import Optional
import re

@dataclass
class UserDtoDataclass:
    """
    Python 표준 라이브러리 사용 (외부 패키지 불필요)
    하지만 검증은 직접 구현해야 함
    """
    user_id: str
    name: str
    email: str
    age: Optional[int] = None
    
    def __post_init__(self):
        """객체 생성 후 자동으로 검증"""
        errors = []
        
        # user_id 검증
        if not self.user_id or len(self.user_id) < 3:
            errors.append("user_id는 최소 3자 이상이어야 합니다")
        
        # name 검증
        if not self.name or len(self.name) < 2:
            errors.append("name은 최소 2자 이상이어야 합니다")
        
        # email 검증
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, self.email):
            errors.append("유효한 이메일 형식이 아닙니다")
        
        # age 검증
        if self.age is not None and (self.age < 0 or self.age > 120):
            errors.append("age는 0-120 사이여야 합니다")
        
        if errors:
            raise ValueError(f"검증 실패: {', '.join(errors)}")


# ============================================
# 방법 4: 검증 데코레이터 (커스텀)
# ============================================

from functools import wraps

def validate_request(schema):
    """
    검증 스키마를 받아서 자동으로 검증하는 데코레이터
    
    Java 비교:
    @Valid @RequestBody UserDto userDto
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            # request에서 데이터 가져오기
            from flask import request, jsonify
            data = request.get_json()
            
            # 스키마로 검증
            errors = []
            for field, rules in schema.items():
                value = data.get(field)
                
                # required 체크
                if rules.get('required') and not value:
                    errors.append(f"{field}는 필수입니다")
                    continue
                
                if value is not None:
                    # type 체크
                    expected_type = rules.get('type')
                    if expected_type and not isinstance(value, expected_type):
                        errors.append(f"{field}는 {expected_type.__name__} 타입이어야 합니다")
                    
                    # min_length 체크
                    if 'min_length' in rules and len(str(value)) < rules['min_length']:
                        errors.append(f"{field}는 최소 {rules['min_length']}자 이상이어야 합니다")
                    
                    # max_length 체크
                    if 'max_length' in rules and len(str(value)) > rules['max_length']:
                        errors.append(f"{field}는 최대 {rules['max_length']}자 이하여야 합니다")
                    
                    # 커스텀 validator
                    if 'validator' in rules:
                        is_valid, error_msg = rules['validator'](value)
                        if not is_valid:
                            errors.append(error_msg)
            
            if errors:
                return jsonify({'errors': errors}), 400
            
            # 검증 통과 시 원래 함수 실행
            return f(*args, **kwargs)
        
        return wrapper
    return decorator


# 사용 예시:
def is_valid_email(email):
    """이메일 검증 함수"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True, None
    return False, "유효한 이메일 형식이 아닙니다"


# 검증 스키마 정의 (Java의 Bean Validation 어노테이션처럼)
user_schema = {
    'user_id': {
        'required': True,
        'type': str,
        'min_length': 3,
        'max_length': 50
    },
    'name': {
        'required': True,
        'type': str,
        'min_length': 2,
        'max_length': 100
    },
    'email': {
        'required': True,
        'type': str,
        'validator': is_valid_email
    },
    'age': {
        'required': False,
        'type': int
    }
}

"""
# Flask에서 사용:
@app.route('/api/v1/users', methods=['POST'])
@validate_request(user_schema)  # ← Java의 @Valid처럼!
def create_user():
    # 여기 도달했다면 이미 검증 통과!
    data = request.get_json()
    user = user_service.create_user(**data)
    return jsonify({...}), 201
"""


# ============================================
# 실제 테스트
# ============================================

if __name__ == "__main__":
    print("=" * 80)
    print("🎯 Java Bean Validation vs Python 검증 방식")
    print("=" * 80)
    
    # 테스트 데이터
    valid_data = {
        'user_id': 'user123',
        'name': '김철수',
        'email': 'kim@example.com',
        'age': 25
    }
    
    invalid_data = {
        'user_id': 'u1',  # 너무 짧음
        'name': '',       # 빈 값
        'email': 'invalid-email',  # 형식 오류
        'age': 150        # 범위 초과
    }
    
    print("\n1️⃣ 수동 검증 방식")
    print("-" * 80)
    print("✅ 유효한 데이터:")
    errors = validate_user_manual(valid_data)
    print(f"  검증 결과: {'통과' if not errors else errors}")
    
    print("\n❌ 유효하지 않은 데이터:")
    errors = validate_user_manual(invalid_data)
    print(f"  검증 결과:")
    for error in errors:
        print(f"    - {error}")
    
    print("\n2️⃣ dataclasses 방식")
    print("-" * 80)
    print("✅ 유효한 데이터:")
    try:
        user = UserDtoDataclass(**valid_data)
        print(f"  객체 생성 성공: {user}")
    except ValueError as e:
        print(f"  검증 실패: {e}")
    
    print("\n❌ 유효하지 않은 데이터:")
    try:
        user = UserDtoDataclass(**invalid_data)
        print(f"  객체 생성 성공: {user}")
    except ValueError as e:
        print(f"  검증 실패: {e}")
    
    print("\n" + "=" * 80)
    print("📊 방식 비교 요약")
    print("=" * 80)
    print("""
    Java Bean Validation          Python 방식
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    @NotNull                      required=True (Pydantic)
    @Size(min=3, max=50)          Field(min_length=3, max_length=50)
    @Email                        EmailStr
    @Min(0) @Max(120)             Field(ge=0, le=120)
    @Pattern(regexp="...")        @validator 사용
    @Valid @RequestBody           Pydantic Model 사용
    
    자동 검증                      Pydantic 사용 시 자동
    BindingResult                 ValidationError 예외
    """)
    
    print("\n💡 결론:")
    print("  • Java: @Valid로 자동 검증 (편리함)")
    print("  • Python 기본: 수동 검증 (번거로움)")
    print("  • Python + Pydantic: Java와 거의 동일한 경험!")
    print("  • 선택: 간단한 API → 수동, 복잡한 API → Pydantic")
    print("=" * 80)

