n = int(input())

li_in = list(map(int,input().split()))
li_item = []
li_result = []

for i in range(0,n):
    li_item.append(li_in[i])
    if i%2 == 0:
        index = ((0+i)//2)
        li_result.append(sorted(li_item)[index])

for item in li_result:
    print(item,end=' ')