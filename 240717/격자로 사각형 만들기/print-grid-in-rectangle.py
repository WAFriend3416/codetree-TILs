n = int(input())

li = [
    [0 for _ in range(n)]
    for _ in range(n)
]


for i in range(n):
    li[0][i] = 1
i=0

for i in range(n):
    li[i][0] = 1

i=0

for i in range(1,n):
    for j in range(1,n):
        li[i][j] = li[i-1][j] + li[i][j-1] + li[i-1][j-1]

for row in li:
    for item in row:
        print(item, end=' ')
    print()