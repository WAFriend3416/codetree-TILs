n = int(input())
m = n
for i in range(1,n+1):
    for j in range(1,m+1):
        print(i,'*',j,'=',i*j,end=' ')
        if j != m:
            print('/',end=' ')
    m = m - 1
    print()