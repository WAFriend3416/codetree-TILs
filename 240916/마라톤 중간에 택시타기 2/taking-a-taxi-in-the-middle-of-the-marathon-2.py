import sys

INT_MAX = sys.maxsize

def calculate_distance(x1,x2):
    return abs(x1[0]-x2[0]) + abs(x1[1]-x2[1])

N = int(input())
checkPoint = [
    list(map(int,input().split()))
    for _ in range(N)
]

answer = INT_MAX

for j in range(1,N-1):
    #print(j)
    result = 0
    checkPoint_new = checkPoint[:]
    checkPoint_new.pop(j)
    #print(checkPoint_new)
    for k in range(1,len(checkPoint_new)):        
        #print(checkPoint_new[k-1],checkPoint_new[k])
        result += calculate_distance(checkPoint_new[k-1],checkPoint_new[k])
    if answer >= result:
        answer = result

print(answer)