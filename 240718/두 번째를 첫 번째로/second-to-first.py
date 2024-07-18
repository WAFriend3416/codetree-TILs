n = list(input())

n1 = n[0]
n2 = n[1]

for i in range(len(n)):
    if n[i] == n2:
        n[i] = n1

n = ''.join(n)

print(n)