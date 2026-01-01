"""
사용자 프로필 모듈 (Feature A-2)
인증 기능(feature-a-1)을 사용합니다.
"""
from auth import AuthService

class ProfileService:
    def __init__(self, auth_service: AuthService):
        self.auth_service = auth_service
        self.profiles = {}
    
    def create_profile(self, username: str, email: str, name: str) -> bool:
        """사용자 프로필 생성"""
        # 인증 서비스를 통해 사용자 확인
        if username not in self.auth_service.users:
            return False
        
        self.profiles[username] = {
            "email": email,
            "name": name
        }
        return True
    
    def get_profile(self, username: str) -> dict:
        """사용자 프로필 조회"""
        return self.profiles.get(username, {})

