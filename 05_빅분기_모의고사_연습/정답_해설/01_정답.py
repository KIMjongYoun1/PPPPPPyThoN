# ============================================================
# 01. Admission 대학원 합격률 — 데이터 로드 연습 (정답)
# ============================================================

import pandas as pd

BASE = "https://raw.githubusercontent.com/Datamanim/datarepo/main"

# Step 3: train 로드
train = pd.read_csv(f"{BASE}/admission/train.csv")
print("train shape:", train.shape)
print(train.head())

# Step 4: test 로드
test = pd.read_csv(f"{BASE}/admission/test.csv")
print("test shape:", test.shape)
