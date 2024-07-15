n = int(input())

cnt = n-2
cnt2 = 0

if n == 1:
    print('*')
else:
    
    for j in range(0,n):
        print('*',end =' ')
    print()
    for k in range(0,n-2):
        print('*',end =' ')
        for b in range(0,cnt2):
            print('*',end =' ')
        for m in range(0,cnt):
            print(' ',end =' ')
        cnt = cnt - 1
        cnt2 = cnt2 + 1
        print('*',end =' ')
        print()
    for z in range(0,n):
        print('*',end =' ')