a = int(input())

for i in range(1,a+1):
    if(int(i/8)%2 == 0):
        continue
    elif((i%7) < 4):
        continue
    elif((i%2 == 0) and (i%4)):
        continue
    else:
        print(i,end=' ')