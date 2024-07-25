import math
n = int(input())

def func(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    else:
        return func(math.floor(N/3)) + func(N-1)

print(func(n))