def in_Range(x,y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    else:
        return True

area = []
    # E S W N
dx = [0,1,0,-1] 
dy = [1,0,-1,0] 
dir_num = 0
N = int(input())


startPos = []
for i in range(0,N):
    startPos.append([0,i,1])
for j in range(0,N):
    startPos.append([j,N-1,2])
for k in range(N-1,-1,-1):
    startPos.append([N-1,k,3])
for m in range(N-1,-1,-1):
    startPos.append([m,0,0])

for _ in range(N):
    area.append(list(input()))

in_R = int(input()) # 시작지점

curPos_x,curPos_y = startPos[in_R-1][0],startPos[in_R-1][1]
dir_num = startPos[in_R-1][2]
cnt = 0
#print(curPos_x,curPos_y,dir_num)
while(in_Range(curPos_x,curPos_y)):
    #print(area[curPos_x][curPos_y])
    if area[curPos_x][curPos_y] == '/':
        if dir_num == 2 or dir_num == 0: # to W || to E 시계
            dir_num = (dir_num-1+4)%4
        else: #dir_num == 3 or dir_num == 1 to N || to S 반시계
            dir_num = (dir_num+1)%4
    else: #area[curPos[0]][curPos[1]] == '\\':
        if dir_num == 1 or dir_num == 3: # to W || to E
            dir_num = (dir_num-1+4)%4
        else: #dir_num == 3 or dir_num == 1 to N || to S
            dir_num = (dir_num+1)%4
    cnt += 1
    curPos_x,curPos_y = curPos_x + dx[dir_num],curPos_y+dy[dir_num]
    #print("dir_num : ",dir_num)
    #print(curPos_x,curPos_y)
    #print("==========")

print(cnt)