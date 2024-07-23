n,m = map(int,input().split())

li = list(map(int,input().split()))

for _ in range(4):
    a,b = map(int,input().split())
    total = 0
    a = a-1
    b = b-1
    for i in li[a:b]:
        total += i
    print(total)