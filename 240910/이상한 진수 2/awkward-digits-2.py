N = list(map(int,input()))

def binaryToDecimal(n):
    total = 0
    for i in range(0,len(n)):
        #print(n[i],(2 ** (len(n)-1-i)))
        total += n[i] * (2 ** (len(n)-1-i))
    return total

maxNumber = 0

#print(binaryToDecimal(N))
if 0 not in N:
    print(binaryToDecimal(N))
else:
    for i in range(1,len(N)):
        test = N
        test[i] = 0 if test[i] == 1 else 1
        #print(test,binaryToDecimal(test))
        maxNumber = binaryToDecimal(test) if maxNumber <= binaryToDecimal(test) else maxNumber

    print(maxNumber)