n = int(input())

li = list(map(int,input().split()))

result = 1

for i in li:
    if result % i == 0:
        continue
    else:
        result *= i

print(result)