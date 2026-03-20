# ============================================================
# 01. Admission 대학원 합격률 — 데이터 로드 연습
# [유형] 2유형 (40점) — 모델링(회귀) / 로드 연습
# ============================================================
#
# ---------- [시험 환경] ----------
# 데이터: 대학원 합격률(Chance of Admit) 회귀 예측
# 제공: train.csv, test.csv (BASE/admission/ 경로)
# 평가(본 문제): RMSE 등 — 회귀 예측값 제출
#
# ---------- [요구사항] (이 파일에서 할 일) ----------
# Q1. train.csv를 로드하고 shape와 head를 출력한다. (아래 Step 3 — 기본 제공)
# Q2. test.csv를 로드하고 shape를 출력한다. (아래 Step 4 — 작성)
# ※ 이후 단계(별도 연습): 전처리 → 회귀 모델 → submission (ID, Chance of Admit)
#
# ---------- [데이터 컬럼 참고] ----------
# train: GRE Score, TOEFL Score, University Rating, SOP, LOR, CGPA, Research,
#        Chance of Admit(종속), ID 또는 Serial No. 등 (DataManim 원본 확인)
# test: 동일 특성 + Chance of Admit 없음(예측 대상)
#
# ---------- [추출해야 할 내용 / 정답 형식] ----------
# (이번 파일) train shape, test shape 출력
# (본 시험형 문제) submission.csv — ID, Chance of Admit (연속형 예측값)
#
# ---------- [학습 목표] ----------
# 나중에 주석 지우고 [기본 제공] + [요구사항]만 보고 연습
# ============================================================
#
# [기본 제공] Step 1~3 | [작성] Step 4
# ============================================================

# ---------- [기본 제공] Step 1: import ----------
import pandas as pd

# ---------- [기본 제공] Step 2: BASE URL ----------
BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

# ---------- [기본 제공] Step 3: train 로드 ----------
train = pd.read_csv(f"{BASE}/admission/train.csv")
print("train shape:", train.shape)
print(train.head())

# ---------- [작성] Step 4: test 로드 ----------
# TODO: test = pd.read_csv(f"{BASE}/admission/test.csv")
# TODO: print("test shape:", test.shape)

test = pd.read_csv(f"{BASE}/admission/test.csv")
print("test shape:", test.shape)
print(test.head())