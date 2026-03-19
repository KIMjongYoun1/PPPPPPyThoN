# ============================================================
# 02. 리스트와 반복 (기초)
# ============================================================
#
# [교수님 말]
# 리스트는 "순서 있는 값들의 묶음"이야. 대괄호 [] 로 만들고, 쉼표로 구분해.
# 인덱스는 0부터 시작한다고 기억해. for 문으로 하나씩 꺼내서 반복할 수 있어.
# append()로 맨 뒤에 추가하고, len()으로 개수를 알 수 있어.
# 슬라이스 [시작:끝] 은 "시작 인덱스는 포함, 끝 인덱스는 미포함"이야.
#
# [import]
# 이 파일은 별도 import 없이 파이썬 내장 함수만 사용 (print, len, range 등).
# ============================================================

# ---------- 따라 칠 코드 (1): 리스트 만들고 인덱스 ----------
scores = [80, 90, 70, 85, 95]
print(scores[0])   # 첫 번째 → 80
print(scores[-1])  # 맨 뒤 → 95

scores = [80, 90, 70, 77, 87, 96]
print(scores[0])
print(scores[-2])


# ---------- 따라 칠 코드 (2): for 로 하나씩 출력 ----------
for s in scores:
    print(s)

for s in scores:
    print(s)

# ---------- 따라 칠 코드 (3): append, len ----------
nums = [1, 2, 3]
nums.append(4)
nums.append(5)
print(nums)
print(len(nums))

nums = [ 1, 2, 3]
nums.append(4)
nums.append(5)
print(nums)
print(len(nums))


# ---------- 따라 칠 코드 (4): 슬라이스 ----------
# [시작:끝] → 시작은 포함, 끝은 미포함
data = [10, 20, 30, 40, 50]
print(data[1:4])   # 20, 30, 40
print(data[:3])    # 처음부터 3개 → 10, 20, 30
print(data[2:])    # 2번부터 끝까지 → 30, 40, 50

data = [10, 20, 30, 40, 50]
print(data[1:4])
print(data[:3])
print(data[2:])
# ---------- 예제 ----------
# 리스트 [3, 7, 2, 9, 1] 에서 (1) 합계를 구하고 (2) for로 하나씩 출력해 보세요.

values = [3, 7, 2, 9, 1]
total = 0
for v in values:
    total = total + v
print(f"합계: {total}")


values = [3, 7, 9 ,11 ,12 ,1]
total = 0
for v in values:
    print(v)
    total = total + v
print(f"합계:{total}")
    
    # 한 줄로 합계: sum(values)
sum(values)