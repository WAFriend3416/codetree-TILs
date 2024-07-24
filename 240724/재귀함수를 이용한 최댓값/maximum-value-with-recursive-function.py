def search_max(N,n,k):
    if N == n:
        return k

    if li[N] >= k:
        k = li[N]

    return search_max(N+1,n,k) 


n = int(input())

li = list(map(int,input().split()))

print(search_max(0,n,0))