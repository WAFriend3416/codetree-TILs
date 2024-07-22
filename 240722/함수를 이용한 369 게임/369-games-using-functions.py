def check_num_in3(n):
    n = list(map(int,str(num)))
    li = [3,6,9]
    return n in li

def check_num_mul3(n):
    return n%3 == 0

cnt = 0 

n,m = map(int,input().split())

for i in range(n,m+1):
    if check_num_in3(i) or check_num_mul3(i):
        cnt = cnt + 1

print(cnt)