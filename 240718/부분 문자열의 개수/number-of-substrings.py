n = input()
n1 = input()
cnt = 0
for i in range(0,len(n)-1):
    #print(n[i:i+2],n1)
    if n[i:i+2] == n1:
        cnt = cnt + 1

print(cnt)