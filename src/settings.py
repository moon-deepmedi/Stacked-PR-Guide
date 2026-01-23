"""
사용자 설정 모듈 (Feature A-3)
프로필 기능(feature-a-2)을 사용합니다.
"""
from auth import AuthService
from profile import ProfileService

class SettingsService:
    def __init__(self, auth_service: AuthService, profile_service: ProfileService):
        self.auth_service = auth_service
        self.profile_service = profile_service
        self.settings = {}
    
    def update_setting(self, username: str, key: str, value: str) -> bool:
        """사용자 설정 업데이트"""
        # 프로필이 존재하는지 확인
        profile = self.profile_service.get_profile(username)
        if not profile:
            return False
        
        if username not in self.settings:
            self.settings[username] = {}
        
        self.settings[username][key] = value
        return True
    
    def get_setting(self, username: str, key: str) -> str:
        """사용자 설정 조회"""
        return self.settings.get(username, {}).get(key, "")

