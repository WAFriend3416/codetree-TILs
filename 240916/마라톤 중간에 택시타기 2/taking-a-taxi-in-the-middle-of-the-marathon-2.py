import sys

INT_MAX = sys.maxsize

def calculate_distance(x1, x2):
    return abs(x1[0] - x2[0]) + abs(x1[1] - x2[1])

N = int(input())
checkPoints = [
    list(map(int, input().split()))
    for _ in range(N)
]

answer = INT_MAX

# 첫 번째와 마지막 체크포인트는 항상 포함
# 중간 체크포인트 중 하나만 건너뛰는 경우를 모두 고려
for skip in range(1, N-1):  # 1부터 N-2까지의 인덱스 (첫 번째와 마지막을 제외한 중간 체크포인트)
    result = 0
    prev = checkPoints[0]  # 시작점
    
    for i in range(1, N):
        if i == skip:
            continue  # 이 체크포인트를 건너뛴다
        curr = checkPoints[i]
        result += calculate_distance(prev, curr)
        prev = curr
    
    answer = min(answer, result)

print(answer)