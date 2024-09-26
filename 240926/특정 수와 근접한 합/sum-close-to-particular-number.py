S, N = map(int,input().split())

li = list(map(int,input().split()))

diff = N
total = 0
for i in range(0,S):
    for j in range(0,S):
        total = 0
        for k in range(S):
            if k == i or k ==j or i == j:
                continue
            else:
                #print(k,end=' ')
                total += li[k]
        #print()
        #print(total)
        diff = min(diff,abs(total-N))

print(diff)