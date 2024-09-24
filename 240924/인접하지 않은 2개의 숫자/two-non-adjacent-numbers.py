N = int(input())

nums = list(map(int,input().split()))

maxValue = 0

for i in range(N):
    for j in range(N):
        if j == (i+1) or j == (i-1) or i == j:
            continue
        else:
            result = nums[i] + nums[j]
            if maxValue <= result:
                maxValue = result

print(maxValue)