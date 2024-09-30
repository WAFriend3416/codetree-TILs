N,K = map(int,input().split())

li = [0 for _ in range(10001)]

for _ in range(N):
    pos, letter = map(str,input().split())
    li[int(pos)] = letter

result = 0
for i in range(1,len(li)-K):
    comp = 0
    for j in range(i,i+K+1):        
        #print(i,i+k)
        if li[j] == 'G':
            #print('g')
            comp += 1
        elif li[j] == 'H':
            #print('h')
            comp += 2
        else:
            continue
    #print("aaaaaaaaaaaaaaaaaaaaaaaaaaa")
    result = max(result,comp)

print(result)