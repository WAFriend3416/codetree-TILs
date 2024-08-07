class User:
    def __init__(self,n,h,w):
        self.n = n
        self.h = h
        self.w = w

Users = []
n = int(input())

for _ in range(n):
    n,h,w = map(str,input().split())
    user = User(n,h,w)
    Users.append(user)

Users.sort(key=lambda x:x.h)

for User in Users:
    print(User.n,User.h,User.w)