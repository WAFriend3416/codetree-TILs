n = int(input())
li = list(map(int,input().split()))

li = sorted(li)
minV = 1
for i in range(0,n-1):
    curV = abs(li[i] - li[i+1])
    if minV >= curV: 
        minV = curV

print(minV)