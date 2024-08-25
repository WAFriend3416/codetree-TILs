rotate_cmd = list(map(str,input()))

x,y = 0,0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
    # E, S, W, N

dir_num = 3

for direction in rotate_cmd:
    if direction == 'L': # 반시계방향
        dir_num = (dir_num-1 + 4) % 4
    elif direction == 'R': # 시계방향
        dir_num = (dir_num+1) % 4
    else: # direction == 'F'
        x,y = x+dx[dir_num] , y+dy[dir_num]

print(x,y)