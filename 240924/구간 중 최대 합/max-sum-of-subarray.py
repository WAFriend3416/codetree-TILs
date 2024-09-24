N,M = map(int,input().split())
numbers = list(map(int,input().split()))


mV = 0
for i in range(0,N-M+1):
    result = 0
   
    for j in range(i,i+M):
        #print(i+j)
        result += numbers[j]
    #print(result)
    mV = max(mV,result)


print(mV)