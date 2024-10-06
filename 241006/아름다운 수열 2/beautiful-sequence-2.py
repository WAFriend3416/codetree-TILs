from itertools import combinations, permutations

N,M = map(int,input().split())
li = list(map(int,input().split()))
target = list(map(int,input().split()))

combi = list(combinations(target, M))

answer = 0

for i in range(len(li)-M+1):
    cnt = 0
    #print(li[i:i+M])
    if li[i:i+M] in combi:
        answer += 1

print(answer)