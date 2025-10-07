# 📁 Python 학습 프로젝트 구조

**Java 개발자를 위한 Python 학습 프로젝트**

---

## 🗂️ 디렉토리 구조

```
/Users/ryankim/Python/
│
├── 📘 01_가이드문서/              # 학습 가이드 및 문서
│   ├── 00_학습_로드맵.md          # 전체 학습 계획
│   ├── 01_python_setup.md         # 환경 설정 가이드
│   ├── 02_python_basics.md        # 기본 문법
│   ├── 03_data_structures.md      # 자료구조
│   ├── 04_control_flow.md         # 제어문
│   ├── 05_object_oriented_programming.md  # 객체지향
│   ├── 06_modules_packages.md     # 모듈과 패키지
│   ├── 07_practical_examples.md   # 실전 예제
│   ├── 08_best_practices.md       # 모범 사례
│   ├── PYTHON_BASICS_FOR_JAVA.md  # Java 개발자용 가이드
│   ├── Python_치트시트_Java개발자용.md  # 빠른 참조
│   ├── package_structure_guide.md  # 패키지 구조 가이드
│   ├── validation_explained.md     # 유효성 검사 설명
│   └── README.md                  # 프로젝트 설명
│
├── 📝 02_실습코드/                # 연습 및 실습 코드
│   ├── 02_practice.py             # 02장 실습 (진행 중!)
│   ├── 02_string_formatting_practice.py  # 문자열 포맷팅 실습
│   ├── hello_world.py             # 첫 프로그램
│   ├── cursor_demo.py             # Cursor 데모
│   ├── decorator_example.py       # 데코레이터 예제
│   ├── bean_validation_demo.py    # 유효성 검사 데모
│   ├── package_structure_demo.py  # 패키지 구조 데모
│   ├── python_basics_examples.py  # 기본 문법 예제
│   ├── validation_comparison.py   # Java vs Python 비교
│   └── test_import.py             # import 테스트
│
├── ✅ 03_정답지/                  # 실습 정답 코드
│   ├── 01_answer.py               # 01장 정답
│   ├── 02_answer.py               # 02장 정답
│   └── 02_string_formatting_answer.py  # 문자열 포맷팅 정답
│
├── 📔 04_학습일지/                # 학습 기록 및 메모
│   ├── 학습_일지_Day1.md          # Day 1 학습 기록
│   ├── 시작하기.txt               # 시작 가이드
│   ├── 실습_가이드.txt            # 실습 가이드
│   └── 학습_가이드_완전판.md      # 완전판 가이드
│
├── 🔧 my_python_env/              # 가상환경 (건드리지 말 것!)
├── 📦 my_sample_app/              # Flask 샘플 앱
├── 📄 requirements.txt            # 패키지 목록
└── 📂 tests/                      # 테스트 파일들

```

---

## 🚀 빠른 시작

### 1. 가상환경 활성화
```bash
cd /Users/ryankim/Python
source my_python_env/bin/activate
```

### 2. 학습 시작
```bash
# 가이드 문서 읽기
cat 01_가이드문서/00_학습_로드맵.md

# 실습 파일 열기
open 02_실습코드/02_practice.py  # Cursor에서

# 실습 실행
python3 02_실습코드/02_practice.py

# 정답 확인
python3 03_정답지/02_answer.py
```

### 3. 학습 일지 작성
```bash
# 오늘의 학습 기록
open 04_학습일지/학습_일지_Day1.md
```

---

## 📚 학습 순서

### Week 1-2: Python 기초
1. **환경 설정** ✅
   - 가이드: `01_가이드문서/01_python_setup.md`
   - 실습: 가상환경 생성 및 활성화

2. **기본 문법** (진행 중)
   - 가이드: `01_가이드문서/02_python_basics.md`
   - 실습: `02_실습코드/02_practice.py`
   - 정답: `03_정답지/02_answer.py`

3. **자료구조**
   - 가이드: `01_가이드문서/03_data_structures.md`

4. **제어 구조**
   - 가이드: `01_가이드문서/04_control_flow.md`

### Week 3-4: Python 중급
5. **객체지향**
6. **모듈과 패키지**
7. **실전 예제**
8. **모범 사례**

---

## 🎯 학습 방법

### 1단계: 이론 학습
```bash
# 가이드 문서 읽기
01_가이드문서/XX_theory.md
```

### 2단계: 실습
```bash
# 실습 파일 작성
02_실습코드/XX_practice.py

# 실행
python3 02_실습코드/XX_practice.py
```

### 3단계: 정답 비교
```bash
# 정답 확인
03_정답지/XX_answer.py
```

### 4단계: 기록
```bash
# 학습 일지 작성
04_학습일지/학습_일지_DayX.md
```

---

## 🔧 자주 사용하는 명령어

### 가상환경
```bash
# 활성화
source my_python_env/bin/activate

# 비활성화
deactivate

# 확인
which python3
```

### 실행
```bash
# 파일 실행
python3 02_실습코드/파일명.py

# 인터랙티브 모드
python3

# 한 줄 실행
python3 -c "print('Hello')"
```

### 패키지 관리
```bash
# 설치
pip install 패키지명

# 목록
pip list

# 저장
pip freeze > requirements.txt

# 설치
pip install -r requirements.txt
```

---

## 📖 주요 파일 설명

### 가이드 문서
- **00_학습_로드맵.md**: 전체 학습 계획 및 체크리스트
- **Python_치트시트_Java개발자용.md**: 빠른 참조용 핵심 문법

### 실습 코드
- **02_practice.py**: 현재 진행 중인 메인 실습 파일
- **hello_world.py**: 첫 Python 프로그램

### 정답지
- **02_answer.py**: 실습 파일의 완성된 정답 코드

### 학습 일지
- **학습_일지_Day1.md**: 오늘 배운 내용 상세 기록

---

## 💡 팁

### DO ✅
- 매일 가상환경 활성화
- 직접 타이핑 (복붙 금지!)
- 에러 메시지 잘 읽기
- 학습 일지 작성하기

### DON'T ❌
- 가상환경 폴더 건드리지 말기
- 정답 먼저 보지 말기
- 순서 건너뛰지 말기

---

## 📞 도움이 필요하면?

1. **가이드 문서 확인**
   - `01_가이드문서/` 폴더의 관련 문서

2. **치트시트 확인**
   - `01_가이드문서/Python_치트시트_Java개발자용.md`

3. **학습 일지 복습**
   - `04_학습일지/` 폴더의 이전 기록

4. **정답 비교**
   - `03_정답지/` 폴더의 정답 코드

---

## 📈 학습 진행 상황

- [x] Week 1 Day 1-2: 환경 설정
- [x] Week 1 Day 3-5: 기본 문법 시작
- [ ] Week 1 Day 6-8: 자료구조
- [ ] Week 1 Day 9-10: 제어 구조
- [ ] Week 2: 중급 과정

**현재 진행률: 약 15%**

---

**화이팅! 🚀**

마지막 업데이트: 2025년 10월 7일

