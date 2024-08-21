a,b,c = map(int,input().split())

li = [0] * a
li_in = []
setting = True

for _ in range(b):
    i= int(input())
    li[i-1] += 1
    #print(li)
    if li[i-1] == c:
        setting = False
        print(li.index(li[i]))
        break
    
if setting:
    print(-1)