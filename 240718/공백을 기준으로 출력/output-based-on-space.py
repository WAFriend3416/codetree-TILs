li = []
for _ in range(2):
    n = list(map(str,input().split()))
    li.append(n)

for row in li:
    for item in row:
        print(item, end='')