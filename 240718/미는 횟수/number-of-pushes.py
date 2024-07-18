n1 = list(input())
n2 = list(input())

cnt = 0
for k  in range(len(n1)):
    result = []
    for M in n1:
        result.append(M)

    cnt = cnt + 1
    for i in range(1,len(n1)):
        n1[i] = result[i-1]
    n1[0] = result[-1]
    
    #print(n1)
    if n1 == n2:
        print(cnt)
        break

if k == len(n1)-1:
    print(-1)