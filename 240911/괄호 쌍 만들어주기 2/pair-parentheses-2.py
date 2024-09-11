li_input = list(input())


cnt = 0
for i in range(1,len(li_input)):
    if li_input[i] == ')':
        continue
    else:
        if li_input[i-1] == '(' and li_input[i] == '(':
            for j in range(i+1,len(li_input)):
                if li_input[j-1] == ')' and li_input[j] == ')':
                    cnt += 1
                else:
                    continue

print(cnt)