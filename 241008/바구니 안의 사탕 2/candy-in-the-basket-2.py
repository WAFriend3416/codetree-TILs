basket = [ 0 for _ in range(101)]

N,K = map(int,input().split())

for _ in range(N):
    candy,b_pos = map(int,input().split())
    basket[b_pos] += candy
maxV = 0
#print(basket[:16])
#print(K,len(basket)-K)
if K >= 100:
    print(sum(basket))
else:
    for i in range(len(basket)-K):
        #print(i)
        #print(basket[i:i+K+K])
        maxV = max(maxV,sum(basket[i:i+K+K+1]))

    print(maxV)