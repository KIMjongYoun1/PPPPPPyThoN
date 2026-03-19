# ============================================================
# 05. 전처리 — 결측 채우기 (중급)
# ============================================================
#
# [교수님 말]
# 결측(missing)은 "값이 비어 있거나 알 수 없는 경우"야. CSV에서는 빈 문자열 "" 이나
# "NA", "null" 같은 문자열로 올 수 있어. 결측을 그대로 두면 평균 같은 계산이 깨지니까,
# "그 열의 평균으로 채운다" 같은 전처리를 많이 해. 먼저 숫자로 바꿀 수 있는지 보고,
# 못 바꾸면 결측으로 처리한 뒤, 결측이 아닌 값들로 평균을 구해 그걸로 채우면 돼.
#
# [import]
# 이 파일은 별도 import 없이 파이썬 내장 함수만 사용 (print, str, float, try/except 등).
# ============================================================

# ---------- 따라 칠 코드 (1): 결측 판별 (문자열 기준) ----------
# Java 스타일: 결과를 변수에 담고 맨 아래에서 한 번만 return
def is_missing(val):
    result = False
    if val is None:
        result = True
    else:
        s = str(val).strip().upper()
        result = (s in ("", "NA", "NAN", "NULL", "NONE", "."))
    return result

print(is_missing(""))
print(is_missing("NA"))
print(is_missing("80"))
print()  # 구분용

def is_missing2(val):
    if val is None:
        return True
    s = str(val).strip().upper()
    return s in ("", "NA", "NAN","NULL", "NONE", ".", "NO")

print(is_missing2(""))
print(is_missing2("NA"))
print(is_missing2("80"))
print(is_missing2("NO"))
print()

# ---------- 따라 칠 코드 (2): 한 열을 숫자 리스트로 바꾸기 (결측은 None) ----------
def parse_numeric_column(values):
    result = []
    for v in values:
        if is_missing(v):
            result.append(None)
        else:
            try:
                result.append(float(v))
            except ValueError:
                result.append(None)
    return result

col = ["10", "20", "", "30", "NA", "40"]
parsed = parse_numeric_column(col)
print("parsed:", parsed)



def parse_numeric_column2(values):
    result = []
    for v in values:
        if is_missing2(v):
            result.append(None)
        else:
            try:
                result.append(float(v))
            except ValueError:
                result.append(None)
    return result

col2 = ["11","22","33","NO","NA", "NAN"]
parsed2 = parse_numeric_column2(col2)
print(f"parsed2 :  {parsed2}")

# ---------- 따라 칠 코드 (3): 결측 제외 평균, 그 값으로 결측 채우기 ----------
def fill_missing_with_mean(parsed_list):
    valid = [x for x in parsed_list if x is not None]
    if not valid:
        return parsed_list
    mean_val = sum(valid) / len(valid)
    return [mean_val if x is None else x for x in parsed_list]

filled = fill_missing_with_mean(parsed)
print("채운 결과:", filled)

def fill_missing_with_mean2(parsed_list):
    valid = [x for x in parsed_list if x is not None]
    if not valid:
        return parsed_list
    mean_val = sum(valid) / len(valid)
    return [mean_val if x is None else x for x in parsed_list]

filed = fill_missing_with_mean2(parsed2)
print(f"채운결과 : {filed}")

# ---------- 예제 ----------
# 아래 리스트에서 결측을 "그 열의 중앙값"으로 채우는 함수를 만들어 보세요.
# (중앙값: 정렬했을 때 가운데 값. 개수가 짝수면 가운데 두 값의 평균)

def median_of_list(arr):
    valid = sorted([x for x in arr if x is not None])
    n = len(valid)
    print(valid)
    if n == 0:
        return None
    if n % 2 == 1:
        return valid[n // 2]
    return (valid[n // 2 - 1] + valid[n // 2]) / 2
  

def fill_missing_with_median(parsed_list):
    m = median_of_list(parsed_list)
    if m is None:
        return parsed_list
    return [m if x is None else x for x in parsed_list]

test = [1.0, None, 3.0, None, 5.0]
print(fill_missing_with_median(test))
print()

def midian_of_list(arr):
    valid = sorted([x for x in arr if x is not None])
    n = len(valid)
    if n == 0:
        return None
    if n % 2 == 1:
        return valid[n // 2]
    return (valid[n // 2 -1 ] + valid[n //2]) /2

def fill_missing_with_median2(parsed_list):
    m = midian_of_list(parsed_list)
    print(m)
    if m is None:
        return parsed_list
    return [m if x is None else x for x in parsed_list]

testData = [1.0, None, 3.0, None, 5.0]
print(fill_missing_with_median2(testData))
print()

