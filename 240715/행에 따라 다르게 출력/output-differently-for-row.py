n = int(input())
cnt = 0 
for i in range(1,n+1):
    for j in range(n):
        if i %2 ==0: # 짝수
            cnt = cnt + 2
        else: # 홀수
            cnt = cnt + 1
        print(cnt,end=' ')

    print()