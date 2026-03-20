# Python 입문 → 빅데이터분석기사 취득

**파이썬 기초부터 빅분기 필기·실기까지** 한 프로젝트에서 끝내는 학습 코스입니다.

---

## 🆕 처음 시작 (아무것도 모르는 분)

**0단계: 준비** → **1단계: 실행** 순서로 진행하세요.

### 0단계: Python 설치 & 가상환경 (처음 한 번만)

1. **Python 설치**
   - [Python 공식](https://www.python.org/downloads/) 또는 [01_가이드문서/01_python_setup.md](01_가이드문서/01_python_setup.md) 참고
   - 터미널에서 `python3 --version` 입력 → 버전이 나오면 OK

2. **가상환경 생성** (이 프로젝트 폴더에서)
   ```bash
   cd /Users/ryankim/Python   # 프로젝트 폴더로 이동
   python3 -m venv my_python_env   # 가상환경 생성 (my_python_env 폴더 생김)
   ```

3. **가상환경 활성화**
   ```bash
   source my_python_env/bin/activate   # macOS/Linux
   # Windows: my_python_env\Scripts\activate
   ```
   → 프롬프트 앞에 `(my_python_env)` 표시되면 성공

### 1단계: 첫 실행

```bash
python 03_기초부터_심화/01_변수와출력.py
```

출력이 나오면 성공! → [04_학습일지/시작하기.txt](04_학습일지/시작하기.txt)에서 다음 단계 진행.

**에러가 나면?** → [04_학습일지/자주_나오는_에러.md](04_학습일지/자주_나오는_에러.md)

---

## 🎯 학습 목표

| 단계 | 목표 |
|------|------|
| 1 | Python 기초 (변수, 리스트, 함수) |
| 2 | 데이터 분석 (pandas, 전처리, 가설검정) |
| 3 | 모델링 (회귀·분류, sklearn) |
| 4 | **빅데이터분석기사** 필기·실기 합격 |

---

## 🚀 빠른 시작 (이미 Python·가상환경 있는 분)

```bash
cd /Users/ryankim/Python
source my_python_env/bin/activate   # macOS/Linux
# Windows: my_python_env\Scripts\activate

python 03_기초부터_심화/01_변수와출력.py
```

**자세한 순서**: [04_학습일지/시작하기.txt](04_학습일지/시작하기.txt) 또는 [README_프로젝트구조.md](README_프로젝트구조.md)

---

## 📂 전체 학습 루트

```
03_기초부터_심화 (1→13)     Python 기초 + pandas + sklearn
        ↓
06_빅분기_필기_정리         4과목 핵심정리 (필기 대비)
        ↓
05_빅분기_모의고사_연습     실기 25문제 (1·2·3유형)
```

| 폴더 | 내용 |
|------|------|
| **03_기초부터_심화** | 13개 파일, 따라치기 형식 (입문→빅분기 실기 기초) |
| **05_빅분기_모의고사_연습** | 실기 25문제 + [실기_핵심_문법](05_빅분기_모의고사_연습/실기_핵심_문법.md) |
| **06_빅분기_필기_정리** | 필기 4과목 핵심정리 + [시험직전_치트시트](06_빅분기_필기_정리/시험직전_치트시트.md) |
| **01_가이드문서** | 이론 보충 (문법, 자료구조, 객체지향 등) |
| **02_실습코드** | Python 문법 실습 |
| **04_학습일지** | 시작 가이드, 학습 기록 |

---

## 📦 패키지 설치 (빅분기용)

```bash
source my_python_env/bin/activate

# pip가 "command not found" 나오면 → python -m pip 사용
python -m pip install pandas numpy scipy scikit-learn statsmodels requests

# 또는
pip install -r requirements.txt
# pip 안 되면: python -m pip install -r requirements.txt
```

---

## ⚙️ 자동완성 비활성화 (실기 대비)

이 프로젝트는 **빅분기 실기 시험 환경**에 맞추어 `.vscode/settings.json`에서 **자동완성을 비활성화**해 두었습니다.

| 이유 | 설명 |
|------|------|
| **시험 환경** | 실기는 구름(goorm) IDE에서 진행되며, 자동완성이 거의 없음 |
| **쌩코딩 연습** | 시험장에서 `pd.` 입력 시 메서드 제안이 안 나오므로, 미리 익숙해지기 위함 |
| **효과** | 함수·문법을 직접 기억하고 타이핑하는 습관 형성 |

**다시 켜려면**: `.vscode/settings.json`에서 `editor.quickSuggestions` 등 관련 설정 삭제 또는 `true`로 변경.

---

## 📖 상세 문서

- [04_학습일지/시작하기.txt](04_학습일지/시작하기.txt) — 지금 바로 시작하기
- [04_학습일지/자주_나오는_에러.md](04_학습일지/자주_나오는_에러.md) — 에러 해결
- [01_가이드문서/01_python_setup.md](01_가이드문서/01_python_setup.md) — Python 설치 상세
- [README_프로젝트구조.md](README_프로젝트구조.md) — 전체 구조, 학습 순서
- [04_학습일지/학습_체크리스트.md](04_학습일지/학습_체크리스트.md) — 진행 상황 체크
