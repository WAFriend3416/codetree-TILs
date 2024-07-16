n = int(input())
li = list(map(int,input().split()))

minV = 1

for i in range(0,n):
    for j in range(i,n):
        if li[i] == li[j]:
            continue
        #print(li[i],li[j])
        #print(abs(li[i]-li[j]))
        if abs(li[i]-li[j]) <= minV:
            minV = abs(li[i]-li[j])

print(minV)