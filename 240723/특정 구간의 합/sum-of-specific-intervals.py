n,m = map(int,input().split())

li = list(map(int,input().split()))

for _ in range(4):
    a,b = map(int,input().split())
    total = 0
    for i in range(a-1,b):
        total += li[i]
    print(total)