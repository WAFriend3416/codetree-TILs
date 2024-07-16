n = int(input())
li = list(map(int,input().split()))


li = reversed(sorted(li))
li_even = []
for i in li:
    if i%2 ==0:
        li_even.append(i)

for j in li_even:
    print(j,end=' ')