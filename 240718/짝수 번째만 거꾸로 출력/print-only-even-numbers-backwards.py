n = input()
li = []

for i in range(len(n)):
    if (i+1)%2 == 0:
        li.append(n[i])

for i in range(len(li)-1,-1,-1):
    print(li[i],end='')