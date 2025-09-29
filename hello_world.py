#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    print("🎉 파이썬 학습을 시작합니다!")
    print("=" * 40)
    
    # 변수 사용
    name = "파이썬 학습자"
    age = 2024
    
    print(f"안녕하세요, {name}님!")
    print(f"파이썬 버전: {age}년도 학습")
    
    # 간단한 계산
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    print(f"숫자 리스트: {numbers}")
    print(f"합계: {total}")
    
    # 조건문
    if total > 10:
        print("합계가 10보다 큽니다! ✅")
    else:
        print("합계가 10 이하입니다.")
    
    print("=" * 40)
    print("파이썬 학습 화이팅! 🐍")

if __name__ == "__main__":
    main()

