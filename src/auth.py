"""
사용자 인증 모듈 (Feature A-1)
"""
class AuthService:
    MIN_PASSWORD_LENGTH = 6
    
    def __init__(self):
        self.users = {}
    
    def register(self, username: str, password: str) -> bool:
        """
        사용자 등록
        
        Args:
            username: 사용자명
            password: 비밀번호 (최소 6자 이상)
        
        Returns:
            bool: 등록 성공 여부
        """
        # 사용자명 중복 체크
        if username in self.users:
            return False
        
        # 비밀번호 길이 검증 (리뷰 반영: 최소 길이 체크 추가)
        if len(password) < self.MIN_PASSWORD_LENGTH:
            return False
        
        self.users[username] = password
        return True
    
    def login(self, username: str, password: str) -> bool:
        """
        사용자 로그인
        
        Args:
            username: 사용자명
            password: 비밀번호
        
        Returns:
            bool: 로그인 성공 여부
        """
        stored_password = self.users.get(username)
        if stored_password is None:
            return False
        return stored_password == password

