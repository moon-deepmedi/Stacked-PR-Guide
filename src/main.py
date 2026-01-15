"""
Stacked PR 예제 프로젝트
"""
from auth import AuthService

def main():
    print("Hello, Stacked PR!")
    auth = AuthService()
    auth.register("user1", "password123")
    print("사용자 등록 완료")

if __name__ == "__main__":
    main()

