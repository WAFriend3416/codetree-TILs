def check_dec(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True


n,m = map(int,input().split())
result = 0
for i in range(n,m+1):
    if n == m:
        break
    if check_dec(i):
        result = result + i
    else:
        continue

print(result)