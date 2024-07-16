n = int(input())
li = list(map(int,input().split()))

li_result = set()
for i in range(0,n-1):
    curV2 = abs(li[i] - li[i+1])
    if curV2 in li_result:
        continue
    else:
        li_result.add(curV2)

print(min(li_result))