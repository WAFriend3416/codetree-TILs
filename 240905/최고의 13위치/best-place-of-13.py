N = int(input())

area = [list(map(int,input().split())) for _ in range(N)]


cur_pos_r,cur_pos_c = 0,0
maxCoin = 0 
for i in range(N):
    for j in range(N):
        cur_pos_r,cur_pos_c = j,i
        cnt = 0
        for k in range(3): # +0, +1 ,+2
            cur_c = cur_pos_c+k
            #print(cur_pos_r,cur_c)
            if cur_c >= N:
                cnt = 0
                break 
            if area[cur_pos_r][cur_c] == 1:
                cnt += 1
        maxCoin = max(maxCoin,cnt)

print(maxCoin)