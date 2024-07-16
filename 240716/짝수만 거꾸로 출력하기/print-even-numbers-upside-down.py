n = int(input())
li = list(map(int,input().split()))


li = reverse(sorted(li))
li_even = []
for i in li:
    if i%2 ==0:
        li_even.append(i)