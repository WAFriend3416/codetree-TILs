def check_num_in3(n):
    num1 = n % 10
    num2 = n // 10
    li = [3,6,9]
    return num1 in li or num2 in li

def check_num_mul3(n):
    return n%3 == 0

cnt = 0 

n,m = map(int,input().split())

for i in range(n,m+1):
    if check_num_in3(i) or check_num_mul3(i):
        cnt = cnt + 1

print(cnt)