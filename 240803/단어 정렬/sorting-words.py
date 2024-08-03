n = int(input())
li = []

for _ in range(n):
    li.append(input())

for item in sorted(li):
    print(item)