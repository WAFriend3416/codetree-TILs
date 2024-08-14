SIZE = 2000

li = [
    0 for _ in range(2000)
]

strPoint = 999

n = int(input())
for i in range(n):
    a,b = map(str,input().split())
    movePoint = int(a)
    if b == 'R':
        for i in range(movePoint+1):
            li[strPoint+i] += 1
        strPoint = strPoint+i
        #print(strPoint)
    else:
        for i in range(movePoint+1):
            li[strPoint-i] += 1
        strPoint = strPoint-i
        #print(strPoint)

print(li.count(2))