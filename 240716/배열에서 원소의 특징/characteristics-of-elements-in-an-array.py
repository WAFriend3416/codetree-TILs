li = list(map(int,input().split()))

cnt = 0
for i in li:
    if i%3 ==0:
        if cnt < 0:
            print(li[0])
            break
        else:
            print(li[cnt-1])
            break
    cnt = cnt + 1