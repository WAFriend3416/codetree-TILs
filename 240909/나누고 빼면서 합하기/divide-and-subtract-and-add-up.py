n,m = map(int,input().split())
li = list(map(int,input().split()))


total = 0 
total += li[m-1]
#print(m,li[m-1])
while(m > 1):
    if m % 2 == 0:
        m = m // 2
        #print(m,li[m-1])
        total += li[m-1]
    else:
        m -= 1
        #print(m,li[m-1])
        total += li[m-1]

print(total)