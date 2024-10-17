N = int(input())
li = list(map(int,input().split()))

for i in range(0,N-1):
    for j in range(0,N-1-i):
        if li[j] > li[j+1]:
            li[j] , li[j+1] = li[j+1],li[j]
        else:
            continue

for k in li:
    print(k,end=' ')