a,b,c = map(int,input().split())

li = [0] * a
li_in = []

for _ in range(b):
    li_in.append(int(input()))

for i in li_in:
    li[i-1] += 1
    if li[i-1] == 3:
        print(li.index(li[i]))
        break