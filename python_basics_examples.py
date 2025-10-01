#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python 기본 문법 실습 예제
Java 개발자를 위한 단계별 학습

각 섹션을 주석 해제하면서 하나씩 실행해보세요!
"""

print("=" * 80)
print("🐍 Python 기본 문법 실습 시작!")
print("=" * 80)

# ============================================
# 1. print(f"...") - 문자열 포맷팅
# ============================================

print("\n" + "="*80)
print("1️⃣ print(f'...') - 문자열 포맷팅 (f-string)")
print("="*80)

# 변수 선언 (타입 선언 불필요!)
name = "김철수"
age = 25
height = 175.5

# f-string 사용 (f를 붙이면 {} 안에 변수를 넣을 수 있음!)
print(f"이름: {name}")
print(f"나이: {age}세")
print(f"키: {height}cm")

# 표현식도 가능!
print(f"내년 나이: {age + 1}세")
print(f"10년 후 나이: {age + 10}세")

# 계산
a = 10
b = 20
print(f"{a} + {b} = {a + b}")
print(f"{a} × {b} = {a * b}")

# 소수점 자릿수 지정
pi = 3.141592653589793
print(f"파이 값 (원본): {pi}")
print(f"파이 값 (소수점 2자리): {pi:.2f}")
print(f"파이 값 (소수점 4자리): {pi:.4f}")

# 천 단위 구분
price = 1234567890
print(f"가격: {price:,}원")

# Java와 비교
print("\n📊 Java와 비교:")
print("Java:   String msg = \"이름: \" + name + \", 나이: \" + age;")
print("Python: msg = f\"이름: {name}, 나이: {age}\"")


# ============================================
# 2. \n, \t - 이스케이프 시퀀스
# ============================================

print("\n" + "="*80)
print("2️⃣ \\n, \\t - 이스케이프 시퀀스")
print("="*80)

# \n - 줄바꿈 (New line)
print("첫 번째 줄\n두 번째 줄\n세 번째 줄")

print()  # 빈 줄

# \t - 탭 (Tab)
print("이름\t나이\t직업")
print("김철수\t25\t개발자")
print("이영희\t30\t디자이너")
print("박민수\t28\t기획자")

print()

# \\ - 백슬래시 출력
print("Windows 경로: C:\\Users\\Documents\\file.txt")
print("Linux 경로: /home/user/file.txt")

print()

# 여러 개 조합
print("=" * 50)
print("회원 정보")
print("=" * 50)
print("이름:\t김철수")
print("나이:\t25세")
print("주소:\t서울시 강남구\n\t테헤란로 123")
print("=" * 50)

# Java와 동일!
print("\n📊 Java와 비교:")
print("Java:   System.out.println(\"첫 줄\\n둘째 줄\");")
print("Python: print(\"첫 줄\\n둘째 줄\")  # 똑같음!")


# ============================================
# 3. def __init__ - 생성자 메서드
# ============================================

print("\n" + "="*80)
print("3️⃣ def __init__ - 생성자 메서드")
print("="*80)

# 클래스 정의
class User:
    """
    사용자 클래스
    
    Java로 표현하면:
    public class User {
        private String name;
        private int age;
        
        public User(String name, int age) {
            this.name = name;
            this.age = age;
        }
    }
    """
    
    # __init__: 생성자 (객체 생성 시 자동 실행)
    # self: Java의 this (자기 자신 참조)
    def __init__(self, name, age):
        print(f"  🔧 __init__ 호출됨! (생성자 실행)")
        self.name = name  # self.name = 인스턴스 변수
        self.age = age
        print(f"  ✅ {name}님의 User 객체 생성 완료!")
    
    # 메서드 정의 (첫 번째 매개변수는 항상 self)
    def introduce(self):
        print(f"  안녕하세요, {self.name}입니다. {self.age}세입니다.")
    
    def birthday(self):
        self.age += 1
        print(f"  🎂 생일 축하합니다! 이제 {self.age}세가 되셨습니다!")

# 객체 생성 (new 키워드 없음!)
print("\n▶ 객체 생성:")
user1 = User("김철수", 25)

print("\n▶ 메서드 호출:")
user1.introduce()

print("\n▶ 생일 축하:")
user1.birthday()
user1.introduce()

print("\n▶ 또 다른 객체 생성:")
user2 = User("이영희", 30)
user2.introduce()

print("\n📊 Java와 비교:")
print("""
Java:
    public class User {
        public User(String name) {  // 생성자 (클래스명과 동일)
            this.name = name;
        }
    }
    User user = new User("김철수");

Python:
    class User:
        def __init__(self, name):  # 생성자 (항상 __init__)
            self.name = name
    
    user = User("김철수")  # new 없음!
""")


# ============================================
# 4. 자주 보는 Python 기호들
# ============================================

print("\n" + "="*80)
print("4️⃣ 자주 보는 Python 기호들")
print("="*80)

# 별표(*) - 곱셈, 거듭제곱, 반복
print("\n▶ 별표(*) 사용법:")
print(f"3 * 4 = {3 * 4}")
print(f"2 ** 3 = {2 ** 3}  # 2의 3승")
print("=" * 30 + " # = 기호 30개")

# 콜론(:) - 코드 블록, 딕셔너리
print("\n▶ 콜론(:) 사용법:")
print("if, for, def, class 뒤에 콜론 필수!")

# 딕셔너리 (Java의 HashMap)
user_dict = {
    "name": "김철수",  # key: value
    "age": 25,
    "job": "개발자"
}
print(f"딕셔너리: {user_dict}")
print(f"이름: {user_dict['name']}")

# 들여쓰기 (Indentation)
print("\n▶ 들여쓰기 (Java의 {}와 동일!):")
print("Python은 들여쓰기로 코드 블록 구분!")

age = 25
if age > 18:
    print("  ✓ 성인입니다")
    print("  ✓ 투표 가능합니다")
    if age > 60:
        print("    ✓ 경로 우대 대상입니다")
print("블록 밖입니다")


# ============================================
# 5. 종합 예제
# ============================================

print("\n" + "="*80)
print("5️⃣ 종합 예제: 상품 관리 시스템")
print("="*80)

class Product:
    """상품 클래스"""
    
    # 클래스 변수 (모든 인스턴스가 공유)
    total_products = 0
    
    def __init__(self, name, price, stock):
        """생성자"""
        self.name = name
        self.price = price
        self.stock = stock
        Product.total_products += 1
        print(f"✅ 상품 등록: {name}")
    
    def display_info(self):
        """상품 정보 출력"""
        print("-" * 50)
        print(f"상품명:\t{self.name}")
        print(f"가격:\t{self.price:,}원")
        print(f"재고:\t{self.stock}개")
        print("-" * 50)
    
    def sell(self, quantity):
        """상품 판매"""
        if self.stock >= quantity:
            self.stock -= quantity
            total_price = self.price * quantity
            print(f"💰 {self.name} {quantity}개 판매 완료!")
            print(f"   총 금액: {total_price:,}원")
            print(f"   남은 재고: {self.stock}개")
            return True
        else:
            print(f"❌ 재고 부족! (현재 재고: {self.stock}개)")
            return False
    
    def restock(self, quantity):
        """재고 추가"""
        self.stock += quantity
        print(f"📦 {self.name} {quantity}개 입고 완료! (총 재고: {self.stock}개)")
    
    def __str__(self):
        """toString()과 유사"""
        return f"Product(name={self.name}, price={self.price:,}원, stock={self.stock}개)"

# 상품 생성
print("\n▶ 상품 등록:")
laptop = Product("노트북", 1200000, 10)
mouse = Product("마우스", 25000, 50)
keyboard = Product("키보드", 80000, 30)

# 상품 정보 출력
print("\n▶ 상품 정보:")
laptop.display_info()

# 판매
print("\n▶ 판매:")
laptop.sell(2)
print()
laptop.sell(5)
print()
laptop.sell(10)  # 재고 부족

# 재고 추가
print("\n▶ 재고 추가:")
laptop.restock(20)

# 전체 상품 수
print(f"\n📊 총 등록 상품 수: {Product.total_products}개")

# 상품 리스트
print("\n▶ 전체 상품 목록:")
products = [laptop, mouse, keyboard]
print("=" * 50)
for i, product in enumerate(products, 1):
    print(f"{i}. {product}")
print("=" * 50)


# ============================================
# 6. 실전 팁
# ============================================

print("\n" + "="*80)
print("6️⃣ 실전 팁")
print("="*80)

# 팁 1: 문자열 곱하기로 구분선 쉽게 만들기
print("\n▶ 팁 1: 구분선 만들기")
print("=" * 60)
print("제목".center(60))
print("=" * 60)

# 팁 2: print() 옵션 활용
print("\n▶ 팁 2: print() 옵션")
print("로딩 중", end="")
for i in range(5):
    print(".", end="", flush=True)
    # time.sleep(0.5)  # 실제로는 딜레이 추가
print(" 완료!")

# 팁 3: 여러 값 한번에 출력
print("\n▶ 팁 3: 여러 값 출력")
print("이름:", "김철수", "나이:", 25, "직업:", "개발자")
print("사과", "바나나", "오렌지", sep=" | ")
print(2025, 1, 15, sep="-")

# 팁 4: f-string 안에서 표현식 사용
print("\n▶ 팁 4: f-string 활용")
numbers = [1, 2, 3, 4, 5]
print(f"리스트: {numbers}")
print(f"리스트 길이: {len(numbers)}")
print(f"리스트 합계: {sum(numbers)}")
print(f"리스트 평균: {sum(numbers) / len(numbers):.2f}")


# ============================================
# 마무리
# ============================================

print("\n" + "="*80)
print("🎉 Python 기본 문법 실습 완료!")
print("="*80)

print("""
📚 학습한 내용:
1. print(f"...") - 문자열 포맷팅
2. \\n, \\t - 이스케이프 시퀀스  
3. def __init__ - 생성자 메서드
4. 자주 보는 Python 기호들
5. 종합 예제 - 클래스 활용
6. 실전 팁

💡 다음 단계:
1. 이 코드를 수정해보면서 실험하기
2. 자신만의 클래스 만들어보기
3. 궁금한 부분은 언제든 질문하기!

📖 참고 문서:
- PYTHON_BASICS_FOR_JAVA.md (상세 설명)
- 02_python_basics.md (기존 학습 자료)
""")

print("=" * 80)

