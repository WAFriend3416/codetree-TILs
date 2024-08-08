class User:
    def __init__(self,idx,h,w):
        self.idx = idx
        self.h = h
        self.w = w

Users = []
n = int(input())
for i in range(n):
    h,w = map(int,input().split())
    user = User(i+1,h,w)
    Users.append(user)

Users.sort(key = lambda x : (x.h,-x.w))

for user in Users:
    print(f'{user.h} {user.w} {user.idx}')