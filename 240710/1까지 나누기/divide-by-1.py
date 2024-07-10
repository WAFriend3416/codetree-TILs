n = int(input())
res = 0
cnt = 1

while(n>1):
    n = int(n/cnt)
    res = res + 1
    cnt = cnt + 1

print(res)