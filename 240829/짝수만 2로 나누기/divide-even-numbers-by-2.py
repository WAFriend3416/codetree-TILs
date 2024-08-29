N = int(input())

li = list(map(int,input().split()))


for i in li:
    if i%2 == 0:
        print(i//2,end=' ')
    else:
        print(i,end=' ')