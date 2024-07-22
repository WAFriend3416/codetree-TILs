def min_num(a,b,c):
    li = []
    li.append(a)
    li.append(b)
    li.append(c)
    li = sorted(li)
    return li[0]

n,m,t = map(int,input().split())

res = min_num(n,m,t)

print(res)