li_input = list(input())



cnt = 0
for i in range(0,len(li_input)):
    if li_input[i] == ')':
        continue
    else:
        for j in range(i+1,len(li_input)):
            if li_input[j] == '(':
                continue
            else:
                #print(i,j)
                cnt +=1

print(cnt)