n = list(input())
#result = []
cmd = list(input())

for i in cmd:
    result = []
    for M in n:
            result.append(M)
    #print('result:',result)
    if i == 'L':
        for j in range(1,len(n)):
            n[j-1] = result[j] 
        n[-1] = result[0]
        #print(n)    
    else:
        for j in range(0,len(n)-1):
            n[j+1] = result[j]
        n[0] =result[-1]
        #print(n) 

for i in range(len(n)):
     print(n[i],end='')

# CODETREE
# ODETREEC
#  ODETREE