class User:
    def __init__(self,name,h,w):
        self.name = name
        self.h = h
        self.w = w

Users = []
n = int(input())
for _ in range(n):
    name,h,w = map(str,input().split())
    user = User(name,int(h),int(w))
    Users.append(user)

Users.sort(key = lambda x : (x.h,-x.w))

for user in Users:
    print(f'{user.name} {user.h} {user.w}')