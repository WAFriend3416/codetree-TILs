n = int(input())

cnt = 1
cnt2 = n

li = []

for i in range(0,n):
    if i % 2 == 0 :
        li_ = ""
        for j in range(0,cnt):
            print('*',end=' ')
            li_ = li_ + '* '
        li.append(li_)
        cnt = cnt + 1
    else:
        li_ = ""
        for j in range(cnt2,0,-1):
            print('*',end=' ')
            li_ = li_ + '* '
        li.append(li_)
        cnt2 = cnt2 -1 
    print()

li2 = li.reverse()

for a in li:
    print(a)