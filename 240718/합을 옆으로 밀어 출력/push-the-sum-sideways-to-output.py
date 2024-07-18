n = int(input())
total = 0
for _ in range(n):
    total = total + int(input())

total = list(str(total))

result = [0 for _ in range(len(total))]

for i in range(1,len(total)):
    result[i-1] = total[i]

result[-1] = total[0]

for item in result:
    print(item,end='')