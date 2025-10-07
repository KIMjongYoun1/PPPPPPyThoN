# 파이썬 설치 및 환경 설정 가이드

## 1. 파이썬 설치

### macOS (현재 시스템)
macOS에는 기본적으로 Python 2.7이 설치되어 있지만, 최신 Python 3를 설치하는 것을 권장합니다.

#### 방법 1: 공식 웹사이트에서 설치
1. [Python 공식 웹사이트](https://www.python.org/downloads/) 방문
2. "Download Python 3.x.x" 버튼 클릭
3. 다운로드된 `.pkg` 파일 실행하여 설치

#### 방법 2: Homebrew 사용 (권장)
```bash
# Homebrew가 설치되어 있지 않다면
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Python 설치
brew install python
```

#### 방법 3: pyenv 사용 (여러 버전 관리)
```bash
# pyenv 설치
brew install pyenv

# Python 3.11 설치
pyenv install 3.11.0

# 전역 Python 버전 설정
pyenv global 3.11.0

# 쉘 설정에 추가 (zsh 사용 중)
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc
```

## 2. 설치 확인

터미널에서 다음 명령어로 설치를 확인하세요:

```bash
python3 --version
pip3 --version
```

## 3. 가상환경 설정

파이썬 프로젝트마다 독립적인 환경을 만들기 위해 가상환경을 사용합니다.

### venv 사용 (Python 3.3+ 내장)
```bash
# 가상환경 생성
python3 -m venv my_python_env

# 가상환경 활성화
source my_python_env/bin/activate

# 가상환경 비활성화
deactivate
```

### virtualenv 사용
```bash
# virtualenv 설치
pip3 install virtualenv

# 가상환경 생성
virtualenv my_python_env

# 가상환경 활성화
source my_python_env/bin/activate
```

## 4. IDE 및 에디터 설정

### VS Code (권장)
1. [VS Code](https://code.visualstudio.com/) 설치
2. Python 확장 프로그램 설치
3. 설정에서 Python 인터프리터 경로 지정

### PyCharm
1. [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/) 다운로드
2. 설치 후 프로젝트 생성

### Jupyter Notebook
```bash
# Jupyter 설치
pip3 install jupyter

# Jupyter 실행
jupyter notebook
```

## 5. 필수 패키지 설치

```bash
# 가상환경 활성화 후
pip install requests  # HTTP 요청
pip install numpy     # 수치 계산
pip install pandas    # 데이터 분석
pip install matplotlib # 그래프 그리기
pip install pytest    # 테스트
```

## 6. 프로젝트 구조

```
my_python_project/
├── src/              # 소스 코드
├── tests/            # 테스트 코드
├── docs/             # 문서
├── requirements.txt  # 의존성 목록
└── README.md         # 프로젝트 설명
```

## 7. requirements.txt 생성

```bash
# 현재 설치된 패키지 목록 저장
pip freeze > requirements.txt

# 다른 환경에서 동일한 패키지 설치
pip install -r requirements.txt
```

## 8. 첫 번째 파이썬 프로그램

`hello.py` 파일을 만들어보세요:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    print("안녕하세요! 파이썬을 시작합니다!")
    print("Python version:", __import__('sys').version)

if __name__ == "__main__":
    main()
```

실행:
```bash
python3 hello.py
```

## 9. 자바/리액트 개발자에게 유용한 팁

### 자바와의 차이점
- **세미콜론 불필요**: 파이썬은 줄바꿈으로 문장 구분
- **중괄호 대신 들여쓰기**: 코드 블록은 들여쓰기로 구분
- **동적 타입**: 변수 타입을 미리 선언하지 않음
- **간결한 문법**: 같은 기능을 더 적은 코드로 작성 가능

### 리액트와의 공통점
- **함수형 프로그래밍**: 람다, map, filter 등 지원
- **모듈 시스템**: import/export와 유사한 import 문법
- **패키지 관리**: npm과 유사한 pip 사용

## 10. 다음 단계

설치가 완료되면 다음 학습 단계로 진행하세요:
1. 파이썬 기본 문법
2. 데이터 타입과 변수
3. 제어 구조 (조건문, 반복문)
4. 함수 정의와 사용
5. 클래스와 객체지향 프로그래밍

---

**문제 해결**
- `python3` 명령어가 인식되지 않으면 PATH 설정 확인
- 권한 오류 시 `sudo` 사용하거나 사용자 디렉토리에 설치
- 가상환경 활성화가 안 되면 경로 확인
