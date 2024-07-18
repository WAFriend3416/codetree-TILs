li = []
for _ in range(3):
    n = input()
    li.append(len(n))

print(max(li) - min(li))