n = int(input())
li = list(map(int,input().split()))


li = sorted(li)
li_even = []
for i in li:
    if i%2 ==0:
        li_even.append(i)

li_even = reversed(li_even)
for j in li_even:
    print(j,end=' ')