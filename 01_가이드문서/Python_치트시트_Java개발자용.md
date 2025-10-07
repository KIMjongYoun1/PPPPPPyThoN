# 🚀 Python 치트시트 (Java 개발자용)

빠른 참조용 핵심 문법 정리

---

## ⚡ 핵심 비교

| 작업 | Java | Python |
|------|------|--------|
| **변수 선언** | `String name = "김";` | `name = "김"` |
| **리스트** | `new ArrayList<>()` | `[]` |
| **맵** | `new HashMap<>()` | `{}` |
| **출력** | `System.out.println()` | `print()` |
| **for 루프** | `for(int i=0; i<10; i++)` | `for i in range(10):` |

---

## 📦 자료구조

### 리스트 (List)
```python
# 생성
fruits = []
fruits = ["사과", "바나나"]

# 추가
fruits.append("포도")

# 접근
first = fruits[0]
last = fruits[-1]

# 순회
for fruit in fruits:
    print(fruit)
```

### 딕셔너리 (Dict = HashMap)
```python
# 생성
user = {}
user = {"name": "김김김", "age": 20}

# 추가/수정
user["city"] = "서울"

# 조회
name = user["name"]

# 순회 (가장 많이 씀!)
for key, value in user.items():
    print(f"{key}: {value}")
```

---

## 🔄 for 루프

```python
# 리스트 순회
for item in list:
    pass

# 범위
for i in range(10):        # 0~9
    pass

for i in range(1, 11):     # 1~10
    pass

for i in range(0, 10, 2):  # 0,2,4,6,8
    pass

# 인덱스 + 값
for i, item in enumerate(list):
    print(f"{i}: {item}")

# 딕셔너리
for key, value in dict.items():
    pass
```

---

## 💡 자주 쓰는 패턴

### 문자열 포맷팅
```python
name = "김김김"
age = 20

# f-string (추천!)
print(f"이름: {name}, 나이: {age}")

# 계산도 가능
print(f"10년 후: {age + 10}세")
```

### 조건문
```python
if age >= 20:
    print("성인")
elif age >= 13:
    print("청소년")
else:
    print("어린이")
```

### 리스트 관련
```python
numbers = [1, 2, 3, 4, 5]

# 길이
len(numbers)  # 5

# 합계
sum(numbers)  # 15

# 최대/최소
max(numbers)  # 5
min(numbers)  # 1

# 정렬
sorted(numbers)
```

---

## 🎯 중첩 구조

```python
# 리스트 안에 딕셔너리 (API 응답 형태!)
students = [
    {"name": "김김김", "score": 85},
    {"name": "이이이", "score": 92}
]

# 접근
students[0]["name"]  # "김김김"

# 순회
for student in students:
    print(student["name"], student["score"])

# 딕셔너리 안에 리스트
student = {
    "name": "김김김",
    "scores": [85, 90, 95]
}

# 접근
student["scores"][0]  # 85
```

---

## ⚠️ 흔한 실수

### 1. = vs :
```python
# ❌ 변수 선언
age: 20

# ✅ 올바름
age = 20
```

### 2. 따옴표 충돌
```python
# ❌ f-string 안에서
print(f"{user["name"]}")

# ✅ 올바름
print(f"{user['name']}")
```

### 3. 들여쓰기
```python
# ❌ 들여쓰기 필수!
if age > 20:
print("성인")  # 에러!

# ✅ 올바름
if age > 20:
    print("성인")
```

### 4. 딕셔너리 키 없음
```python
# ❌ 키가 없으면 에러
age = user["age"]  # KeyError!

# ✅ 안전하게
age = user.get("age", 0)  # 없으면 0
```

---

## 🔧 가상환경

```bash
# 활성화 (매번!)
source my_python_env/bin/activate

# 확인
which python3

# 패키지 설치
pip install 패키지명

# 목록 확인
pip list
```

---

## 🚀 실행

```bash
# 파일 전체 실행
python3 파일명.py

# 한 줄 실행
python3 -c "print('Hello')"

# 인터랙티브 모드
python3
>>> print("test")
>>> exit()
```

---

## 💻 Cursor 단축키

```
저장:        Cmd + S
터미널:      Ctrl + `
부분 실행:   Shift + Enter
파일 찾기:   Cmd + P
```

---

## 🎯 핵심 개념

### Python dict = Java HashMap
```
데이터 형태: 동일 (키:값)
작성 문법: 다름

Python: {"name": "김김김"}
Java:   map.put("name", "김김김")
```

### 가상환경 = JDK + Maven 저장소
```
프로젝트별로 완전 격리
Python 버전 + 라이브러리
```

### for 루프
```
Python: 무엇을 순회하는지
Java:   어떻게 순회하는지
```

---

## 📚 자주 쓰는 메서드

### 리스트
```python
list.append(x)      # 추가
list.remove(x)      # 제거
list.pop()          # 마지막 제거
list.sort()         # 정렬
list.reverse()      # 뒤집기
len(list)           # 길이
```

### 딕셔너리
```python
dict.keys()         # 키 목록
dict.values()       # 값 목록
dict.items()        # 키-값 쌍
dict.get(key, 기본값) # 안전 조회
key in dict         # 키 존재 확인
```

### 문자열
```python
str.upper()         # 대문자
str.lower()         # 소문자
str.strip()         # 공백 제거
str.split()         # 분리
str.replace(a, b)   # 치환
```

---

## 🎓 학습 순서

1. ✅ 환경 설정 (가상환경)
2. ✅ 기본 문법 (변수, 타입)
3. ✅ 자료구조 (리스트, 딕셔너리)
4. ✅ 제어문 (for, if)
5. ⏭️ 함수
6. ⏭️ 클래스
7. ⏭️ 모듈
8. ⏭️ 실전 프로젝트

---

**빠른 참조용이므로 출력해서 옆에 두고 보세요!** 📄

