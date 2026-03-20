# ============================================================
# 17. Spotify 음악 (집계·전처리)
# [유형] 1유형 (30점) — 데이터 수집·가공
# ============================================================
#
# ---------- [시험 환경] 요구사항 ----------
# 데이터: 스포티파이 음악 데이터
# 제공: spotify.csv (BASE/spotify/)
# 요구: typeone.html Spotify Q — groupby, 집계, 정렬 등
#
# ---------- [추출해야 할 내용 / 정답 형식] ----------
# 각 Q별로 요구하는 DataFrame/Series/값 출력
# (typeone.html에서 Spotify Q 확인)
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
df = pd.read_csv(f"{BASE}/spotify/spotify.csv")

# ---------- [작성] Step 4: typeone.html Spotify Q 작성 ----------
# TODO: groupby, agg, sort_values 등 활용
