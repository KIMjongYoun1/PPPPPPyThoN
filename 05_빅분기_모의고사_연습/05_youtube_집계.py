# ╔══════════════════════════════════════════════════════════════╗
# ║  [1유형-집계] 05. YouTube 인기동영상 Q1~Q10                     ║
# ╚══════════════════════════════════════════════════════════════╝
# ★ submission 없음 → print로 답 출력 / 파일: youtube.csv
#   ※ 지문 판단법: "Q1. ~를 구하시오" 형태로 질문 여러 개 나열 → 1유형
#                  "예측하시오" 없음, submission 제출 없음 → print()로 출력
#                  import: pandas만
#
# [1유형 핵심 5패턴 암기]
#   개수: .value_counts() / groupby().size()
#   합계/평균: groupby()["열"].sum() / .mean()
#   상위N: .sort_values(ascending=False).head(N) / .nlargest(N,"열")
#   날짜: pd.to_datetime → .dt.day_name() / .dt.month / .dt.year
#   필터: df[df["열"] > 값] / df[df["열"].str.contains("문자")]


# ═══ import + 로드
# import pandas as pd
# BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
# df = pd.read_csv(f"{BASE}/youtube/youtube.csv", index_col=0)


# ═══ Q1: 인기동영상 제작횟수 상위 10개 채널명
# channelId로 개수 세기 → 상위10 index → 해당 channelTitle
# answer1 = list(df.loc[df.channelId.isin(df.channelId.value_counts().head(10).index)].channelTitle.unique())
# print("Q1:", answer1)


# ═══ Q2: dislikes > likes 동영상 제작 채널
# 조건 필터 → .unique()로 채널명 목록
# answer2 = list(df.loc[df.likes < df.dislikes].channelTitle.unique())
# print("Q2:", answer2)


# ═══ Q3: 채널명 바꾼 적 있는 채널 수
# 같은 channelId에 channelTitle이 여러 개 → drop_duplicates 후 value_counts
# change  = df[["channelTitle", "channelId"]].drop_duplicates().channelId.value_counts()
# answer3 = len(change[change > 1])
# print("Q3:", answer3)


# ═══ Q4: 일요일 인기영상 중 가장 많은 categoryId
# ⚠️ 날짜 처리 필수: pd.to_datetime → .dt.day_name() == "Sunday"
# df["trending_date2"] = pd.to_datetime(df["trending_date2"])
# answer4 = df.loc[df["trending_date2"].dt.day_name() == "Sunday"].categoryId.value_counts().index[0]
# print("Q4:", answer4)


# ═══ Q5: 요일별 categoryId 개수 표
# groupby([날짜.dt.day_name(), 범주열]).size() → pivot
# group   = df.groupby([df["trending_date2"].dt.day_name(), "categoryId"], as_index=False).size()
# answer5 = group.pivot(index="categoryId", columns="trending_date2")
# print("Q5:", answer5)


# ═══ Q6: viewcount 대비 댓글수 가장 높은 영상
# 새 열(ratio) 만들기 → sort_values → .iloc[0]
# target  = df.loc[df.view_count != 0].copy()
# target["ratio"] = target["comment_count"] / target["view_count"]
# answer6 = target.sort_values(by="ratio", ascending=False).iloc[0].title
# print("Q6:", answer6)


# ═══ Q7: viewcount 대비 댓글수 가장 낮은 영상 (ratio 0 제외)
# ratio   = (df["comment_count"] / df["view_count"]).dropna().sort_values()
# idx     = ratio[ratio != 0].index[0]
# answer7 = df.loc[idx, "title"]
# print("Q7:", answer7)


# ═══ Q8: like 대비 dislike 가장 적은 영상
# target8 = df.loc[(df.likes != 0) & (df.dislikes != 0)]
# num     = (target8["dislikes"] / target8["likes"]).sort_values().index[0]
# answer8 = df.loc[num, "title"]
# print("Q8:", answer8)


# ═══ Q9: 트렌드 영상 가장 많이 제작한 채널명
# channelId 최빈값 → 해당 채널의 channelTitle
# answer9 = df.loc[df.channelId == df.channelId.value_counts().index[0]].channelTitle.unique()[0]
# print("Q9:", answer9)


# ═══ Q10: 20회 이상 인기동영상 수
# value_counts() 후 >= 조건 → .sum()
# answer10 = (df[["title", "channelId"]].value_counts() >= 20).sum()
# print("Q10:", answer10)
