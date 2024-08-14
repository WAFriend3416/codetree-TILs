moveL = 0
moveR = 0

n = int(input())
for i in range(n):
    a,b = map(str,input().split())
    movePoint = int(a)
    if b == 'R':
        moveR += movePoint
    else:
        moveL += movePoint

if moveL < moveR:
    print(moveL)
else:
    print(moveR)