def check_in369(n):
    li = list(map(int,str(n)))
    if 3 in li or 6 in li or 9 in li:
        return True
    else:
        return False

def check_mul3(n):
    return n%3 == 0


cnt = 0

n,m = map(int,input().split())

for i in range(n,m+1):
    if check_in369(i) or check_mul3(i):
        cnt = cnt + 1
    else:
        continue

print(cnt)