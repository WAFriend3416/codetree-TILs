cnt = 0
n = int(input())
while(True):
    if(n >= 1000):
        break
    else:
        if(n%2):
            n = (n * 2) + 2
            cnt = cnt + 1
        else:
            n = (n * 3) + 1
            cnt = cnt + 1

print(cnt)