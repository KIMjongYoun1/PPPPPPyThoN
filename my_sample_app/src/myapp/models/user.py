"""
User 모델 클래스
"""

from datetime import datetime

class User:
    """사용자 정보를 나타내는 클래스"""
    
    def __init__(self, user_id, name, email, age=None):
        """
        사용자 객체 초기화
        
        Args:
            user_id (str): 사용자 ID
            name (str): 사용자 이름
            email (str): 이메일 주소
            age (int, optional): 나이
        """
        self.user_id = user_id
        self.name = name
        self.email = email
        self.age = age
        self.created_at = datetime.now()
        self.is_active = True
    
    def __str__(self):
        """문자열 표현"""
        return f"User(id={self.user_id}, name={self.name}, email={self.email})"
    
    def __repr__(self):
        """개발자용 문자열 표현"""
        return f"User('{self.user_id}', '{self.name}', '{self.email}', {self.age})"
    
    def get_info(self):
        """사용자 정보 반환"""
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'age': self.age,
            'created_at': self.created_at.isoformat(),
            'is_active': self.is_active
        }
    
    def deactivate(self):
        """사용자 비활성화"""
        self.is_active = False
    
    def activate(self):
        """사용자 활성화"""
        self.is_active = True
