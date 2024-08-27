N,M = map(int,input().split()) # N : row / M : column

area = [
    [0 for _ in range(M)] for _ in range(N)
]

def in_range(x,y):
    if (x >= 0 and x < N) and (y>=0 and y < N):
        return True
    else:
        return False


dx,dy = [0,1,0,-1] , [1,0,-1,0] # R , D , L , U

dir_num = 0 # 진행방향 오른쪽
x,y = 0,0 # 초기 위치

area[x][y] = 1
cnt = 1

for _ in range(0,N):
    for _ in range(0,M):
        if cnt == N*M:
            break
        cur_x , cur_y = x+dx[dir_num] , y+dy[dir_num]
        if in_range(cur_x , cur_y) and area[cur_x][cur_y] == 0:
            cnt += 1
            area[cur_x][cur_y] = cnt
        else:
            dir_num = (dir_num+1) % 4
            cur_x , cur_y = x+dx[dir_num] , y+dy[dir_num]
            # if cnt == 13:
            #     print(cur_x,cur_y,dir_num)
            #     print(area[cur_x][cur_y],cnt)
            # while(area[cur_x][cur_y] != 0):
            #     dir_num = (dir_num+1) % 4
            #     cur_x , cur_y = x+dx[dir_num] , y+dy[dir_num]                
            cnt += 1
            area[cur_x][cur_y] = cnt
        x,y = cur_x , cur_y 

for row in area:
    for item in row:
        print(item,end=' ')
    print()