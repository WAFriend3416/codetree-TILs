N,M = map(int,input().split())
li = list(map(int,input().split()))
target = list(map(int,input().split()))

answer = 0

for i in range(len(li)-M+1):
    cnt = 0
    #print('i: ',i)
    for j in range(M):
        #print(i+j)
        if li[i+j] in target:
            cnt += 1
    #print('-------------------')
    if cnt == M:
        answer += 1

print(answer)