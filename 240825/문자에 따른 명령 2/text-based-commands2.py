rotate_cmd = list(map(str,input()))

x,y = 0,0

dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
# E, W , S , N

dir_num = 3

for direction in rotate_cmd:
    if direction == 'L': # 반시계방향
        dir_num = (dir_num-1 + 4) % 4
        print(dir_num)
    elif direction == 'R': # 시계방향
        dir_num = (dir_num+1) % 4
    else: # direction == 'F'
        x,y = x+dx[dir_num] , y+dy[dir_num]

print(x,y)


# move
nx, ny = x + dx[dir_num], y + dy[dir_num]