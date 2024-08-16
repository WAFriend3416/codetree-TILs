OFFSET = 100
area = [
    [0 for _ in range(201)] for _ in range(201)
]

n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    x = a+OFFSET
    y = b+OFFSET
    for i in range(0,8):
        for j in range(0,8):
            area[(x-8)+i][y+j] += 1

cnt = 0
for row in area:
    for i in row:
        if i > 0:
            cnt += 1

print(cnt)