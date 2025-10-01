#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
데코레이터 vs Java 어노테이션 완전 이해하기
"""

from functools import wraps
import time

# ============================================
# 예제 1: 실행 시간 측정 (Java의 @Timed와 유사)
# ============================================

def measure_time(f):
    """
    함수 실행 시간을 측정하는 데코레이터
    
    Java 비교:
    @Timed
    public void someMethod() { ... }
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f"⏱️  {f.__name__} 실행 시간: {end - start:.4f}초")
        return result
    return wrapper


# ============================================
# 예제 2: 권한 검증 (Java의 @PreAuthorize와 유사)
# ============================================

def require_auth(f):
    """
    인증 필요 데코레이터
    
    Java 비교:
    @PreAuthorize("hasRole('USER')")
    public void securedMethod() { ... }
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        # 실제로는 토큰 검증 등을 수행
        user = kwargs.get('user')
        if user != 'admin':
            print("❌ 권한이 없습니다!")
            return None
        print("✅ 권한 검증 통과")
        return f(*args, **kwargs)
    return wrapper


# ============================================
# 예제 3: 로깅 (Java의 @Loggable와 유사)
# ============================================

def log_call(f):
    """
    함수 호출을 로깅하는 데코레이터
    
    Java 비교:
    @Loggable
    public void businessMethod() { ... }
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(f"📝 [{f.__name__}] 호출됨 - args: {args}, kwargs: {kwargs}")
        result = f(*args, **kwargs)
        print(f"📝 [{f.__name__}] 완료 - 결과: {result}")
        return result
    return wrapper


# ============================================
# 예제 4: 재시도 로직 (Java의 @Retryable과 유사)
# ============================================

def retry(max_attempts=3):
    """
    실패 시 재시도하는 데코레이터 (파라미터 있음!)
    
    Java 비교:
    @Retryable(maxAttempts = 3)
    public void unreliableMethod() { ... }
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return f(*args, **kwargs)
                except Exception as e:
                    print(f"🔄 시도 {attempt + 1}/{max_attempts} 실패: {e}")
                    if attempt == max_attempts - 1:
                        raise
        return wrapper
    return decorator


# ============================================
# 실제 사용 예시
# ============================================

@measure_time
def slow_function():
    """실행 시간 측정 예시"""
    print("⏳ 무거운 작업 수행 중...")
    time.sleep(1)
    return "완료!"


@log_call
@measure_time
def calculate(x, y):
    """여러 데코레이터를 동시에 사용 (순서 중요!)"""
    result = x + y
    return result


@require_auth
def delete_user(user_id, user=None):
    """권한 검증이 필요한 함수"""
    print(f"🗑️  사용자 {user_id} 삭제됨")
    return True


@retry(max_attempts=3)
def unreliable_api_call():
    """실패할 수 있는 API 호출"""
    import random
    if random.random() < 0.7:  # 70% 확률로 실패
        raise Exception("API 호출 실패")
    return "API 성공!"


# ============================================
# Flask 스타일 데코레이터
# ============================================

class RequestValidator:
    """
    클래스 기반 데코레이터
    
    Java 비교:
    @Validated
    @RequestMapping("/api/users")
    """
    
    def __init__(self, required_fields):
        self.required_fields = required_fields
    
    def __call__(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            data = kwargs.get('data', {})
            
            # 필수 필드 검증
            missing = [field for field in self.required_fields if field not in data]
            if missing:
                print(f"❌ 필수 필드 누락: {missing}")
                return None
            
            print("✅ 필드 검증 통과")
            return f(*args, **kwargs)
        return wrapper


@RequestValidator(required_fields=['name', 'email'])
def create_user(data):
    """필수 필드 검증을 거치는 함수"""
    print(f"👤 사용자 생성: {data}")
    return True


# ============================================
# 메인 실행
# ============================================

if __name__ == "__main__":
    print("=" * 70)
    print("🎯 Python 데코레이터 = Java 어노테이션")
    print("=" * 70)
    
    print("\n1️⃣ 실행 시간 측정 (@Timed)")
    print("-" * 70)
    result = slow_function()
    print(f"결과: {result}")
    
    print("\n2️⃣ 여러 데코레이터 조합")
    print("-" * 70)
    result = calculate(10, 20)
    
    print("\n3️⃣ 권한 검증 (@PreAuthorize)")
    print("-" * 70)
    print("▶ 관리자로 실행:")
    delete_user("user123", user="admin")
    print("\n▶ 일반 사용자로 실행:")
    delete_user("user123", user="guest")
    
    print("\n4️⃣ 재시도 로직 (@Retryable)")
    print("-" * 70)
    try:
        result = unreliable_api_call()
        print(f"✅ {result}")
    except Exception as e:
        print(f"❌ 최종 실패: {e}")
    
    print("\n5️⃣ 필드 검증 (@Validated)")
    print("-" * 70)
    print("▶ 유효한 데이터:")
    create_user(data={'name': '김철수', 'email': 'kim@example.com'})
    print("\n▶ 누락된 데이터:")
    create_user(data={'name': '이영희'})  # email 누락
    
    print("\n" + "=" * 70)
    print("🎓 정리:")
    print("  • 데코레이터 = 함수를 감싸서 기능 추가")
    print("  • @ 기호 사용 (Java 어노테이션과 동일)")
    print("  • 여러 개 중첩 가능 (위에서 아래로 실행)")
    print("  • 타입이 아니라 '기능 추가 도구'입니다!")
    print("=" * 70)


# ============================================
# Java vs Python 매핑
# ============================================

"""
Java 어노테이션          →  Python 데코레이터

@Timed                  →  @measure_time
@PreAuthorize           →  @require_auth
@Loggable               →  @log_call
@Retryable(max=3)       →  @retry(max_attempts=3)
@Validated              →  @RequestValidator(...)
@Transactional          →  @transactional
@Cacheable              →  @cache
@Async                  →  @async_task

Flask 전용:
@RequestMapping         →  @app.route('/path')
@GetMapping             →  @app.route('/path', methods=['GET'])
@PostMapping            →  @app.route('/path', methods=['POST'])
"""

