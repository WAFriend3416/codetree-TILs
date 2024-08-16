OFFSET = 100
MAX_R = 200

checked = [
    [0] * (MAX_R + 1)
    for _ in range(MAX_R + 1)
]

n = int(input())

for i in range(n):
    rect_input = list(map(int,input().split()))
    if i % 2 == 0:
        mark = 1 # red
    else:
        mark = 2 # blue
    
    for i in range(0,4):
        rect_input[i] += OFFSET
    
    i=0
    j=0

    for i in range(rect_input[0],rect_input[2]):
        for j in range(rect_input[1],rect_input[3]):
            checked[i][j] = mark

cnt = 0
for row in checked:
    for item in row:
        if item == 2:
            cnt += 1
print(cnt)