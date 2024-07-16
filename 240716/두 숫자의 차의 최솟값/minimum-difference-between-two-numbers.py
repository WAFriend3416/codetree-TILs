n = int(input())
li = list(map(int,input().split()))

li_result = []
for i in range(1,n-1):
    curV1 = abs(li[i-1] - li[i])
    curV2 = abs(li[i] - li[i+1])
    li_result.append(curV1)
    li_result.append(curV2)

print(min(li_result))