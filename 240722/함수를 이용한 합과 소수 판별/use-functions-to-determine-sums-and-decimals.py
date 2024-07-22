def check_dec(num):
    cnt = 2
    while(num > cnt):
        if num % cnt == 0:
            return False
        cnt += 1
    return True


def check_sumdec_even(num):
    if ((num // 10) + (num % 10)) % 2 ==0:
        return True
    else:
        return False

cnt = 0
n,m = map(int,input().split())

for i in range(n,m+1):
    if check_dec(i):
        if check_sumdec_even(i):
            cnt += 1

print(cnt)