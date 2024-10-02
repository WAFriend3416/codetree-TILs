N = int(input())
li = list(map(int,input().split()))

cnt = 0
for i in range(N):
    for j in range(i,N):
        sumVal = 0
        cntVal = 0
        avrVal = 0
        if i == j:
            cnt += 1
        else:
            for k in range(i,j+1):
                sumVal += li[k]
                cntVal += 1
            avrVal = sumVal/cntVal
            if avrVal in li[i:j+1]:
                cnt += 1

print(cnt)