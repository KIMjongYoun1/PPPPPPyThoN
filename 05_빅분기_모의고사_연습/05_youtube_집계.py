# ============================================================
# 05. YouTube 인기동영상 (집계·전처리)
# [유형] 1유형 (30점) — 데이터 수집·가공
# ============================================================
#
# ---------- [시험 환경] 요구사항 ----------
# 데이터: YouTube 인기동영상 (날짜기준, 중복포함)
# 제공: youtube.csv (BASE/youtube/) — 단일 CSV
# 요구: Q1~Q10 각각 집계·전처리 후 출력
#
# ---------- [추출해야 할 내용 / 정답 형식] ----------
# Q1: 인기동영상 제작횟수 상위 10개 채널명 → DataFrame/Series
# Q2: dislikes > likes 동영상 제작한 채널 → 모두 출력
# Q3: 채널명을 한번이라도 바꾼 채널 갯수 → 숫자
# Q4: 일요일 인기영상 중 가장 많은 categoryId → 값
# Q5: 요일별 categoryId 개수 → DataFrame
# Q6: viewcount대비 댓글수 가장 높은 영상 → 행
# Q7: viewcount대비 댓글수 가장 낮은 영상 → 행
# Q8: like 대비 dislike 가장 적은 영상 → 행
# Q9: 트렌드 영상 가장 많이 제작한 채널명 → 값
# Q10: 20회 이상 인기동영상 포함된 동영상 숫자 → 숫자
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
df = pd.read_csv(f"{BASE}/youtube/youtube.csv")

# ---------- [작성] Step 4: Q1~Q10 각각 작성 ----------
# TODO: Q1 — df.groupby("channelTitle") 또는 value_counts() 활용
# TODO: Q2 — dislikes > likes 필터 후 채널
# TODO: Q3 — channelId별 channelTitle 중복 제거 후 채널명 변경 여부
# TODO: Q4~Q10 — typeone.html 요구사항 참고
