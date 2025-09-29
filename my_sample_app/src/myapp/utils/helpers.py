"""
헬퍼 함수들
"""

import re
import uuid
from datetime import datetime

def format_currency(amount, currency="KRW"):
    """
    통화 형식으로 포맷팅
    
    Args:
        amount (float): 금액
        currency (str): 통화 코드
        
    Returns:
        str: 포맷팅된 통화 문자열
    """
    if currency == "KRW":
        return f"{amount:,.0f}원"
    elif currency == "USD":
        return f"${amount:,.2f}"
    else:
        return f"{amount:,.2f} {currency}"

def validate_email(email):
    """
    이메일 주소 유효성 검증
    
    Args:
        email (str): 이메일 주소
        
    Returns:
        bool: 유효한 이메일인지 여부
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def generate_id(prefix=""):
    """
    고유 ID 생성
    
    Args:
        prefix (str): ID 접두사
        
    Returns:
        str: 생성된 고유 ID
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    unique_id = str(uuid.uuid4())[:8]
    return f"{prefix}{timestamp}_{unique_id}"

def clean_text(text):
    """
    텍스트 정리 (공백 제거, 소문자 변환)
    
    Args:
        text (str): 정리할 텍스트
        
    Returns:
        str: 정리된 텍스트
    """
    return re.sub(r'\s+', ' ', text.strip().lower())

def format_phone_number(phone):
    """
    전화번호 포맷팅
    
    Args:
        phone (str): 전화번호
        
    Returns:
        str: 포맷팅된 전화번호
    """
    # 숫자만 추출
    numbers = re.sub(r'\D', '', phone)
    
    if len(numbers) == 11 and numbers.startswith('010'):
        return f"{numbers[:3]}-{numbers[3:7]}-{numbers[7:]}"
    elif len(numbers) == 10:
        return f"{numbers[:3]}-{numbers[3:6]}-{numbers[6:]}"
    else:
        return phone
