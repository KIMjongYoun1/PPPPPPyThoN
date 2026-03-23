# ============================================================
# 17. Spotify 음악 (집계·전처리)
# [유형] 빅분기 실기 1유형 — 표 다루기·집계 (연습: Datamanim spotify)
# ============================================================
#
# ┌─ [문제 목표] ───────────────────────────────────────────
# │  차트·음원 메타데이터 **한 표**로 질문마다 **집계·정렬·빈도** 등을 구한다.
# └──────────────────────────────────────────────────────────
#
# ┌─ [제공 데이터] ───────────────────────────────────────────
# │  경로: BASE/spotify/spotify.csv
# │  · 열: title, artist, top genre, year released, added, bpm, nrgy, dnce, dB, live, val,
# │    dur, acous, spch, pop, top year, artist type
# │  · 공백·특수문자가 들어간 열 이름은 `df.columns`로 확인 (예: "top genre").
# └──────────────────────────────────────────────────────────
#
# ┌─ [수행 요구사항] ─────────────────────────────────────────
# │  · Q1~Q10: `groupby`, `agg`, `sort_values`, `value_counts`, `nlargest` 등.
# │  · Q1: **artist**별 곡(**title**) 개수 상위 **10**명 아티스트
# │  · Q2: **top genre**별 곡 수 — 많은 순
# │  · Q3: **pop**이 **80 이상**인 곡 **개수**
# │  · Q4: **year released**별 평균 **bpm** (연도 × 평균 bpm)
# │  · Q5: **nrgy**(에너지)가 **가장 큰** 곡의 **title** 하나
# │  · Q6: **artist type**별 곡 수
# │  · Q7: **dnce** 상위 **5**곡의 **title** (정렬 후 head)
# │  · Q8: **top year**가 **2010**인 행에서 **top genre** 빈도 상위 **3**
# │  · Q9: **top genre**별 **dur**(초) **평균**이 **가장 긴** 장르 이름 하나
# │  · Q10: **added**를 `pd.to_datetime`으로 변환한 뒤 **연도**별로 추가된 곡 **개수** (added 열 형식 주의)
# └──────────────────────────────────────────────────────────
#
# ┌─ [산출물 / 정답 형식] ───────────────────────────────────
# │  · 문항별 요구 형식(표/값)으로 **출력**.
# └──────────────────────────────────────────────────────────
#
# ┌─ [평가·연습 시 참고] ─────────────────────────────────────
# │  · `added` 값에 특수 하이픈(유니코드)이 섞일 수 있음 → `errors="coerce"` 후 결측 처리.
# └──────────────────────────────────────────────────────────
#
# [학습 방법] import·BASE만 참고하고, **데이터 로드(Step 3)** 직접 작성 후 Step 4.
# ============================================================
#
# [기본 제공] Step 1~2 | [작성] Step 3~4
# ============================================================

# ---------- [기본 제공] Step 1: import ----------
import pandas as pd

# ---------- [기본 제공] Step 2: BASE URL ----------
BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

# ---------- [작성] Step 3: 데이터 로드 ----------
# TODO: df = pd.read_csv(f"{BASE}/spotify/spotify.csv")

# ---------- [작성] Step 4: Q1~Q10 (상단 [수행 요구사항]과 동일) ----------
#
# TODO: Q1 — df.groupby("artist")["title"].nunique() 또는 size(); sort_values head(10)
# TODO: Q2 — df["top genre"].value_counts()
# TODO: Q3 — (df["pop"] >= 80).sum()
# TODO: Q4 — groupby("year released")["bpm"].mean()
# TODO: Q5 — df.nlargest(1, "nrgy")["title"].iloc[0]
# TODO: Q6 — df.groupby("artist type").size()
# TODO: Q7 — df.nlargest(5, "dnce")["title"]
# TODO: Q8 — df[df["top year"] == 2010]["top genre"].value_counts().head(3)
# TODO: Q9 — groupby("top genre")["dur"].mean().idxmax()
# TODO: Q10 — pd.to_datetime(df["added"], errors="coerce").dt.year.value_counts().sort_index()
