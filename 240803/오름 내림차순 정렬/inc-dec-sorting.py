n = int(input())

li = list(map(int,input().split()))

for i in sorted(li,reverse=False):
    print(i,end=' ')
print()

for i in sorted(li,reverse=True):
    print(i,end=' ')