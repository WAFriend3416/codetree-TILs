n,m = map(int,input().split())

li = [
    [0 for _ in range(m)]
    for _ in range(n)
]

cnt = 0

for j in range(0,m):
    if j%2 == 0:
        for i in range(0,n):
            li[i][j] = cnt
            cnt = cnt + 1
    else:
        for i in range(n-1,-1,-1):
            li[i][j] = cnt
            cnt = cnt + 1

for row in li:
    for item in row:
        print(item,end=' ')
    print()