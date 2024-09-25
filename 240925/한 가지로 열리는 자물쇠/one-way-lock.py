N = int(input())
lockNumber = list(map(int,input().split()))

cnt = N*N*N

for i in range(1,N+1):
    for j in range(1,N+1):
            for k in range(1,N+1):
                if (abs(k-lockNumber[2]) > 2) and (abs(i-lockNumber[0]) > 2) and (abs(j-lockNumber[1]) > 2):
                    #print(i,j,k)
                    cnt -= 1

print(cnt)