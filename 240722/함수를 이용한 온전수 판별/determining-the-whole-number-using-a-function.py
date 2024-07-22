def check_number(num):
    if num % 2 == 0:
        return False
    
    elif num % 10 == 5:
        return False
    
    elif num % 3 == 0  and num % 9 != 0:
        return False
    else:
        return True
    

cnt = 0
n,m = map(int,input().split())

for i in range(n,m+1):
    if check_number(i):
        cnt += 1

print(cnt)