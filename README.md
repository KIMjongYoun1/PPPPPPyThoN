# 파이썬 학습 가이드

자바와 리액트 경험이 있는 개발자를 위한 파이썬 완전 학습 가이드입니다.

## 📚 학습 순서

### 1. [파이썬 설치 및 환경 설정](01_python_setup.md)
- 파이썬 설치 방법 (macOS, Windows, Linux)
- 가상환경 설정
- IDE 및 에디터 설정
- 필수 패키지 설치
- 자바/리액트 개발자를 위한 팁

### 2. [파이썬 기본 문법](02_python_basics.md)
- 변수와 데이터 타입
- 문자열 다루기
- 숫자 연산
- 입력과 출력
- 들여쓰기와 코드 블록
- 자바/리액트와의 차이점

### 3. [데이터 구조](03_data_structures.md)
- 리스트 (List)
- 딕셔너리 (Dictionary)
- 튜플 (Tuple)
- 집합 (Set)
- 문자열 시퀀스
- 컴프리헨션 활용

### 4. [제어 구조](04_control_flow.md)
- 조건문 (if, elif, else)
- 반복문 (for, while)
- 함수 정의와 사용
- 람다 함수
- 스코프와 네임스페이스

### 5. [객체지향 프로그래밍](05_object_oriented_programming.md)
- 클래스와 객체
- 상속과 다형성
- 캡슐화
- 특수 메서드
- 자바와의 비교

### 6. [모듈과 패키지](06_modules_packages.md)
- 모듈 생성과 사용
- 패키지 구조
- 내장 모듈 활용
- 외부 패키지 설치
- 프로젝트 구조화

### 7. [실습 예제 및 프로젝트](07_practical_examples.md)
- 계산기 프로그램
- 학생 성적 관리 시스템
- 웹 스크래퍼
- 파일 관리 도구
- 실행 가능한 완전한 예제

### 8. [코딩 스타일 및 모범 사례](08_best_practices.md)
- PEP 8 스타일 가이드
- 명명 규칙
- 함수와 클래스 설계
- 예외 처리
- 문서화
- 테스트 작성

## 🚀 빠른 시작

### 1. 환경 설정
```bash
# 파이썬 설치 확인
python3 --version

# 가상환경 생성
python3 -m venv my_python_env

# 가상환경 활성화 (macOS/Linux)
source my_python_env/bin/activate

# 가상환경 활성화 (Windows)
my_python_env\Scripts\activate

# 필수 패키지 설치
pip install requests numpy pandas matplotlib pytest
```

### 2. 첫 번째 파이썬 프로그램
```python
# hello.py
def greet(name):
    return f"안녕하세요, {name}님! 파이썬을 시작합니다!"

if __name__ == "__main__":
    name = input("이름을 입력하세요: ")
    print(greet(name))
```

### 3. 실행
```bash
python3 hello.py
```

## 🎯 학습 목표

### 초급 (1-2주)
- [ ] 파이썬 기본 문법 이해
- [ ] 데이터 구조 활용
- [ ] 기본 제어 구조 사용
- [ ] 간단한 함수 작성

### 중급 (3-4주)
- [ ] 객체지향 프로그래밍 이해
- [ ] 모듈과 패키지 사용
- [ ] 예외 처리 구현
- [ ] 파일 입출력 처리

### 고급 (5-6주)
- [ ] 복잡한 프로젝트 구현
- [ ] 외부 라이브러리 활용
- [ ] 테스트 코드 작성
- [ ] 코드 품질 향상

## 🛠️ 실습 프로젝트

### 1. 계산기 프로그램
- 기본 사칙연산
- 과학 계산 기능
- 계산 기록 관리

### 2. 학생 성적 관리 시스템
- 학생 정보 관리
- 성적 입력 및 조회
- 통계 분석
- 데이터 저장/로드

### 3. 웹 스크래퍼
- 웹 페이지 데이터 추출
- 뉴스 헤드라인 수집
- 상품 정보 수집
- 데이터 저장

### 4. 파일 관리 도구
- 파일/폴더 관리
- 파일 검색
- 파일 해시 확인
- 작업 기록 관리

## 📖 추가 학습 자료

### 공식 문서
- [Python 공식 문서](https://docs.python.org/3/)
- [PEP 8 스타일 가이드](https://pep8.org/)

### 온라인 튜토리얼
- [Python.org 튜토리얼](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)

### 추천 도서
- "파이썬 코딩의 기술" - Brett Slatkin
- "Effective Python" - Brett Slatkin
- "Fluent Python" - Luciano Ramalho

## 🔧 개발 도구

### IDE/에디터
- **VS Code** (권장) - 무료, 확장성 좋음
- **PyCharm** - 전문적인 Python IDE
- **Sublime Text** - 가벼운 텍스트 에디터

### 필수 확장 프로그램 (VS Code)
- Python
- Python Docstring Generator
- Python Test Explorer
- GitLens

### 코드 품질 도구
```bash
# 코드 포맷팅
pip install black

# 린팅
pip install flake8

# 타입 체킹
pip install mypy

# 테스트
pip install pytest
```

## 🎓 자바/리액트 개발자를 위한 핵심 차이점

### 자바와의 주요 차이점
| 자바 | 파이썬 |
|------|--------|
| `public class MyClass {}` | `class MyClass:` |
| `int x = 5;` | `x = 5` |
| `if (condition) { }` | `if condition:` |
| `for (int i = 0; i < 10; i++)` | `for i in range(10):` |
| `List<String> list = new ArrayList<>();` | `list = []` |
| `Map<String, Integer> map = new HashMap<>();` | `dict = {}` |

### 리액트와의 공통점
- 함수형 프로그래밍 스타일
- 컴포넌트/모듈 기반 구조
- 동적 타입 (TypeScript 없이)
- 풍부한 생태계

## 🚨 주의사항

### 자주 하는 실수
1. **들여쓰기 오류**: 파이썬은 들여쓰기가 문법의 일부
2. **세미콜론 사용**: 파이썬에서는 불필요
3. **타입 선언**: 파이썬은 동적 타입 언어
4. **변수 스코프**: 함수 내에서 전역 변수 수정 시 `global` 키워드 필요

### 성능 고려사항
- 리스트 vs 튜플: 불변 데이터는 튜플 사용
- 딕셔너리 vs 리스트: 빠른 검색이 필요하면 딕셔너리
- 제너레이터: 큰 데이터 처리 시 메모리 효율적

## 📞 도움 요청

### 문제 해결 순서
1. 오류 메시지 자세히 읽기
2. 공식 문서 확인
3. Stack Overflow 검색
4. 커뮤니티 질문

### 유용한 커뮤니티
- [Python 한국 사용자 그룹](https://www.facebook.com/groups/pythonkorea/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/python)
- [Reddit r/Python](https://www.reddit.com/r/Python/)

## 🎉 다음 단계

파이썬 기초를 마스터한 후 고려할 분야:

### 웹 개발
- **Flask**: 가벼운 웹 프레임워크
- **Django**: 풀스택 웹 프레임워크
- **FastAPI**: 고성능 API 프레임워크

### 데이터 분석
- **NumPy**: 수치 계산
- **Pandas**: 데이터 조작
- **Matplotlib/Seaborn**: 데이터 시각화

### 머신러닝
- **Scikit-learn**: 머신러닝 라이브러리
- **TensorFlow/PyTorch**: 딥러닝 프레임워크

### 자동화
- **Selenium**: 웹 자동화
- **Requests**: HTTP 요청
- **BeautifulSoup**: HTML 파싱

---

**Happy Coding! 🐍**

파이썬 학습 여정을 즐기시고, 궁금한 점이 있으면 언제든 질문해주세요!
