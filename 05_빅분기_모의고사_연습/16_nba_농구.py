# ============================================================
# 16. NBA 농구 (집계·전처리)
# [유형] 1유형 (30점) — 데이터 수집·가공
# ============================================================
#
# ---------- [시험 환경] 요구사항 ----------
# 데이터: NBA 선수 통계 (Rk, Player, Pos, Age, Tm, G, PTS 등)
# 제공: nba.csv (BASE/nba/) — sep=";", encoding="latin-1"
# 요구: typeone.html NBA 관련 Q — groupby, 집계, 정렬 등
#
# ---------- [추출해야 할 내용 / 정답 형식] ----------
# 각 Q별로 요구하는 DataFrame/Series/값 출력
# (typeone.html에서 NBA Q 확인)
# 예: 팀별 평균 득점, 포지션별 선수 수, 상위 N명 등
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

# ---------- [기본 제공] Step 3: 데이터 로드 ----------
df = pd.read_csv(f"{BASE}/nba/nba.csv", encoding="latin-1", sep=";")

# ---------- [작성] Step 4: typeone.html NBA Q 작성 ----------
# TODO: groupby, agg, sort_values, value_counts 등 활용
# TODO: 각 Q별 출력 형식 확인 후 작성
