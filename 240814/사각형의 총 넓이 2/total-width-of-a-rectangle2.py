area = [
    [0 for _  in range(200)] for _ in range(200)
]

list_pos = []

n = int(input())

for _ in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            area[i][j] += 1

cnt = 0
for i in area:
    for j in i:
        if j > 0:
            cnt += 1    

print(cnt)