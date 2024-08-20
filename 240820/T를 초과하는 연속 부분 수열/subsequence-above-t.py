n,m = map(int,input().split())
li = list(map(int,input().split()))

ans,cnt = 0,0
for i in range(n):
    if i >= 1 and li[i] > m:
        cnt += 1
    else:
        cnt = 0
    
    #print(li[i],ans,cnt)
    ans = max(ans,cnt)

print(ans)