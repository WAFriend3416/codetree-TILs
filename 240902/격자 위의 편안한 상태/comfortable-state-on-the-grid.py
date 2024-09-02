# E S W N
dx = [1,0,-1,0] 
dy = [0,-1,0,1] 

x,y = 0,0 #원점
cur_x , cur_y = 0,0 #현재위치

N,M = map(int,input().split())

area = [
    [0 for _ in range(N)] for _ in range(N)
]

def check_comfortable(x,y):
    area[x][y] = 1
    cnt = 0
    for i in range(4):
        cur_x = x + dx[i]
        cur_y = y + dy[i]
        if cur_x < 0 or cur_x >= N or cur_y < 0 or cur_y >= N:
            continue
        else:
            if area[cur_x][cur_y] == 1:
                cnt += 1
    if cnt >= 3:
        return True
    else:
        return False

for _ in range(M):
    x_pos,y_pos = map(int,input().split())
    if check_comfortable(x_pos-1,y_pos-1):
        print(1)
    else:
        print(0)