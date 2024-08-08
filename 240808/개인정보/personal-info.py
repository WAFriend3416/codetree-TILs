class User:
    def __init__(self,name,h,w):
        self.name = name
        self.h = h
        self.w = w

Users = []

for _ in range(5):
    name,h,w = map(str,input().split())
    user = User(name,int(h),float(w))
    Users.append(user)

Users.sort(key = lambda x : (x.name))
print("name")
for user in Users:
    print(f'{user.name} {user.h} {user.w:.1f}')

Users.sort(key = lambda x : -x.h)
print("\nheight")
for user in Users:
    print(f'{user.name} {user.h} {user.w:.1f}')