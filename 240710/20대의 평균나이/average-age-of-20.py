total = 0
cnt = 0
while(True):
    n = int(input())
    if(n < 20 or n > 29):
        break
    total = total + n
    cnt = cnt + 1
result = total / cnt
print(f'{result:.2f}')