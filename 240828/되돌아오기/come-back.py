N = int(input())


    # E S W N
dx = [1,0,-1,0] 
dy = [0,-1,0,1] 

x,y = 0,0 #원점
cur_x , cur_y = 0,0 #현재위치
move_cmd = []

#이동방향, 이동거리 입력받기
for _ in range(N):
    dircetion,time = map(str,input().split())
    time = int(time)
    cmd = (dircetion,time)
    move_cmd.append(cmd)

#입력 받은 대로 움직이기
stopS = False
cnt = 0
for D,T in move_cmd:
    if stopS:
        break
    else:
        if D == 'E': # 0
            dir_num = 0
        elif D == 'S': # 1
            dir_num = 1
        elif D == 'W': # 2
            dir_num = 2
        elif D == 'N': # 3
            dir_num = 3
        else:
            print("wrong Input")

        for _ in range(T):
            cur_x, cur_y = cur_x + dx[dir_num] , cur_y + dy[dir_num]
            #print(D,cur_x,cur_y)
            cnt += 1
            if cur_x == x and cur_y == y:
                stopS = True
                break

if stopS:
    print(cnt)
else:
    print(-1)