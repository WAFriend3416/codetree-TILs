li = list(input())

cnt = 0
for i in range(len(li)):
    for j in li:
        if i != j:
            cnt += 1

if cnt >= 2:
    print('Yes')
else:
    print('No')