n,m = map(int,input().split())

li = [
    0 for _ in range(n)
]

for i in range(m):
    n,m = map(int,input().split())
    if n == m:
        li[n-1] += 1
    else:
        for i in range(n-1,m):
            li[i] += 1
    #print(li)

print(max(li))