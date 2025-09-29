# 파이썬 실습 예제 및 프로젝트

## 1. 간단한 계산기 프로그램

### 기본 계산기
```python
# calculator.py
import math

class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("0으로 나눌 수 없습니다.")
        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return result
    
    def power(self, a, b):
        result = a ** b
        self.history.append(f"{a}^{b} = {result}")
        return result
    
    def sqrt(self, a):
        if a < 0:
            raise ValueError("음수의 제곱근을 계산할 수 없습니다.")
        result = math.sqrt(a)
        self.history.append(f"√{a} = {result}")
        return result
    
    def show_history(self):
        if not self.history:
            print("계산 기록이 없습니다.")
            return
        
        print("\n=== 계산 기록 ===")
        for i, calculation in enumerate(self.history, 1):
            print(f"{i}. {calculation}")
    
    def clear_history(self):
        self.history.clear()
        print("계산 기록이 삭제되었습니다.")

def main():
    calc = Calculator()
    
    while True:
        print("\n=== 계산기 ===")
        print("1. 덧셈")
        print("2. 뺄셈")
        print("3. 곱셈")
        print("4. 나눗셈")
        print("5. 거듭제곱")
        print("6. 제곱근")
        print("7. 계산 기록 보기")
        print("8. 기록 삭제")
        print("9. 종료")
        
        try:
            choice = input("\n선택하세요 (1-9): ")
            
            if choice == "9":
                print("계산기를 종료합니다.")
                break
            
            if choice in ["1", "2", "3", "4", "5"]:
                a = float(input("첫 번째 숫자: "))
                b = float(input("두 번째 숫자: "))
                
                if choice == "1":
                    result = calc.add(a, b)
                elif choice == "2":
                    result = calc.subtract(a, b)
                elif choice == "3":
                    result = calc.multiply(a, b)
                elif choice == "4":
                    result = calc.divide(a, b)
                elif choice == "5":
                    result = calc.power(a, b)
                
                print(f"결과: {result}")
            
            elif choice == "6":
                a = float(input("숫자: "))
                result = calc.sqrt(a)
                print(f"결과: {result}")
            
            elif choice == "7":
                calc.show_history()
            
            elif choice == "8":
                calc.clear_history()
            
            else:
                print("잘못된 선택입니다.")
                
        except ValueError as e:
            print(f"오류: {e}")
        except Exception as e:
            print(f"예상치 못한 오류: {e}")

if __name__ == "__main__":
    main()
```

## 2. 학생 성적 관리 시스템

### 성적 관리 클래스
```python
# student_management.py
import json
import os
from datetime import datetime

class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.subjects = {}
        self.created_at = datetime.now().isoformat()
    
    def add_subject_score(self, subject, score):
        if 0 <= score <= 100:
            self.subjects[subject] = score
            return True
        return False
    
    def get_average_score(self):
        if not self.subjects:
            return 0
        return sum(self.subjects.values()) / len(self.subjects)
    
    def get_grade_level(self):
        avg = self.get_average_score()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "grade": self.grade,
            "subjects": self.subjects,
            "created_at": self.created_at
        }
    
    @classmethod
    def from_dict(cls, data):
        student = cls(data["student_id"], data["name"], data["grade"])
        student.subjects = data.get("subjects", {})
        student.created_at = data.get("created_at", datetime.now().isoformat())
        return student

class StudentManager:
    def __init__(self, data_file="students.json"):
        self.data_file = data_file
        self.students = {}
        self.load_data()
    
    def add_student(self, student_id, name, grade):
        if student_id in self.students:
            print(f"학생 ID {student_id}는 이미 존재합니다.")
            return False
        
        student = Student(student_id, name, grade)
        self.students[student_id] = student
        self.save_data()
        print(f"학생 {name}이(가) 추가되었습니다.")
        return True
    
    def remove_student(self, student_id):
        if student_id in self.students:
            student = self.students.pop(student_id)
            self.save_data()
            print(f"학생 {student.name}이(가) 삭제되었습니다.")
            return True
        else:
            print(f"학생 ID {student_id}를 찾을 수 없습니다.")
            return False
    
    def add_score(self, student_id, subject, score):
        if student_id in self.students:
            if self.students[student_id].add_subject_score(subject, score):
                self.save_data()
                print(f"{self.students[student_id].name}의 {subject} 점수가 {score}점으로 설정되었습니다.")
                return True
            else:
                print("점수는 0-100 사이여야 합니다.")
        else:
            print(f"학생 ID {student_id}를 찾을 수 없습니다.")
        return False
    
    def show_student_info(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            print(f"\n=== {student.name} 학생 정보 ===")
            print(f"학생 ID: {student.student_id}")
            print(f"이름: {student.name}")
            print(f"학년: {student.grade}")
            print(f"등록일: {student.created_at}")
            
            if student.subjects:
                print("\n과목별 점수:")
                for subject, score in student.subjects.items():
                    print(f"  {subject}: {score}점")
                print(f"\n평균: {student.get_average_score():.2f}점")
                print(f"등급: {student.get_grade_level()}")
            else:
                print("등록된 과목이 없습니다.")
        else:
            print(f"학생 ID {student_id}를 찾을 수 없습니다.")
    
    def show_all_students(self):
        if not self.students:
            print("등록된 학생이 없습니다.")
            return
        
        print("\n=== 전체 학생 목록 ===")
        for student in self.students.values():
            avg = student.get_average_score()
            grade_level = student.get_grade_level()
            print(f"ID: {student.student_id}, 이름: {student.name}, "
                  f"학년: {student.grade}, 평균: {avg:.2f}, 등급: {grade_level}")
    
    def show_statistics(self):
        if not self.students:
            print("등록된 학생이 없습니다.")
            return
        
        all_scores = []
        grade_distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
        
        for student in self.students.values():
            avg = student.get_average_score()
            all_scores.append(avg)
            grade_level = student.get_grade_level()
            grade_distribution[grade_level] += 1
        
        print("\n=== 성적 통계 ===")
        print(f"총 학생 수: {len(self.students)}")
        print(f"전체 평균: {sum(all_scores) / len(all_scores):.2f}")
        print(f"최고 점수: {max(all_scores):.2f}")
        print(f"최저 점수: {min(all_scores):.2f}")
        
        print("\n등급별 분포:")
        for grade, count in grade_distribution.items():
            percentage = (count / len(self.students)) * 100
            print(f"  {grade}등급: {count}명 ({percentage:.1f}%)")
    
    def save_data(self):
        data = {
            student_id: student.to_dict() 
            for student_id, student in self.students.items()
        }
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self.students = {
                    student_id: Student.from_dict(student_data)
                    for student_id, student_data in data.items()
                }
            except Exception as e:
                print(f"데이터 로드 중 오류 발생: {e}")
                self.students = {}

def main():
    manager = StudentManager()
    
    while True:
        print("\n=== 학생 성적 관리 시스템 ===")
        print("1. 학생 추가")
        print("2. 학생 삭제")
        print("3. 점수 입력")
        print("4. 학생 정보 조회")
        print("5. 전체 학생 목록")
        print("6. 성적 통계")
        print("7. 종료")
        
        choice = input("\n선택하세요 (1-7): ")
        
        if choice == "1":
            student_id = input("학생 ID: ")
            name = input("이름: ")
            try:
                grade = int(input("학년: "))
                manager.add_student(student_id, name, grade)
            except ValueError:
                print("학년은 숫자로 입력하세요.")
        
        elif choice == "2":
            student_id = input("삭제할 학생 ID: ")
            manager.remove_student(student_id)
        
        elif choice == "3":
            student_id = input("학생 ID: ")
            subject = input("과목명: ")
            try:
                score = float(input("점수: "))
                manager.add_score(student_id, subject, score)
            except ValueError:
                print("점수는 숫자로 입력하세요.")
        
        elif choice == "4":
            student_id = input("조회할 학생 ID: ")
            manager.show_student_info(student_id)
        
        elif choice == "5":
            manager.show_all_students()
        
        elif choice == "6":
            manager.show_statistics()
        
        elif choice == "7":
            print("프로그램을 종료합니다.")
            break
        
        else:
            print("잘못된 선택입니다.")

if __name__ == "__main__":
    main()
```

## 3. 간단한 웹 스크래퍼

### 웹 스크래핑 도구
```python
# web_scraper.py
import requests
from bs4 import BeautifulSoup
import json
import csv
from urllib.parse import urljoin, urlparse
import time

class WebScraper:
    def __init__(self, delay=1):
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def get_page(self, url):
        """웹 페이지 가져오기"""
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"페이지 로드 실패: {e}")
            return None
    
    def parse_links(self, html, base_url):
        """페이지에서 링크 추출"""
        soup = BeautifulSoup(html, 'html.parser')
        links = []
        
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(base_url, href)
            text = link.get_text(strip=True)
            if text and full_url.startswith('http'):
                links.append({
                    'url': full_url,
                    'text': text
                })
        
        return links
    
    def scrape_news_headlines(self, url):
        """뉴스 헤드라인 스크래핑"""
        html = self.get_page(url)
        if not html:
            return []
        
        soup = BeautifulSoup(html, 'html.parser')
        headlines = []
        
        # 일반적인 뉴스 헤드라인 선택자들
        selectors = [
            'h1', 'h2', 'h3',
            '.headline', '.title', '.news-title',
            'a[href*="news"]', 'a[href*="article"]'
        ]
        
        for selector in selectors:
            elements = soup.select(selector)
            for element in elements:
                text = element.get_text(strip=True)
                if text and len(text) > 10:  # 너무 짧은 텍스트 제외
                    headlines.append({
                        'text': text,
                        'tag': element.name,
                        'class': element.get('class', [])
                    })
        
        return headlines[:20]  # 상위 20개만 반환
    
    def scrape_product_info(self, url):
        """상품 정보 스크래핑"""
        html = self.get_page(url)
        if not html:
            return {}
        
        soup = BeautifulSoup(html, 'html.parser')
        product_info = {}
        
        # 제품명
        title_selectors = ['h1', '.product-title', '.product-name', 'title']
        for selector in title_selectors:
            element = soup.select_one(selector)
            if element:
                product_info['title'] = element.get_text(strip=True)
                break
        
        # 가격
        price_selectors = ['.price', '.product-price', '[class*="price"]']
        for selector in price_selectors:
            element = soup.select_one(selector)
            if element:
                price_text = element.get_text(strip=True)
                # 숫자만 추출
                import re
                price_match = re.search(r'[\d,]+', price_text)
                if price_match:
                    product_info['price'] = price_match.group()
                break
        
        # 설명
        desc_selectors = ['.description', '.product-description', 'meta[name="description"]']
        for selector in desc_selectors:
            element = soup.select_one(selector)
            if element:
                if element.name == 'meta':
                    product_info['description'] = element.get('content', '')
                else:
                    product_info['description'] = element.get_text(strip=True)
                break
        
        return product_info
    
    def save_to_json(self, data, filename):
        """JSON 파일로 저장"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"데이터가 {filename}에 저장되었습니다.")
    
    def save_to_csv(self, data, filename):
        """CSV 파일로 저장"""
        if not data:
            print("저장할 데이터가 없습니다.")
            return
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"데이터가 {filename}에 저장되었습니다.")

def main():
    scraper = WebScraper()
    
    while True:
        print("\n=== 웹 스크래퍼 ===")
        print("1. 뉴스 헤드라인 스크래핑")
        print("2. 상품 정보 스크래핑")
        print("3. 링크 추출")
        print("4. 종료")
        
        choice = input("\n선택하세요 (1-4): ")
        
        if choice == "1":
            url = input("뉴스 사이트 URL: ")
            print("헤드라인을 스크래핑 중...")
            headlines = scraper.scrape_news_headlines(url)
            
            if headlines:
                print(f"\n=== 발견된 헤드라인 ({len(headlines)}개) ===")
                for i, headline in enumerate(headlines, 1):
                    print(f"{i}. {headline['text']}")
                
                save = input("\n결과를 저장하시겠습니까? (y/n): ")
                if save.lower() == 'y':
                    scraper.save_to_json(headlines, 'headlines.json')
            else:
                print("헤드라인을 찾을 수 없습니다.")
        
        elif choice == "2":
            url = input("상품 페이지 URL: ")
            print("상품 정보를 스크래핑 중...")
            product_info = scraper.scrape_product_info(url)
            
            if product_info:
                print("\n=== 상품 정보 ===")
                for key, value in product_info.items():
                    print(f"{key}: {value}")
                
                save = input("\n결과를 저장하시겠습니까? (y/n): ")
                if save.lower() == 'y':
                    scraper.save_to_json(product_info, 'product_info.json')
            else:
                print("상품 정보를 찾을 수 없습니다.")
        
        elif choice == "3":
            url = input("웹 페이지 URL: ")
            print("링크를 추출 중...")
            html = scraper.get_page(url)
            
            if html:
                links = scraper.parse_links(html, url)
                print(f"\n=== 발견된 링크 ({len(links)}개) ===")
                for i, link in enumerate(links[:10], 1):  # 상위 10개만 표시
                    print(f"{i}. {link['text']} -> {link['url']}")
                
                if len(links) > 10:
                    print(f"... 및 {len(links) - 10}개 더")
                
                save = input("\n결과를 저장하시겠습니까? (y/n): ")
                if save.lower() == 'y':
                    scraper.save_to_csv(links, 'links.csv')
            else:
                print("페이지를 로드할 수 없습니다.")
        
        elif choice == "4":
            print("프로그램을 종료합니다.")
            break
        
        else:
            print("잘못된 선택입니다.")
        
        time.sleep(scraper.delay)  # 요청 간 지연

if __name__ == "__main__":
    main()
```

## 4. 파일 관리 도구

### 파일 관리 시스템
```python
# file_manager.py
import os
import shutil
import hashlib
import json
from datetime import datetime
from pathlib import Path

class FileManager:
    def __init__(self, base_path="."):
        self.base_path = Path(base_path)
        self.history_file = "file_operations.json"
        self.operations_history = self.load_history()
    
    def load_history(self):
        """작업 기록 로드"""
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_history(self):
        """작업 기록 저장"""
        with open(self.history_file, 'w', encoding='utf-8') as f:
            json.dump(self.operations_history, f, ensure_ascii=False, indent=2)
    
    def log_operation(self, operation, source, destination=None, result="success"):
        """작업 기록"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "operation": operation,
            "source": str(source),
            "destination": str(destination) if destination else None,
            "result": result
        }
        self.operations_history.append(log_entry)
        self.save_history()
    
    def list_files(self, path=None, show_hidden=False):
        """파일 목록 표시"""
        target_path = self.base_path / path if path else self.base_path
        
        if not target_path.exists():
            print(f"경로가 존재하지 않습니다: {target_path}")
            return []
        
        files = []
        try:
            for item in target_path.iterdir():
                if not show_hidden and item.name.startswith('.'):
                    continue
                
                file_info = {
                    'name': item.name,
                    'type': 'directory' if item.is_dir() else 'file',
                    'size': item.stat().st_size if item.is_file() else 0,
                    'modified': datetime.fromtimestamp(item.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")
                }
                files.append(file_info)
            
            # 이름순 정렬
            files.sort(key=lambda x: (x['type'], x['name']))
            
            print(f"\n=== {target_path} 내용 ===")
            print(f"{'이름':<30} {'타입':<10} {'크기':<15} {'수정일'}")
            print("-" * 70)
            
            for file_info in files:
                size_str = f"{file_info['size']:,} bytes" if file_info['type'] == 'file' else "폴더"
                print(f"{file_info['name']:<30} {file_info['type']:<10} {size_str:<15} {file_info['modified']}")
            
            return files
            
        except PermissionError:
            print(f"권한이 없습니다: {target_path}")
            return []
    
    def create_file(self, filename, content=""):
        """파일 생성"""
        file_path = self.base_path / filename
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"파일이 생성되었습니다: {file_path}")
            self.log_operation("create_file", file_path)
            return True
        except Exception as e:
            print(f"파일 생성 실패: {e}")
            self.log_operation("create_file", file_path, result=f"failed: {e}")
            return False
    
    def create_directory(self, dirname):
        """디렉토리 생성"""
        dir_path = self.base_path / dirname
        
        try:
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"디렉토리가 생성되었습니다: {dir_path}")
            self.log_operation("create_directory", dir_path)
            return True
        except Exception as e:
            print(f"디렉토리 생성 실패: {e}")
            self.log_operation("create_directory", dir_path, result=f"failed: {e}")
            return False
    
    def copy_file(self, source, destination):
        """파일 복사"""
        source_path = self.base_path / source
        dest_path = self.base_path / destination
        
        try:
            if source_path.is_file():
                shutil.copy2(source_path, dest_path)
                print(f"파일이 복사되었습니다: {source_path} -> {dest_path}")
                self.log_operation("copy_file", source_path, dest_path)
                return True
            else:
                print(f"소스 파일이 존재하지 않습니다: {source_path}")
                return False
        except Exception as e:
            print(f"파일 복사 실패: {e}")
            self.log_operation("copy_file", source_path, dest_path, result=f"failed: {e}")
            return False
    
    def move_file(self, source, destination):
        """파일 이동"""
        source_path = self.base_path / source
        dest_path = self.base_path / destination
        
        try:
            shutil.move(str(source_path), str(dest_path))
            print(f"파일이 이동되었습니다: {source_path} -> {dest_path}")
            self.log_operation("move_file", source_path, dest_path)
            return True
        except Exception as e:
            print(f"파일 이동 실패: {e}")
            self.log_operation("move_file", source_path, dest_path, result=f"failed: {e}")
            return False
    
    def delete_file(self, filename):
        """파일 삭제"""
        file_path = self.base_path / filename
        
        try:
            if file_path.is_file():
                file_path.unlink()
                print(f"파일이 삭제되었습니다: {file_path}")
                self.log_operation("delete_file", file_path)
                return True
            elif file_path.is_dir():
                shutil.rmtree(file_path)
                print(f"디렉토리가 삭제되었습니다: {file_path}")
                self.log_operation("delete_directory", file_path)
                return True
            else:
                print(f"파일이나 디렉토리가 존재하지 않습니다: {file_path}")
                return False
        except Exception as e:
            print(f"삭제 실패: {e}")
            self.log_operation("delete", file_path, result=f"failed: {e}")
            return False
    
    def get_file_hash(self, filename):
        """파일 해시값 계산"""
        file_path = self.base_path / filename
        
        if not file_path.is_file():
            print(f"파일이 존재하지 않습니다: {file_path}")
            return None
        
        try:
            hash_md5 = hashlib.md5()
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()
        except Exception as e:
            print(f"해시 계산 실패: {e}")
            return None
    
    def find_files(self, pattern, file_type="all"):
        """파일 검색"""
        found_files = []
        
        try:
            for root, dirs, files in os.walk(self.base_path):
                for file in files:
                    if pattern.lower() in file.lower():
                        file_path = Path(root) / file
                        if file_type == "all" or (file_type == "file" and file_path.is_file()):
                            found_files.append(str(file_path))
            
            if found_files:
                print(f"\n=== '{pattern}' 검색 결과 ({len(found_files)}개) ===")
                for file in found_files:
                    print(file)
            else:
                print(f"'{pattern}'와 일치하는 파일을 찾을 수 없습니다.")
            
            return found_files
            
        except Exception as e:
            print(f"검색 실패: {e}")
            return []
    
    def show_history(self):
        """작업 기록 표시"""
        if not self.operations_history:
            print("작업 기록이 없습니다.")
            return
        
        print("\n=== 작업 기록 ===")
        for i, operation in enumerate(self.operations_history[-10:], 1):  # 최근 10개만 표시
            print(f"{i}. {operation['timestamp']} - {operation['operation']}")
            print(f"   소스: {operation['source']}")
            if operation['destination']:
                print(f"   대상: {operation['destination']}")
            print(f"   결과: {operation['result']}")
            print()

def main():
    manager = FileManager()
    
    while True:
        print("\n=== 파일 관리 도구 ===")
        print("1. 파일 목록 보기")
        print("2. 파일 생성")
        print("3. 디렉토리 생성")
        print("4. 파일 복사")
        print("5. 파일 이동")
        print("6. 파일 삭제")
        print("7. 파일 해시 확인")
        print("8. 파일 검색")
        print("9. 작업 기록 보기")
        print("10. 종료")
        
        choice = input("\n선택하세요 (1-10): ")
        
        if choice == "1":
            path = input("경로 (엔터시 현재 디렉토리): ").strip()
            show_hidden = input("숨김 파일 표시? (y/n): ").lower() == 'y'
            manager.list_files(path if path else None, show_hidden)
        
        elif choice == "2":
            filename = input("파일명: ")
            content = input("내용 (엔터시 빈 파일): ")
            manager.create_file(filename, content)
        
        elif choice == "3":
            dirname = input("디렉토리명: ")
            manager.create_directory(dirname)
        
        elif choice == "4":
            source = input("복사할 파일: ")
            destination = input("대상 경로: ")
            manager.copy_file(source, destination)
        
        elif choice == "5":
            source = input("이동할 파일: ")
            destination = input("대상 경로: ")
            manager.move_file(source, destination)
        
        elif choice == "6":
            filename = input("삭제할 파일/디렉토리: ")
            confirm = input("정말 삭제하시겠습니까? (y/n): ")
            if confirm.lower() == 'y':
                manager.delete_file(filename)
        
        elif choice == "7":
            filename = input("해시를 확인할 파일: ")
            hash_value = manager.get_file_hash(filename)
            if hash_value:
                print(f"MD5 해시: {hash_value}")
        
        elif choice == "8":
            pattern = input("검색할 파일명 패턴: ")
            manager.find_files(pattern)
        
        elif choice == "9":
            manager.show_history()
        
        elif choice == "10":
            print("프로그램을 종료합니다.")
            break
        
        else:
            print("잘못된 선택입니다.")

if __name__ == "__main__":
    main()
```

## 5. 실행 방법

### 1. 계산기 실행
```bash
python calculator.py
```

### 2. 학생 성적 관리 시스템 실행
```bash
python student_management.py
```

### 3. 웹 스크래퍼 실행 (BeautifulSoup 설치 필요)
```bash
pip install beautifulsoup4 requests
python web_scraper.py
```

### 4. 파일 관리 도구 실행
```bash
python file_manager.py
```

## 6. 프로젝트 확장 아이디어

### 1. 계산기 개선
- GUI 버전 (tkinter 사용)
- 과학 계산기 기능 추가
- 계산 그래프 표시

### 2. 성적 관리 시스템 개선
- 웹 인터페이스 (Flask 사용)
- 데이터베이스 연동 (SQLite)
- 성적 차트 생성

### 3. 웹 스크래퍼 개선
- 스케줄링 기능
- 데이터베이스 저장
- 이메일 알림 기능

### 4. 파일 관리 도구 개선
- GUI 버전
- 클라우드 스토리지 연동
- 파일 동기화 기능

## 7. 다음 학습 단계

1. 예외 처리 심화
2. 파일 입출력 고급 기능
3. 데이터베이스 연동
4. 웹 프레임워크 (Flask/Django)
5. GUI 프로그래밍 (tkinter/PyQt)

---

**핵심 포인트**
- 실습을 통한 파이썬 문법 익히기
- 클래스와 모듈 활용
- 파일 처리와 데이터 저장
- 외부 라이브러리 사용
- 에러 처리와 사용자 경험 개선
