N = int(input())
li = list(map(int,input().split()))

cnt =0 
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if li[i] <= li[j] and li[j] <= li[k]:
                cnt += 1

print(cnt)