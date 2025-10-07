#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
hello_world.py를 import해서 사용하는 예시
"""

# hello_world 모듈을 import
from hello_world import main

print("=" * 50)
print("이것은 test_import.py 파일입니다")
print("=" * 50)

# hello_world의 함수를 사용할 수 있지만,
# hello_world.py의 if __name__ == "__main__": 블록은 실행되지 않습니다!

print("\n이제 hello_world의 main()을 명시적으로 호출해볼게요:")
print("-" * 50)
main()  # 명시적으로 호출해야 실행됨

