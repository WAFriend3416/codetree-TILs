N = int(input())

li_num = list(map(int,input().split()))

minDistance = 10000000000
for i in range(0,N):
    total = 0
    for j in range(0,N):
        #print(abs(i-j),li_num[j])
        total += abs(i-j) * li_num[j]
    #print(total)
    minDistance = min(minDistance,total)

print(minDistance)