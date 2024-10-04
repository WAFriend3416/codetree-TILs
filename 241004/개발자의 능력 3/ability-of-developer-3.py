nums = list(map(int,input().split()))

sum0 = sum(nums)
minV = 1000000000000

for i in range(len(nums)-2):
    for j in range(1,len(nums)-1):
        for k in range(2,len(nums)):
            if i == j or i == k or j == k:
                # print(nums[i] , nums[j] , nums[k])
                continue
            else:
                sum1 = nums[i] + nums[j] + nums[k]
                sum2 = sum0 - sum1
                # if abs(sum1-sum2) == 4:
                #     print(nums[i] , nums[j] , nums[k])
                minV = min(minV,abs(sum1-sum2))
            #print(minV)

print(minV)