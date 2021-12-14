# 전역변수
str = "Not Class Member"

# 클래스 정의
class GString:
    def __init__(self):
        # 인스턴스 멤버 변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        # 버그 발생~
        print(str)          # 결과: 전역변수(Not Class Member) 나옴
        # 이렇게 써야 함
        print(self.str)     # 결과: First Message 나옴

# 인스턴스
g = GString()
g.set("First Message")
g.print()
