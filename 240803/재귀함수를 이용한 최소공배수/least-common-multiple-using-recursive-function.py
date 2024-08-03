n = int(input())

li = list(map(int,input().split()))

result = 1 * li[0]

for i in li[1:]:
    if result % i == 0:
        continue
    else:
        result *= i

print(result)