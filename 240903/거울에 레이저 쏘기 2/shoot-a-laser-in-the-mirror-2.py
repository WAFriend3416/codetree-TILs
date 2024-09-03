def in_Range(x,y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    else:
        return True

area = []
    # E S W N
dx = [0,1,-1,0] 
dy = [1,0,0,-1] 
dir_num = 0
N = int(input())


startPos = []
for i in range(0,N):
    startPos.append([0,i])
for j in range(0,N):
    startPos.append([j,N-1])
for k in range(N-1,-1,-1):
    startPos.append([N-1,k])
for m in range(N-1,-1,-1):
    startPos.append([m,0])

for _ in range(N):
    area.append(list(input()))

in_R = int(input()) # 시작지점

if (in_R // N) == 0:
    dir_num =  1# to S
elif (in_R // N) == 1:
    dir_num =  2# to W
elif (in_R // N) == 2:
    dir_num =  3# to N
else:
    dir_num =  0# to E

curPos_x,curPos_y = startPos[in_R-1][0],startPos[in_R-1][1]
cnt = 0
#print(curPos_x,curPos_y,dir_num)
while(in_Range(curPos_x,curPos_y)):
    #print(area[curPos_x][curPos_y])
    if area[curPos_x][curPos_y] == '/':
        if dir_num == 2 or dir_num == 0: # to W || to E 시계
            dir_num = (dir_num+1)%4
        else: #dir_num == 3 or dir_num == 1 to N || to S 반시계
            dir_num = (dir_num-1+3)%4
    else: #area[curPos[0]][curPos[1]] == '\\':
        if dir_num == 1 or dir_num == 3: # to W || to E
            dir_num = (dir_num-1+3)%4
        else: #dir_num == 3 or dir_num == 1 to N || to S
            dir_num = (dir_num+1)%4
    cnt += 1
    curPos_x,curPos_y = curPos_x + dx[dir_num],curPos_y+dy[dir_num]
    #print(curPos_x,curPos_y)
print(cnt)