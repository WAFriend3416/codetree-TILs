N,H,T = map(int,input().split())
base = list(map(int,input().split()))

minV = 1000000000000000000
for i in range(0,N-T+1):
    compV = 0
    target = base[i:i+T]
    #print(target) 
    for j in target:
        compV += abs(H-j)
    #print(compV)
    minV = min(compV,minV)


print(minV)