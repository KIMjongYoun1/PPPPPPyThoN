#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
파이썬 패키지 구조 이해를 위한 데모
"""

import os
import sys

def show_current_structure():
    """현재 디렉토리 구조 보여주기"""
    print("🔍 현재 디렉토리 구조:")
    print("=" * 50)
    
    current_dir = os.getcwd()
    print(f"현재 위치: {current_dir}")
    print()
    
    # 현재 디렉토리의 내용 보기
    items = os.listdir(current_dir)
    for item in sorted(items):
        item_path = os.path.join(current_dir, item)
        if os.path.isdir(item_path):
            print(f"📁 {item}/")
        else:
            print(f"📄 {item}")

def explain_virtual_environment():
    """가상환경 구조 설명"""
    print("\n🐍 가상환경 (my_python_env) 구조 설명:")
    print("=" * 50)
    
    explanations = {
        "bin/": "실행 파일들 (python, pip, activate 등)",
        "lib/": "설치된 파이썬 패키지들이 저장되는 곳",
        "include/": "C 확장 모듈을 위한 헤더 파일들",
        "pyvenv.cfg": "가상환경 설정 정보 파일"
    }
    
    for folder, description in explanations.items():
        print(f"📁 {folder:<15} → {description}")

def show_java_vs_python_structure():
    """자바 vs 파이썬 패키지 구조 비교"""
    print("\n📦 자바 vs 파이썬 패키지 구조 비교:")
    print("=" * 50)
    
    print("☕ 자바 구조:")
    print("""
    my-java-project/
    ├── src/
    │   └── main/
    │       └── java/
    │           └── com/
    │               └── example/
    │                   └── myproject/
    │                       ├── Main.java
    │                       ├── model/
    │                       │   └── User.java
    │                       └── service/
    │                           └── UserService.java
    └── pom.xml
    """)
    
    print("🐍 파이썬 구조:")
    print("""
    my-python-project/
    ├── src/
    │   └── myproject/
    │       ├── __init__.py      ← 자바에는 없음!
    │       ├── main.py
    │       ├── models/
    │       │   ├── __init__.py  ← 자바에는 없음!
    │       │   └── user.py
    │       └── services/
    │           ├── __init__.py  ← 자바에는 없음!
    │           └── user_service.py
    ├── tests/
    ├── requirements.txt         ← pom.xml과 비슷
    └── setup.py
    """)

def create_sample_package_structure():
    """샘플 패키지 구조 생성"""
    print("\n🛠️  샘플 파이썬 패키지 구조 생성:")
    print("=" * 50)
    
    # 패키지 구조 생성
    package_structure = {
        "my_sample_project": {
            "src": {
                "myproject": {
                    "__init__.py": "# MyProject 패키지",
                    "main.py": "# 메인 실행 파일",
                    "models": {
                        "__init__.py": "# 모델 패키지",
                        "user.py": "# User 클래스",
                        "product.py": "# Product 클래스"
                    },
                    "services": {
                        "__init__.py": "# 서비스 패키지", 
                        "user_service.py": "# UserService 클래스",
                        "product_service.py": "# ProductService 클래스"
                    },
                    "utils": {
                        "__init__.py": "# 유틸리티 패키지",
                        "helpers.py": "# 헬퍼 함수들"
                    }
                }
            },
            "tests": {
                "__init__.py": "# 테스트 패키지",
                "test_models.py": "# 모델 테스트",
                "test_services.py": "# 서비스 테스트"
            },
            "requirements.txt": "# 패키지 의존성",
            "setup.py": "# 패키지 설치 설정",
            "README.md": "# 프로젝트 설명"
        }
    }
    
    print("생성할 패키지 구조:")
    print_structure(package_structure, "")

def print_structure(structure, indent):
    """구조를 예쁘게 출력"""
    for key, value in structure.items():
        if isinstance(value, dict):
            print(f"{indent}📁 {key}/")
            print_structure(value, indent + "  ")
        else:
            print(f"{indent}📄 {key}")

def show_import_examples():
    """파이썬 임포트 예제"""
    print("\n📥 파이썬 임포트 예제:")
    print("=" * 50)
    
    examples = [
        ("# 패키지에서 모듈 임포트", "from myproject.models import user"),
        ("# 패키지에서 클래스 임포트", "from myproject.models.user import User"),
        ("# 서브패키지 임포트", "from myproject.services import user_service"),
        ("# 유틸리티 함수 임포트", "from myproject.utils.helpers import format_name"),
        ("# 전체 패키지 임포트", "import myproject"),
    ]
    
    for comment, code in examples:
        print(f"{comment}")
        print(f"  {code}")
        print()

def main():
    """메인 함수"""
    print("🎯 파이썬 패키지 구조 이해하기")
    print("=" * 60)
    
    show_current_structure()
    explain_virtual_environment()
    show_java_vs_python_structure()
    create_sample_package_structure()
    show_import_examples()
    
    print("\n💡 핵심 포인트:")
    print("1. 가상환경 ≠ 프로젝트 패키지 구조")
    print("2. 파이썬은 __init__.py로 패키지 정의")
    print("3. 자바의 src/ 구조와 유사하지만 __init__.py 필요")
    print("4. requirements.txt = 자바의 pom.xml")

if __name__ == "__main__":
    main()
