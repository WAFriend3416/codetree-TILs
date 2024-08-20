n = int(input())
li = [int(input()) for _ in range(n)]
li_cnt = []
cnt = 0
for i in range(n):
    if i == 0 or li[i] == li[i-1]:
        cnt += 1
    else: 
        li_cnt.append(cnt)

print(max(li_cnt))