"""
사용자 인증 모듈 (Feature A-1)
"""
class AuthService:
    def __init__(self):
        self.users = {}
    
    def register(self, username: str, password: str) -> bool:
        """사용자 등록"""
        if username in self.users:
            return False
        self.users[username] = password
        return True
    
    def login(self, username: str, password: str) -> bool:
        """사용자 로그인"""
        return self.users.get(username) == password

