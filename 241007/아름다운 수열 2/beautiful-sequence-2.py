from itertools import combinations, permutations

N,M = map(int,input().split())
li = list(map(int,input().split()))
target = list(map(int,input().split()))

#target_case = list(permutations(target,M))
#print(target_case)
answer = 0

for i in range(0,len(li)-M+1):
    cnt = 0
    target_case = target[:]
    for j in li[i:i+M]:
        #print(j,end = ' ')
        if j in target_case:
            #target_case.pop(target_case.index(j))
            target_case.remove(j)
    #print()
    if len(target_case) == 0:
       answer += 1

print(answer)