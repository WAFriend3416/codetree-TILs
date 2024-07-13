n = int(input())

cnt = 1
cnt2 = n
for i in range(0,n):
    if i % 2 == 0 :
        for j in range(0,cnt):
            print('*',end=' ')
        cnt = cnt + 1
    else:
        for j in range(cnt2,0,-1):
            print('*',end=' ')
        cnt2 = cnt2 -1 
    print()

cnt = cnt - 1
cnt2 = cnt2 + 1

for i in range(0,n):
    if i % 2 == 0 :
        for j in range(cnt,0,-1):
            print('*',end=' ')
        cnt = cnt - 1
    else:
        for j in range(0,cnt2):
            print('*',end=' ')
        cnt2 = cnt2 + 1 
    print()