li = [
    0 for _ in range(200)
]

n = int(input())

for i in range(n):
    n,m = map(int,input().split())
    n += 100
    m += 100
    for j in range(n-1,m-1):
        li[j] += 1
    
print(max(li))