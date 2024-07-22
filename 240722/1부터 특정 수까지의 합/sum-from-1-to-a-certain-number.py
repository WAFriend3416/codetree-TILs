def add_range(n):
    result = 0
    total = 0
    for i in range(1,n+1):
        total = total + i
    result = int(total / 10)
    return result

n = int(input())

res = add_range(n)

print(res)