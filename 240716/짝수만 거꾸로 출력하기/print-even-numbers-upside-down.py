n = int(input())
li = list(map(int,input().split()))

li = sorted(li)

for i in li:
    if i%2 ==0:
        print(i,end=' ')