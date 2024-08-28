cmd = list(input())

    # E S W N
dx = [1,0,-1,0] 
dy = [0,-1,0,1] 

x,y = 0,0 #원점
cur_x , cur_y = 0,0 #현재위치

#입력 받은 대로 움직이기
stopS = True
cnt = 0
dir_num = 3

for D in cmd:
    if D == 'F': # 직진
        cur_x, cur_y = cur_x + dx[dir_num] , cur_y + dy[dir_num]
        cnt += 1
        if cur_x == x and cur_y == y:
            stopS = False
            break
    elif D == 'L': # 반시계
        dir_num = (dir_num -1 + 3) % 4
        cnt += 1
    elif D == 'R': # 시계
        dir_num = (dir_num + 1) % 4
        cnt += 1
    else:
        print("wrong Input")

if stopS:
    print(cnt)
else:
    print(-1)