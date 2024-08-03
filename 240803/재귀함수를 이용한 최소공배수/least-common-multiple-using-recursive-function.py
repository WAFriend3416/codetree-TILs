def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

def lcm(a, b):
    return a * b // gcd(a, b)

n = int(input())

li = list(map(int,input().split()))

lim = lcm(li[0],li[1])
if n > 2:
    for i in range(2,n):
        lim = lcm(lim,li[i])

elif n == 2:
    print(lcm(li[0],li[1]))

else:
    print(li[0])