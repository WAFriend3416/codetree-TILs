N,M = map(int,input().split())
numbers = list(map(int,input().split()))


mV = 0
for i in range(0,N-M):
    result = 0
   
    for j in range(i,i+M):
        #print(i+j)
        result += numbers[j]
    mV = max(mV,result)


print(mV)