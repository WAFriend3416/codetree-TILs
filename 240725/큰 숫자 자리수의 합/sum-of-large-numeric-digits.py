def BigNum(N):
    if N < 10:
        return N
    N1 = N // 10
    return BigNum(N1) + (N % 10)

li = list(map(int,input().split()))

total = 1
for i in li:
    total *= i

print(BigNum(total))