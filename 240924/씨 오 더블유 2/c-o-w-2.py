N = int(input())

COW_list = list(input())

cnt = 0
for i in range(0,N-2):
    if COW_list[i] != 'C':
        continue
    else:
        for j in range(1,N-1):
            if COW_list[j] != 'O':
                continue
            else:
                for k in range(2,N):
                    if COW_list[k] != 'W':
                        continue
                    else:
                        cnt += 1

print(cnt)