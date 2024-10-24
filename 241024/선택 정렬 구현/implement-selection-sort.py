N = int(input())
li = list(map(int,input().split()))

for i in range(N-1):
    minV = i
    for j in range(i+1,N):
        if li[j] < li[minV]:
            minV = j
    tmp =  li[i]
    li[i] = li[minV]
    li[minV] = tmp

for j in li:
    print(j,end=' ')