OFFSET = 1000
area = [
    [0 for _ in range(2001)] for _ in range(2001)
]

li_input1 = list(map(int,input().split()))
li_input2 = list(map(int,input().split()))

for i in range(4):
    li_input1[i] += OFFSET
    li_input2[i] += OFFSET

for i in range(li_input1[3]-li_input1[1]):
    for j in range(li_input1[2]-li_input1[0]):
        area[li_input1[0]+i][li_input1[1]+j] += 3

for i in range(li_input2[3]-li_input2[1]):
    for j in range(li_input2[2]-li_input2[0]):
        area[li_input2[0]+i][li_input2[1]+j] -= 1        


cnt = 0
for row in area:
    for i in row:
        if i >= 2:
            cnt += 1

print(cnt)