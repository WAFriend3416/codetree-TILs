N = list(map(int,input()))

def binaryToDecimal(n):
    total = 0
    for i in range(0,len(n)):
        #print(n[i],(2 ** (len(n)-1-i)))
        total += n[i] * (2 ** (len(n)-1-i))
    return total

maxNumber = binaryToDecimal(N)

#print(binaryToDecimal(N))
li_res = []

for i in range(0,len(N)):
    test = N
    test[i] = 0 if test[i] == 1 else 1
    #print(test,binaryToDecimal(test))
    li_res.append(binaryToDecimal(test))

print(max(li_res))