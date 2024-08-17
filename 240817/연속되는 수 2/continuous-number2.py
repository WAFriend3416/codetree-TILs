n = int(input())
cnt = 0
a = []
for _ in range(n):
    a.append(int(input()))
    
for i in range(n):
    if i == 0 or a[i] != a[i - 1]:
        cnt += 1

print(cnt)