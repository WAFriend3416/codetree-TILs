import sys

INT_MAX = sys.maxsize

def calculate_distance(x1, x2):
    return abs(x1[0] - x2[0]) + abs(x1[1] - x2[1])

N = int(input())
checkPoint = [
    list(map(int, input().split()))
    for _ in range(N)
]

answer = INT_MAX

for j in range(1, N-1):  # 첫 번째와 마지막 체크포인트는 제거하지 않음
    result = 0
    checkPoint_new = checkPoint[:j] + checkPoint[j+1:]  # j번째 체크포인트를 제거
    
    for k in range(1, len(checkPoint_new)):
        result += calculate_distance(checkPoint_new[k-1], checkPoint_new[k])
    
    answer = min(answer, result)

print(answer)