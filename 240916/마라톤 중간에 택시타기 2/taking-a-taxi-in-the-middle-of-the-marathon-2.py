def calculate_distance(x1,x2):
    return abs(x1[0]-x2[0]) + abs(x1[1]-x2[1])


N = int(input())
checkPoint = []
for _ in range(N):
    checkPoint.append(list(map(int,input().split())))

answer = 1000000000
result = 0
for j in range(1,N-2):
    #print(j)
    checkPoint_new = checkPoint
    checkPoint_new.pop(j)
    for k in range(1,len(checkPoint_new)):
        #print(checkPoint_new)
        #print(checkPoint[k-1],checkPoint[k])
        result += calculate_distance(checkPoint[k-1],checkPoint[k])
    if answer >= result:
        answer = result

print(answer)