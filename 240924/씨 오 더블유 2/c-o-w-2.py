N = int(input())

COW_list = list(input())

cnt = 0
for i in range(0,N-2):
    if COW_list[i] != 'C':
        continue
    else:
        for j in range(i,N-1):
            if COW_list[j] != 'O':
                continue
            else:
                for k in range(j,N):
                    if COW_list[k] != 'W':
                        continue
                    else:
                        if COW_list[i] == 'C' and COW_list[j] == 'O' and COW_list[k] == 'W':
                            #print(i,j,k)
                            cnt += 1

print(cnt)