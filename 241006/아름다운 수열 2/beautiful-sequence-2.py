N,M = map(int,input().split())
li = list(map(int,input().split()))
target = list(map(int,input().split()))

answer = 0

for i in range(len(li)-M+1):
    cnt = 0
    #print(li[i:i+M])
    for j in target:
        if j in li[i:i+M]:
            cnt += 1
    if cnt == M:
        #print(li[i:i+M],target)
        answer += 1

print(answer)