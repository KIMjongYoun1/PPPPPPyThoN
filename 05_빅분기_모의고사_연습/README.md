# 빅데이터분석기사 실기 모의고사·기출 연습

**03_기초부터_심화** 따라치기 후, **실제 데이터**로 연습하는 폴더입니다.

📌 **전체 학습 루트**: `03_기초부터_심화` → `06_빅분기_필기_정리` → `05_빅분기_모의고사_연습` (여기)

**출처**: 모든 데이터는 DataManim (https://github.com/Datamanim/datarepo) 에서 제공하며, 무료 사용 가능. (라이선스 미명시)

---

## 📌 시험형식 구조 (모든 문제 공통)

각 파일은 **시험 환경**과 동일한 구조로 세팅되어 있습니다.

| 구역 | 내용 |
|------|------|
| **[시험 환경] 요구사항** | 데이터 설명, 제공 파일, 평가 방식 (시험에서 주어지는 것) |
| **[추출해야 할 내용 / 정답 형식]** | 정확히 어떤 값·형식으로 출력/제출해야 하는지 |
| **[기본 제공] Step 1~2** | import, BASE URL (연습용 GitHub 경로 — 실기는 문제지 경로 따름) |
| **[작성] Step 3~** | **데이터 로드(`read_csv`)** 포함 이후 전처리·모델·제출 (직접 작성) |

---

## 📌 학습 단계 (점진적 난이도)

1. **1단계**: Step 힌트(TODO) 보면서 작성 → 환경 익숙해지기
2. **2단계**: Step 주석만 보고 흐름 파악 후 작성
3. **3단계**: **[기본 제공] + [요구사항]만** 남기고 나머지 주석 지우고 연습 → 시험과 동일 환경

→ 나중에는 `기본 세팅 + 요구사항`만 보고 풀 수 있을 때까지 반복 연습

---

**📌 [실기_핵심_문법.md](실기_핵심_문법.md)** — 평소 암기 + 시험장에서 바로 타이핑 (groupby, LabelEncoder, logit, ols, ttest_ind 등)

---

## ⚙️ 자동완성 비활성화 (시험 환경 맞추기)

이 프로젝트 루트의 `.vscode/settings.json`에서 **자동완성이 비활성화**되어 있습니다.

| 이유 | 설명 |
|------|------|
| **시험 환경** | 빅분기 실기는 구름(goorm) IDE에서 진행, 자동완성이 거의 없음 |
| **쌩코딩** | `pd.` 입력 시 메서드 제안이 안 나오므로, 미리 손에 익혀야 함 |
| **효과** | `pd.read_csv`, `groupby`, `LabelEncoder` 등 직접 타이핑 연습 |

**복원**: `.vscode/settings.json`에서 `editor.quickSuggestions` 등 삭제 또는 `true`로 변경.

---

## 📂 정답·해설 (`정답_해설/`)

| 파일 | 내용 |
|------|------|
| `01_정답.py` / `01_해설.md` | 실행 가능한 정답 코드 + 풀이 흐름·핵심 포인트 |
| ... | 01~25 각 문제별 정답·해설 |

풀고 나서 `정답_해설/` 에서 확인.

---

## 📂 연습 문제 목록 (25문제)

### 시험 유형별 정리

| 유형 | 배점 | 파일 |
|------|------|------|
| **1유형** | 30점 | 05, 16, 17, 18, 19, 22 |
| **2유형** | 40점 | 01, 02, 03, 04, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 20, 21 |
| **3유형** | 30점 | 23, 24, 25 |

---

### 1유형 (30점) — 데이터 수집·가공
| 번호 | 파일 | 데이터셋 | 비고 |
|------|------|----------|------|
| 05 | 05_youtube_집계.py | youtube | 단일 CSV |
| 16 | 16_nba_농구.py | nba | groupby·집계 |
| 17 | 17_spotify_음악.py | spotify | groupby·집계 |
| 18 | 18_weather_날씨.py | weather | 시계열·집계 |
| 19 | 19_worldcup_월드컵.py | worldcup | groupby·집계 |
| 22 | 22_happy_행복지수.py | happy | 회귀/집계 |

### 2유형 (40점) — 모델링(분류/회귀)
| 번호 | 파일 | 데이터셋 | 유형 | 비고 |
|------|------|----------|------|------|
| 01 | 01_데이터_로드_연습.py | admission | 회귀 | 대학원 합격률 |
| 02 | 02_churn_이탈예측.py | churn | 분류 | train/test |
| 03 | 03_MedicalCost_의료비.py | MedicalCost | 회귀 | train/test |
| 04 | 04_HRdata_인사.py | HRdata | 분류 | X_train/y_train |
| 06 | 06_bank_은행마케팅.py | bank | 분류 | train/test |
| 07 | 07_diabetes_당뇨병.py | diabetes | 분류 | x_train/y_train |
| 08 | 08_heart_심장병.py | heart | 분류 | x_train/y_train |
| 09 | 09_cancer_유방암.py | cancer | 분류 | x_train/y_train |
| 10 | 10_stroke_뇌졸중.py | stroke_ | 분류 | train/test |
| 11 | 11_titanic_타이타닉.py | titanic | 분류 | train만 → split |
| 12 | 12_audit_감사위험.py | audit | 분류 | x_train/y_train |
| 13 | 13_redwine_와인품질.py | redwine | 회귀 | x_train/y_train |
| 14 | 14_kingcountyprice_주택가격.py | kingcountyprice | 회귀 | x_train/y_train |
| 15 | 15_carsprice_자동차가격.py | carsprice | 회귀 | X_train/y_train |
| 20 | 20_shipping_배송.py | shipping | 분류 | X_train/y_train |
| 21 | 21_drug_약물분류.py | drug | 분류 | 다중분류 |

### 3유형 (30점) — 가설검정·통계
| 번호 | 파일 | 내용 | 비고 |
|------|------|------|------|
| 23 | 23_가설검정_F검정_t검정.py | F검정, 합동분산, t검정 | krdatacertificate/s1.csv |
| 24 | 24_로지스틱회귀_이직예측.py | 로지스틱 회귀, 오즈비, 회귀계수 | statsmodels logit |
| 25 | 25_다중선형회귀_주택가격.py | 다중선형회귀, R², 회귀계수 합 | statsmodels ols |

---

## 📋 요구사항·정답 확인 방법

| 유형 | 링크 | 내용 |
|------|------|------|
| **작업 1유형** | [typeone.html](https://www.datamanim.com/dataset/03_dataq/typeone.html) | DataManim 원본 문항·정답 예시 (참고용) |
| **작업 2유형** | [typetwo.html](https://www.datamanim.com/dataset/03_dataq/typetwo.html) | 분류/회귀 **제출 형식** (예: CustomerId, Exited), y_test로 평가 |
| **작업 3유형** | [typethree.html](https://www.datamanim.com/dataset/03_dataq/typethree.html) | F검정, t검정, 로지스틱/다중선형회귀 (statsmodels) |

- **작업 1 (이 폴더 연습 스크립트)**: `05_youtube_집계.py`, `16_nba_농구.py`, `17_spotify_음악.py`, `18_weather_날씨.py`, `22_happy_행복지수.py` 등 **파일 상단 [수행 요구사항] + Step 4**에 **Q1~Qn·TODO**를 **스크립트 안에** 적어 두었음. 외부 페이지 없이 해당 `.py`만 열고 풀이하면 됨.
- **작업 2**: 제출용 CSV 컬럼(예: `CustomerId`, `Exited`), 평가 지표(accuracy, F1, AUC 등) 명시
- **y_test**: `{데이터셋}/y_test.csv` 또는 `test_label.csv`로 예측 정확도 확인 가능

→ **작업 1**은 우선 각 연습 `.py` 상단 요구사항을 따르고, 더 풀고 싶으면 DataManim typeone에서 추가 문항을 참고.

---

## 📌 무료 자료 링크 (합격률 ↑용)

### 1. DataManim (실기 연습 필수)
- **사이트**: https://www.datamanim.com/dataset/03_dataq/index_big_python.html
- **작업 1·2·3유형** + 데이터 전처리 100제
- **GitHub**: https://github.com/Datamanim/datarepo

### 2. 기출·모의고사 (2025·2026 대비)
- **10회 실기 (2025.06)**: https://lab.statisticsplaybook.com/bae-exam-10/ — 작업형 1·2·3, 데이터 GitHub 제공
- **9회 실기 복원**: jesimsim.tistory.com — 답안·풀이코드
- **2026 실기 교재**: lab.statisticsplaybook.com — 기출복원 10회, 합격모의고사

### 3. 필기
- **영진 CBT**: https://license.youngjin.com/ → 빅데이터분석기사필기
- **프로젝트 내 정리**: `../06_빅분기_필기_정리/` — 4과목 핵심정리 (필기+실기 참고)
- **기출 PDF**: nursecoder.tistory.com (4·8·10회)

---

## 🔗 DataManim 데이터셋 URL (Base: .../Datamanim/datarepo/main/)

| 데이터셋 | 형식 | 비고 |
|----------|------|------|
| admission | train.csv, test.csv | 대학원 합격률 |
| churn | train.csv, test.csv | 이탈 예측 |
| MedicalCost | train.csv, test.csv | 의료비 회귀 |
| HRdata | X_train, X_test, y_train, y_test | 인사 |
| bank | train.csv, test.csv | 은행 마케팅 |
| diabetes | x_train, x_test, y_train, y_test | 당뇨병 |
| heart | x_train, x_test, y_train, y_test | 심장병 |
| cancer | x_train, x_test, y_train, y_test | 유방암 |
| stroke_ | train.csv, test.csv | 뇌졸중 |
| titanic | train.csv | 생존 예측 |
| audit | x_train, x_test, y_train, y_test | 감사 위험 |
| redwine | x_train, x_test, y_train, y_test | 와인 품질 |
| kingcountyprice | x_train, x_test, y_train, y_test | 주택 가격 |
| carsprice | X_train, X_test, y_train, y_test | 자동차 가격 |
| shipping | X_train, X_test, y_train, y_test | 배송 지연 |
| drug | x_train, x_test, y_train, y_test | 약물 다중분류 |
| youtube | youtube.csv | 단일 CSV |
| nba | nba.csv | 단일 CSV |
| spotify | spotify.csv | 단일 CSV |
| weather | weather2.csv | 단일 CSV |
| worldcup | worldcupgoals.csv | 단일 CSV |
| happy | happiness.csv | 단일 CSV |

---

## 📂 사용법

1. `01_데이터_로드_연습.py` ~ `25_다중선형회귀_주택가격.py` — 시험형식으로 세팅됨
2. **[시험 환경] 요구사항** + **[추출해야 할 내용]** 확인 → Step 4~7 작성
3. 막히면: TODO 힌트 참고, `_정답` 파일 또는 DataManim 정답 참고

### 3유형 필수 패키지
```bash
pip install scipy statsmodels pandas numpy
```
※ 24, 25번은 `statsmodels` 필요. 미설치 시 `ModuleNotFoundError` 발생.
