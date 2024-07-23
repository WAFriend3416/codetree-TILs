def func(a,b):
    if a > b:
        a *= 2
        b += 10
        li = [b,a]
    else:
        b *= 2
        a += 10
        li = [a,b]
    return li


n,m = map(int,input().split())

lis = func(n,m)

for i in lis:
    print(i,end=' ')