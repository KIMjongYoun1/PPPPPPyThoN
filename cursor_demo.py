#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Cursor IDE에서 파이썬 학습을 위한 데모 파일
이 파일을 Cursor에서 열고 F5를 눌러서 실행해보세요!
"""

def greet_user():
    """사용자에게 인사하는 함수"""
    name = input("이름을 입력하세요: ")
    print(f"안녕하세요, {name}님! 파이썬 학습을 시작해봅시다! 🐍")

def calculate_demo():
    """간단한 계산 데모"""
    print("\n=== 계산 데모 ===")
    
    # 숫자 입력 받기
    try:
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))
        
        # 계산 결과 출력
        print(f"\n계산 결과:")
        print(f"{num1} + {num2} = {num1 + num2}")
        print(f"{num1} - {num2} = {num1 - num2}")
        print(f"{num1} × {num2} = {num1 * num2}")
        
        if num2 != 0:
            print(f"{num1} ÷ {num2} = {num1 / num2:.2f}")
        else:
            print("0으로 나눌 수 없습니다!")
            
    except ValueError:
        print("올바른 숫자를 입력해주세요!")

def list_demo():
    """리스트 데모"""
    print("\n=== 리스트 데모 ===")
    
    # 과일 리스트
    fruits = ["사과", "바나나", "오렌지", "포도", "딸기"]
    print(f"과일 목록: {fruits}")
    
    # 리스트 조작
    fruits.append("키위")
    print(f"키위 추가 후: {fruits}")
    
    # 리스트 정렬
    fruits.sort()
    print(f"정렬 후: {fruits}")
    
    # 리스트 컴프리헨션
    long_fruits = [fruit for fruit in fruits if len(fruit) > 2]
    print(f"긴 이름의 과일: {long_fruits}")

def dictionary_demo():
    """딕셔너리 데모"""
    print("\n=== 딕셔너리 데모 ===")
    
    # 학생 정보 딕셔너리
    student = {
        "이름": "김철수",
        "나이": 25,
        "전공": "컴퓨터공학",
        "성적": [85, 92, 78, 96]
    }
    
    print("학생 정보:")
    for key, value in student.items():
        print(f"  {key}: {value}")
    
    # 성적 평균 계산
    grades = student["성적"]
    average = sum(grades) / len(grades)
    print(f"\n성적 평균: {average:.2f}")

def main():
    """메인 함수"""
    print("🎉 Cursor IDE에서 파이썬 학습 데모")
    print("=" * 50)
    
    # 각 데모 실행
    greet_user()
    calculate_demo()
    list_demo()
    dictionary_demo()
    
    print("\n" + "=" * 50)
    print("데모가 완료되었습니다! 🎊")
    print("이제 01_python_setup.md부터 차근차근 학습해보세요!")

if __name__ == "__main__":
    main()
