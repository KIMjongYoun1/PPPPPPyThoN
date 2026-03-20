# ============================================================
# 22. Happy 행복 지수 (정답) — typeone.html Happy Q 참고
# ============================================================

import pandas as pd

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"
df = pd.read_csv(f"{BASE}/happy/happiness.csv")

# 예시: 국가별 행복지수 상위 5
if "Country" in df.columns and "Happiness Score" in df.columns:
    answer = df.nlargest(5, "Happiness Score")[["Country", "Happiness Score"]]
    print(answer)

# typeone.html Happy Q에서 회귀/집계 요구사항 확인
