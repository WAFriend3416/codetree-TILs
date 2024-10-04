nums = list(map(int,input().split()))

sum0 = sum(nums)
minV = 1000000000000

for i in range(len(nums)-2):
    for j in range(1,len(nums)-1):
        for k in range(2,len(nums)):
            sum1 = nums[i] + nums[j] + nums[k]
            sum2 = sum0 - sum1
            minV = min(minV,abs(sum1-sum2))


print(minV)