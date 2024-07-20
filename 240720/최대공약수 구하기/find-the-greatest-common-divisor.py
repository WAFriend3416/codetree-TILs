def asdf(n,m):
    while(True):
        q = n//m
        r = n%m
        if(r == 0):
            break
        n = m
        m = r

    print(m)

n,m = map(int,input().split())

asdf(n,m)