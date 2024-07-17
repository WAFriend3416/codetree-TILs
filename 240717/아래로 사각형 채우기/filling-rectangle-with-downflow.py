n = int(input())
cnt = 1

arr_2d = [
    [0 for _ in range(n)]
     for _ in range(n)
]

for i in range(n):
    for j in range(n):
        arr_2d[j][i] = cnt
        cnt = cnt + 1

for row in arr_2d:
    for item in row:
        print(item, end=' ')
    print()