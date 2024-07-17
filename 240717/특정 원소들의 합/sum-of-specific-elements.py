li = []
total = 0
for i in range(4):
    row = list(map(int,input().split()))
    li.append(row)
for j in range(0,4):
    for k in range(0,j+1):
        total = total + li[j][k]

print(total)