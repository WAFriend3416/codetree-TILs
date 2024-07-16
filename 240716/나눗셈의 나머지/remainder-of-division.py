a,b = map(int,input().split())
li = []

while(a>1):
    mod_v = a%b
    li.append(mod_v)
    a = a//b

li_set = list(set(li))

sum = 0

for j in li_set:
    cnt = li.count(j)
    sum = sum + (cnt * cnt)

print(sum)