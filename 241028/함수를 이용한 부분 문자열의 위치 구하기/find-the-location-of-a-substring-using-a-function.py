word = list(input())
target = list(input())

check = True

for i in range(len(word)-len(target)+1):
    cnt = 0
    for j in range(len(target)):
        #print(word[i+j],target[j])
        #print((word[i+j] == target[j]))
        if word[i+j] == target[j]:
            cnt += 1
    #print(cnt)
    if cnt == len(target):
        check = False
        break

if check:
    print(-1)
else:
    print(i)