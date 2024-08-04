n = int(input())

li = sorted(list(map(int,input().split())))

li_res = []

for i in range(n): # 0,1
    li_res.append(li[i] + li[-(i+1)])

print(max(li_res))