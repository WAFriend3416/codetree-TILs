# A : 65

n = int(input())

cnt = 0
asci = 65

for i in range(n):
    for j in range(0,cnt):
        print(' ',end=' ')
    for k in range(n-cnt):
        print(chr(asci),end=' ')
        if asci == 90:
            asci = 65
        else:
            asci = asci + 1
    cnt = cnt + 1
    print()