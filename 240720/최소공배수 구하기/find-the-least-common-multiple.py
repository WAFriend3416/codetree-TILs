def asdf(n,m):
    a = n
    b = m
    while(True):
        q = n//m
        r = n%m
        if(r == 0):
            break
        n = m
        m = r

    print(int((a*b)/m))

n,m = map(int,input().split())

asdf(n,m)