#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Bean Validation 개념 이해를 위한 시연

Java의 Bean Validation과 Python의 Pydantic을 비교합니다.
"""

from dataclasses import dataclass
from typing import Optional
import re

print("=" * 80)
print("🎯 Bean Validation 개념 이해하기")
print("=" * 80)

# ============================================
# 시나리오: 사용자 등록 API
# ============================================

print("\n📋 시나리오: 사용자 등록 API를 만든다고 가정")
print("-" * 80)

# ============================================
# 방법 1: 전통적인 방식 (서비스에서 검증)
# ============================================

print("\n" + "="*80)
print("방법 1️⃣: 전통적인 방식 - 서비스 로직에서 직접 검증")
print("="*80)

# DTO - 검증 규칙 없음! 그냥 데이터만 담음
class UserDtoTraditional:
    """검증 규칙이 없는 DTO (그냥 데이터 컨테이너)"""
    def __init__(self, user_id, name, email, age=None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.age = age


# Service - 여기서 모든 검증을 수동으로!
class UserServiceTraditional:
    """전통적인 서비스: 검증 로직이 서비스 안에 있음"""
    
    def create_user(self, dto: UserDtoTraditional):
        """사용자 생성 - 검증 로직 포함"""
        
        print("\n  🔍 검증 시작 (수동으로 하나씩 체크)...")
        
        # userId 검증
        if not dto.user_id:
            return "❌ 오류: userId는 필수입니다"
        if len(dto.user_id) < 3 or len(dto.user_id) > 50:
            return "❌ 오류: userId는 3-50자여야 합니다"
        if not dto.user_id.isalnum():
            return "❌ 오류: userId는 영문자와 숫자만 가능합니다"
        print(f"  ✓ userId 검증 통과: {dto.user_id}")
        
        # name 검증
        if not dto.name or not dto.name.strip():
            return "❌ 오류: name은 필수입니다"
        if len(dto.name) < 2 or len(dto.name) > 100:
            return "❌ 오류: name은 2-100자여야 합니다"
        print(f"  ✓ name 검증 통과: {dto.name}")
        
        # email 검증
        if not dto.email:
            return "❌ 오류: email은 필수입니다"
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, dto.email):
            return "❌ 오류: 유효한 이메일 형식이 아닙니다"
        print(f"  ✓ email 검증 통과: {dto.email}")
        
        # age 검증
        if dto.age is not None:
            if dto.age < 0 or dto.age > 120:
                return "❌ 오류: age는 0-120 사이여야 합니다"
            print(f"  ✓ age 검증 통과: {dto.age}")
        
        # 여기서야 비로소 실제 비즈니스 로직!
        print("\n  💾 검증 완료! 사용자 생성 중...")
        return f"✅ 사용자 생성 완료: {dto.name} ({dto.email})"


print("\n▶ 코드 구조:")
print("""
    class UserDto:
        # 검증 규칙 없음, 그냥 데이터만 담음
        user_id, name, email, age
    
    class UserService:
        def create_user(dto):
            # 여기서 모든 검증을 직접!
            if not dto.user_id: ...
            if len(dto.user_id) < 3: ...
            if not dto.email: ...
            if not 이메일형식: ...
            # ... 30줄의 검증 코드
            
            # 비즈니스 로직
            save(dto)
""")

print("\n▶ 테스트:")
print("\n  1. 유효한 데이터:")
dto1 = UserDtoTraditional("user123", "김철수", "kim@example.com", 25)
service1 = UserServiceTraditional()
result = service1.create_user(dto1)
print(f"  {result}")

print("\n  2. 유효하지 않은 데이터 (userId가 너무 짧음):")
dto2 = UserDtoTraditional("u1", "김철수", "kim@example.com", 25)
result = service1.create_user(dto2)
print(f"  {result}")

print("\n  3. 유효하지 않은 데이터 (email 형식 오류):")
dto3 = UserDtoTraditional("user123", "김철수", "invalid-email", 25)
result = service1.create_user(dto3)
print(f"  {result}")

print("\n❌ 문제점:")
print("  • 검증 코드가 비즈니스 로직과 섞임 (가독성 나쁨)")
print("  • updateUser, deleteUser 등 다른 메서드에서도 같은 검증 필요 (중복!)")
print("  • 검증 규칙 변경 시 여러 곳 수정 필요")
print("  • DTO만 봐서는 어떤 규칙이 있는지 알 수 없음")


# ============================================
# 방법 2: Bean Validation 방식 (객체에 검증 규칙 선언)
# ============================================

print("\n" + "="*80)
print("방법 2️⃣: Bean Validation 방식 - 객체에 검증 규칙 선언!")
print("="*80)

# DTO - 검증 규칙이 객체 안에 선언되어 있음!
@dataclass
class UserDtoBeanValidation:
    """
    검증 규칙이 포함된 DTO
    
    Java로 표현하면:
    
    public class UserDto {
        @NotNull
        @Size(min=3, max=50)
        @Pattern(regexp="^[a-zA-Z0-9]+$")
        private String userId;  // ← 검증 규칙이 필드 위에!
        
        @NotBlank
        @Size(min=2, max=100)
        private String name;
        
        @Email
        @NotNull
        private String email;
        
        @Min(0) @Max(120)
        private Integer age;
    }
    """
    user_id: str
    name: str
    email: str
    age: Optional[int] = None
    
    def __post_init__(self):
        """
        객체 생성 시 자동으로 검증!
        
        Java에서는 @Valid를 붙이면 Spring이 자동으로 이 검증을 수행
        """
        errors = []
        
        # userId 검증 규칙
        if not self.user_id:
            errors.append("userId는 필수입니다")
        elif len(self.user_id) < 3 or len(self.user_id) > 50:
            errors.append("userId는 3-50자여야 합니다")
        elif not self.user_id.isalnum():
            errors.append("userId는 영문자와 숫자만 가능합니다")
        
        # name 검증 규칙
        if not self.name or not self.name.strip():
            errors.append("name은 필수입니다")
        elif len(self.name) < 2 or len(self.name) > 100:
            errors.append("name은 2-100자여야 합니다")
        
        # email 검증 규칙
        if not self.email:
            errors.append("email은 필수입니다")
        else:
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, self.email):
                errors.append("유효한 이메일 형식이 아닙니다")
        
        # age 검증 규칙
        if self.age is not None and (self.age < 0 or self.age > 120):
            errors.append("age는 0-120 사이여야 합니다")
        
        if errors:
            raise ValueError(f"검증 실패: {', '.join(errors)}")


# Service - 검증 코드 없음! 순수 비즈니스 로직만!
class UserServiceBeanValidation:
    """Bean Validation 서비스: 검증 로직이 없음!"""
    
    def create_user(self, dto: UserDtoBeanValidation):
        """
        사용자 생성 - 검증 코드 없음!
        
        Java로 표현하면:
        
        @PostMapping
        public User createUser(@Valid @RequestBody UserDto dto) {
            // 여기 도달했다면 이미 검증 통과!
            // dto의 모든 필드가 규칙에 맞음
            return userRepository.save(dto);
        }
        """
        # 검증은 이미 DTO 생성 시 완료됨!
        # 바로 비즈니스 로직 시작
        print(f"\n  💾 사용자 생성 중... (검증은 이미 완료됨)")
        return f"✅ 사용자 생성 완료: {dto.name} ({dto.email})"


print("\n▶ 코드 구조:")
print("""
    class UserDto:
        # 객체에 검증 규칙 선언!
        user_id: str  # ← 3-50자, 영문+숫자만
        email: str    # ← 이메일 형식
        age: int      # ← 0-120 사이
        
        __post_init__():
            # 객체 생성 시 자동 검증!
            if not 규칙: raise Error
    
    class UserService:
        def create_user(dto):
            # 검증 코드 없음!
            # dto가 생성되었다면 이미 검증 통과!
            save(dto)
""")

print("\n▶ 테스트:")
print("\n  1. 유효한 데이터 (객체 생성 시 자동 검증!):")
try:
    dto1 = UserDtoBeanValidation("user123", "김철수", "kim@example.com", 25)
    print(f"  ✅ 객체 생성 성공: {dto1}")
    service2 = UserServiceBeanValidation()
    result = service2.create_user(dto1)
    print(f"  {result}")
except ValueError as e:
    print(f"  ❌ 객체 생성 실패: {e}")

print("\n  2. 유효하지 않은 데이터 (객체 생성 자체가 실패!):")
try:
    dto2 = UserDtoBeanValidation("u1", "김철수", "kim@example.com", 25)
    print(f"  객체 생성 성공: {dto2}")
except ValueError as e:
    print(f"  ❌ 객체 생성 실패 (Controller까지 도달하지도 못함!)")
    print(f"     {e}")

print("\n  3. 여러 필드가 잘못된 경우:")
try:
    dto3 = UserDtoBeanValidation("u1", "", "invalid", 999)
    print(f"  객체 생성 성공: {dto3}")
except ValueError as e:
    print(f"  ❌ 객체 생성 실패")
    print(f"     {e}")

print("\n✅ 장점:")
print("  • 검증 규칙이 객체(DTO)에 집중됨 (한눈에 파악)")
print("  • 서비스 로직은 순수 비즈니스 로직만 (가독성 좋음)")
print("  • 객체 생성 = 검증 완료 (자동!)")
print("  • 재사용성 (같은 DTO를 여러 곳에서 사용해도 동일한 검증)")


# ============================================
# 핵심 개념 정리
# ============================================

print("\n" + "="*80)
print("🎓 핵심 개념 정리")
print("="*80)

print("""
1️⃣ "객체"란?
   → UserDto 같은 데이터를 담는 클래스

2️⃣ "객체에 검증 규칙을 선언"이란?
   → UserDto 클래스 정의할 때 각 필드마다 검증 규칙을 함께 작성
   
   Java 예시:
   public class UserDto {
       @NotNull          // ← 검증 규칙 (null이면 안됨)
       @Size(min=3)      // ← 검증 규칙 (최소 3자)
       private String userId;  // ← 데이터 필드
   }

3️⃣ "객체가 검증한다"란?
   → 객체를 생성할 때 자동으로 검증이 수행됨
   → 검증 통과해야만 객체 생성 성공
   
   // 객체 생성 시도
   UserDto dto = new UserDto("u1", ...);  // ← 검증 실패! 예외 발생
   UserDto dto = new UserDto("user123", ...);  // ← 검증 통과! 객체 생성 성공

4️⃣ Controller에서 @Valid의 역할
   → 요청 데이터를 객체로 변환하면서 자동 검증
   → 검증 실패 시 Controller 메서드 실행 안됨 (자동으로 400 응답)
   → 검증 통과 시 메서드 실행 (안심하고 데이터 사용 가능!)

5️⃣ 왜 "Bean Validation"이라고 부르나?
   → Java에서 데이터 객체를 "Bean"이라고 부름
   → Bean(객체)을 Validation(검증)하는 것
   → Bean Validation = 객체 검증
""")

print("\n" + "="*80)
print("📊 전통적 방식 vs Bean Validation 비교")
print("="*80)

print("""
┌─────────────────────────────────────────────────────────────────────┐
│                          전통적 방식                                 │
├─────────────────────────────────────────────────────────────────────┤
│ Controller: 데이터 받음 → Service로 전달                            │
│ Service:    검증 30줄 + 비즈니스 로직 10줄                          │
│                                                                     │
│ 문제점:                                                              │
│ - 검증 코드가 비즈니스 로직과 섞임                                  │
│ - createUser, updateUser마다 중복 검증                              │
│ - DTO 보고는 어떤 규칙인지 모름                                     │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                        Bean Validation                              │
├─────────────────────────────────────────────────────────────────────┤
│ DTO:        검증 규칙 선언 (어노테이션)                             │
│ Controller: @Valid만 붙임 (자동 검증!)                              │
│ Service:    순수 비즈니스 로직만 10줄                               │
│                                                                     │
│ 장점:                                                                │
│ - 검증 규칙이 DTO에 집중 (한눈에 파악)                              │
│ - Service는 깔끔 (비즈니스 로직만)                                  │
│ - DTO 재사용 시 검증도 함께 적용                                    │
│ - 중복 코드 제거                                                     │
└─────────────────────────────────────────────────────────────────────┘
""")

print("\n💡 결론:")
print("  \"객체 검증\" = 객체(DTO)에 검증 규칙을 선언해두고,")
print("                객체 생성 시 자동으로 검증하는 방식!")
print("\n  값은 검증하되, 검증 방법이 다릅니다:")
print("  - 전통적: 서비스에서 if문으로 직접 검증")
print("  - Bean Validation: 객체 정의 시 규칙 선언, @Valid로 자동 검증")

print("\n" + "="*80)

