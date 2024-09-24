N,M = map(int,input().split())
numbers = list(map(int,input().split()))


mV = 0
for i in range(0,N-2):
    result = 0
    result = numbers[i] + numbers[i+1] +  numbers[i+2]
    if mV <= result:
        mV =result


print(mV)