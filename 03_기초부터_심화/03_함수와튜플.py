# ============================================================
# 03. 함수와 튜플 (기초)
# ============================================================
#
# [교수님 말]
# 함수는 "이름 붙인 처리 묶음"이야. def 이름(매개변수): 로 정의하고,
# return 으로 결과를 돌려준다. 튜플은 괄호 () 로 만드는 "순서 있는 묶음"인데,
# 리스트와 달리 한 번 만들면 수정할 수 없어. 함수가 여러 값을 한 번에 반환할 때
# 튜플로 (a, b) return 하면 편해.
#
# [import]
# 이 파일은 별도 import 없이 파이썬 내장 함수만 사용 (print, min, max 등).
# ============================================================

# ---------- 따라 칠 코드 (1): 함수 정의와 호출 ----------
def greet(name):
    return f"안녕, {name}!"

msg = greet("영희")
print(msg)

def greet2(name):
    return f"안녕하세요?, {name}!"

msg = greet2("철수")
print(msg)

# ---------- 따라 칠 코드 (2): 매개변수 여러 개, return 하나 ----------
def add(a, b):
    return a + b

print(add(10, 20))

def add2(a, b):
    return a + b

print(add2(11,22))

# ---------- 따라 칠 코드 (3): 여러 값 반환 (튜플) ----------
def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max([3, 7, 2, 9, 1])
print(result)   # (1, 9)
low, high = min_max([3, 7, 2, 9, 1])
print(f"최소: {low}, 최대: {high}")

def min_max2(numbers):
    return min(numbers), max(numbers)

result = min_max([1,2,3,4,5,6,6,7,8,9,10])
print(result)
low, high = min_max2([1,2,3,4,5,6,6,7,8,9,10])
print(f"최소: {low}, 최대 : {high}")

# ---------- 따라 칠 코드 (4): 튜플 만들기 ----------
point = (10, 20)
print(point[0], point[1])

point = (10, 20)
print([point[0], point[1]])
# ---------- 예제 ----------
# 리스트를 받아서 "평균"을 반환하는 함수 average() 를 만들고 호출해 보세요.

def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

print(average([10, 20, 30]))
print(average([1, 2, 3, 4, 5]))

def average2(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

print(average2([10,20,30,40]))
print (average([1,2,3,4,5]))