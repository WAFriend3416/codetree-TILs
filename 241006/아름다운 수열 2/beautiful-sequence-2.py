from itertools import combinations, permutations

N,M = map(int,input().split())
li = list(map(int,input().split()))
target = list(map(int,input().split()))

target_case = list(permutations(target,M))
#print(target_case)
answer = 0

for i in range(len(li)-M+1):
    cnt = 0
    #print(li[i:i+M])
    #print(tuple(li[i:i+M]))
    if tuple(li[i:i+M]) in target_case:
       answer += 1

print(answer)