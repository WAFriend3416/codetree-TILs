N,M = map(int,input().split())
li = list(map(int,input().split()))
target = list(map(int,input().split()))

answer = 0

for i in range(len(li)-2):
    cnt = 0
    for j in range(3):
        if li[i+j] in target:
            cnt += 1
    if cnt == 3:
        answer += 1

print(answer)