"""
Stacked PR 예제 프로젝트
"""
from auth import AuthService
from profile import ProfileService

def main():
    print("Hello, Stacked PR!")
    auth = AuthService()
    auth.register("user1", "password123")
    print("사용자 등록 완료")
    
    profile = ProfileService(auth)
    profile.create_profile("user1", "user1@example.com", "User One")
    print("프로필 생성 완료")

if __name__ == "__main__":
    main()

