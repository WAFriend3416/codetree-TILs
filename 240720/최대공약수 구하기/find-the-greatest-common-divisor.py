def asdf(n,m):
    while(True):
        q = n//m
        r = n%m
        if(r == 0):
            break
        n = m
        m = r
    
    if(m == 1):
        print('서로소')
    else:
        print(m)

n,m = map(int,input().split())

asdf(n,m)