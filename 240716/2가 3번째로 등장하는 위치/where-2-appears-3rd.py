n = int(input())
li = list(map(int,input().split()))
index = 0
cnt = 0
for i in range(n):
    if li[i] == 2:
        cnt = cnt + 1
    if cnt == 3:
        print(i+1)
        break