n,m = map(int,input().split())

for i in range(2,9,2):
    for j in range(m,n-1,-1):
            print(j,'*',i,'=',j*i,end='')
            if j != n:
                print(' /',end=' ')
    print()