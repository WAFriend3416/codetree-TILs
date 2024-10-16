N,H,T = map(int,input().split())
base = list(map(int,input().split()))

minV = 1000000000000000
for i in range(0,N-T):
    compV = 0
    target = base[i:i+T] 
    if (sum(target) % H) == 0:
        for j in target:
            compV += abs(H-j)
    
    minV = min(compV,minV)


print(minV)