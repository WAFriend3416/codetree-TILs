n = int(input())
li = [int(input()) for _ in range(n)]

ans,cnt = 0,0
for i in range(n):
    if i >= 1 and (li[i] *li[i-1]) >= 0:
        cnt += 1
    else:
        cnt = 1
    
    ans = max(ans,cnt)

print(ans)