li = list(map(int,input().split()))

li[2:] = [0 for i in range(8)]

for i in range(2,10):
    li[i] = li[i-1] + 2 * li[i-2]

for j in li:
    print(j,end=' ')