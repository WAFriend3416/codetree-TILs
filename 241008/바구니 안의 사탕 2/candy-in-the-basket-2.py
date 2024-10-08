basket = [ 0 for _ in range(101)]

N,K = map(int,input().split())

for _ in range(N):
    candy,b_pos = map(int,input().split())
    basket[b_pos] += candy
maxV = 0
#print(basket[:16])
for i in range(K,len(basket)-K):
    #print()
    maxV = max(maxV,sum(basket[i-K:i+K+1]))

print(maxV)