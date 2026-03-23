# ============================================================
# 05. YouTube 인기동영상 (집계·전처리)
# [유형] 빅분기 실기 1유형 — 표 다루기·집계 (연습: Datamanim youtube)
# ============================================================
#
# ┌─ [문제 목표] ─────────────────────────────────────────────
# │  **하나의 큰 표(df)** 를 주고, 질문(Q1~Q10)마다 **필터·집계·정렬**로 답을 낸다.
# │  모델 학습·submission 파일이 아니라 **요구된 형태로 값/표를 출력**하는 유형.
# └──────────────────────────────────────────────────────────
#
# ┌─ [제공 데이터] ───────────────────────────────────────────
# │  경로: BASE/youtube/youtube.csv (단일 파일)
# │  내용: 인기 동영상 메타데이터 (채널, 조회수, 좋아요/싫어요, 날짜 등 — 중복 행 포함 가능)
# └──────────────────────────────────────────────────────────
#
# ┌─ [수행 요구사항] ─────────────────────────────────────────
# │  · Q1~Q10 각각: `groupby`, `value_counts`, `sort_values`, 날짜 처리 등으로 풀이.
# │  · Q1: 인기동영상 **제작 횟수 상위 10개 채널명**
# │  · Q2: **dislikes > likes** 인 동영상을 만든 **채널** 전부
# │  · Q3: **채널명을 바꾼 적 있는** 채널 **개수**
# │  · Q4: **일요일** 인기영상 중 가장 많은 **categoryId**
# │  · Q5: **요일별** **categoryId** 개수 표
# │  · Q6~Q7: 조회수 대비 댓글 비율 **최고/최저** **영상(행)**
# │  · Q8: like 대비 dislike **가장 적은** 영상(행)
# │  · Q9: 트렌드 영상 **가장 많이 낸 채널명**
# │  · Q10: **20회 이상** 인기 목록에 든 **동영상** 수
# └──────────────────────────────────────────────────────────
#
# ┌─ [산출물 / 정답 형식] ───────────────────────────────────
# │  · 문제마다 **숫자 한 개 / Series / DataFrame / 행 한 줄** 등 지시에 맞게 **출력**.
# └──────────────────────────────────────────────────────────
#
# ┌─ [평가·연습 시 참고] ─────────────────────────────────────
# │  · 실기 1유형은 **집계·필터·정렬** 패턴이 반복됨 (`groupby`, `value_counts`, `sort_values`).
# │  · 비율 계산 시 **0으로 나누기** 없도록 조회수·좋아요 0 행 처리 주의.
# │  · 실제 열 이름은 `df.columns`, `df.head()` 로 확인 (예: trending_date, view_count 등).
# └──────────────────────────────────────────────────────────
#
# [학습 방법] import·BASE만 참고하고, **데이터 로드(Step 3)** 직접 작성 후 Q1~Q10.
# ============================================================
#
# [기본 제공] Step 1~2 | [작성] Step 3~4
# ============================================================

# ---------- [기본 제공] Step 1: import ----------
import pandas as pd

# ---------- [기본 제공] Step 2: BASE URL ----------
BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

# ---------- [작성] Step 3: 데이터 로드 ----------
# 첫 열이 Unnamed 인덱스면 index_col=0 (정답 예시와 동일)
df = pd.read_csv(f"{BASE}/youtube/youtube.csv", index_col=0)
# 디버그: print(df.head()); print(df.columns)
# ---------- [작성] Step 4: Q1~Q10 각각 작성 (요구사항 전부 이 파일 상단 블록과 동일) ----------
#
# Q1: 인기동영상 **제작 횟수** 기준 **상위 10개 채널명** (DataFrame/Series 등 문제 형식에 맞게 출력)
# Q2: **dislikes > likes** 인 동영상을 **제작한 채널** → 해당 채널들 **전부** 출력
# Q3: **채널명(channelTitle)을 한 번이라도 바꾼** 채널(channelId 기준) **개수** → 숫자
# Q4: **일요일**에 인기 영상이었던 것 중 **가장 많이 등장한 categoryId** → 값 하나
# Q5: **요일별**로 **categoryId**가 각각 몇 번씩 나왔는지 → 표(DataFrame 형태)
# Q6: **view_count 대비 댓글수(comment_count)** 비율이 **가장 높은** 영상 → **행 한 줄**(또는 해당 영상 정보)
# Q7: Q6과 동일 비율 정의에서 **가장 낮은** 영상 → **행 한 줄** (view_count=0 등은 제외 문제 있으면 필터)
# Q8: **like 대비 dislike** 비율이 **가장 적은**(싫어요 비중이 가장 작은) 영상 → **행 한 줄**
# Q9: **트렌드(인기) 영상을 가장 많이 제작한** **채널명(channelTitle)** → 값 하나
# Q10: **동일 (title, channelId) 조합**이 인기 목록에 **20회 이상** 등장한 **서로 다른 동영상**이 몇 개인지 → 숫자
#
# TODO: Q1 — 인기 목록 **행 수** 기준 상위 10 채널: channelId 로 세고 → 해당 채널들의 channelTitle (정답 방식)
top10_ids = df.channelId.value_counts().head(10).index
q1_titles = list(df.loc[df.channelId.isin(top10_ids)].channelTitle.unique())
print("================================================")
print("Q1:", q1_titles)
# TODO: Q2 — df[df["dislikes"] > df["likes"]] 후 채널 열 추출·중복 처리
dislike_many = df[df["dislikes"] > df["likes"]]["channelTitle"].unique()
for i in dislike_many:
    print(i)
print("================================================")
print(dislike_many)
# TODO: Q3 — channelId별 channelTitle unique 개수가 2 이상인 channelId 개수
count_title = df[["channelTitle", "channelId"]].drop_duplicates().channelId.value_counts()
print(len(count_title[count_title > 1]))
print("================================================")
print((count_title > 1).sum())
# TODO: Q4 — 날짜 열 to_datetime → 요일이 일요일인 행만 → categoryId value_counts → 최빈값
# 원본 열 이름: trending_date2 (오타 주의: tranding X). .dt 는 df["열"] Series 에 붙인다.
df["trending_date2"] = pd.to_datetime(df["trending_date2"])
Sunday_count = df[df["trending_date2"].dt.day_name() == "Sunday"]["categoryId"].value_counts()
print("================================================")
print(Sunday_count.idxmax())  # 최빈 categoryId: Sunday_count.idxmax()
# TODO: Q5 — 요일 × categoryId 개수 표 (정답과 동일: pivot. unstack만 쓰면 행·열이 뒤바뀜)
group = df.groupby([df["trending_date2"].dt.day_name(), "categoryId"], as_index=False).size()
q5_table = group.pivot(index="categoryId", columns="trending_date2")
print("================================================")
print("Q5:")
print(q5_table)
# TODO: Q6 — ratio = comment_count / view_count (view_count=0 제외) → 비율 **최대인 영상 행**
target_view = df.loc[df["view_count"] != 0].copy()
target_view["ratio_cc"] = target_view["comment_count"] / target_view["view_count"]
print("================================================")
print("Q6 (비율 최대 행):")
print(target_view.sort_values(by="ratio_cc", ascending=False).iloc[0])
# TODO: Q7 — 동일 비율에서 **최소** (정답: ratio==0 인 행은 제외 후 최소)
ratio_nonzero = target_view.loc[target_view["ratio_cc"] != 0]
print("================================================")
print("Q7 (비율 최소 행, ratio!=0):")
print(ratio_nonzero.loc[ratio_nonzero["ratio_cc"].idxmin()])
# TODO: Q8 — dislike/likes 최소 (likes·dislikes 둘 다 0 제외) → **행**
# 잘못된 예: df[mask]["dislikes"] != 0 / df[...]  → 괄호·우선순위 깨져 bool Series 됨
target_like = df.loc[(df["likes"] != 0) & (df["dislikes"] != 0)].copy()
target_like["ratio_dl"] = target_like["dislikes"] / target_like["likes"]
print("================================================")
print("Q8 (dislike/like 최소 행):")
print(target_like.loc[target_like["ratio_dl"].idxmin()])
# TODO: Q9 — 트렌드 행이 가장 많은 **채널명** (.iloc[0]을 size에 쓰면 **개수**만 나옴)
print("================================================")
top_cid = df["channelId"].value_counts().index[0]
q9_name = df.loc[df["channelId"] == top_cid, "channelTitle"].unique()[0]
print("Q9:", q9_name)
# TODO: Q10 — (title, channelId) 쌍이 20회 이상인 **서로 다른 동영상** 개수
print("================================================")
q10 = (df[["title", "channelId"]].value_counts() >= 20).sum()
print("Q10:", q10)
