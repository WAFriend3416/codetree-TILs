OFFSET = 1000

area = [
    [0 for _  in range(2001)] for _ in range(2001)
]

list_pos = []

for _ in range(2):
    x1,y1,x2,y2 = map(int,input().split())
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET
    for i in range(x1,x2):
        for j in range(y1,y2):
            area[i][j] += 1

x1,y1,x2,y2 = map(int,input().split())
x1 += OFFSET
y1 += OFFSET
x2 += OFFSET
y2 += OFFSET
for i in range(x1,x2):
    for j in range(y1,y2):
        area[i][j] -= 1

cnt = 0
for i in area:
    for j in i:
        if j == 1:
            cnt += 1    

print(cnt)