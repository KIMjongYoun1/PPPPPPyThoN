"""
UserService - 사용자 관련 비즈니스 로직
"""

from ..models.user import User

class UserService:
    """사용자 관련 서비스 클래스"""
    
    def __init__(self):
        """서비스 초기화"""
        self.users = {}  # 메모리에 사용자 저장 (실제로는 DB 사용)
    
    def create_user(self, user_id, name, email, age=None):
        """
        새 사용자 생성
        
        Args:
            user_id (str): 사용자 ID
            name (str): 사용자 이름
            email (str): 이메일 주소
            age (int, optional): 나이
            
        Returns:
            User: 생성된 사용자 객체
            
        Raises:
            ValueError: 이미 존재하는 사용자 ID인 경우
        """
        if user_id in self.users:
            raise ValueError(f"사용자 ID '{user_id}'는 이미 존재합니다.")
        
        user = User(user_id, name, email, age)
        self.users[user_id] = user
        return user
    
    def get_user(self, user_id):
        """
        사용자 조회
        
        Args:
            user_id (str): 사용자 ID
            
        Returns:
            User: 사용자 객체 (없으면 None)
        """
        return self.users.get(user_id)
    
    def get_all_users(self):
        """
        모든 사용자 조회
        
        Returns:
            list: 사용자 객체 리스트
        """
        return list(self.users.values())
    
    def get_active_users(self):
        """
        활성 사용자만 조회
        
        Returns:
            list: 활성 사용자 객체 리스트
        """
        return [user for user in self.users.values() if user.is_active]
    
    def update_user(self, user_id, **kwargs):
        """
        사용자 정보 업데이트
        
        Args:
            user_id (str): 사용자 ID
            **kwargs: 업데이트할 필드들
            
        Returns:
            User: 업데이트된 사용자 객체
            
        Raises:
            ValueError: 사용자가 존재하지 않는 경우
        """
        user = self.get_user(user_id)
        if not user:
            raise ValueError(f"사용자 ID '{user_id}'를 찾을 수 없습니다.")
        
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
        
        return user
    
    def delete_user(self, user_id):
        """
        사용자 삭제 (비활성화)
        
        Args:
            user_id (str): 사용자 ID
            
        Returns:
            bool: 삭제 성공 여부
        """
        user = self.get_user(user_id)
        if user:
            user.deactivate()
            return True
        return False
    
    def get_user_count(self):
        """
        사용자 수 조회
        
        Returns:
            int: 전체 사용자 수
        """
        return len(self.users)
    
    def get_active_user_count(self):
        """
        활성 사용자 수 조회
        
        Returns:
            int: 활성 사용자 수
        """
        return len(self.get_active_users())
