N,M = map(str,input().split())
N = int(N)
CMD = list(input())

    # 주의! 좌표 이동에 따라서 달라질 수 있음.
    # x ,y <-> row, column
    # E S W N
dr = [0,1,0,-1]
dc = [1,0,-1,0]

area = []
for _ in range(N):
    area.append(list(map(int,input().split())))

# 가운데 위치
cur_r,cur_c = N//2,N//2
# 초기 진행 방향 : to N
dir_num = 3 

cnt =  area[cur_r][cur_c]

for item in CMD:
    if item == 'R':
        dir_num = (dir_num+1)%4
        #print(item,dir_num)
    elif item =='L':
        dir_num = (dir_num-1+4)%4
        #print(item,dir_num)
    else:
        r,c = cur_r + dr[dir_num],cur_c + dc[dir_num]
        if r < 0 or r >= N or c < 0 or c >= N:
            continue
        else:
            cur_r,cur_c = cur_r + dr[dir_num],cur_c + dc[dir_num]
            #print(item,area[cur_r][cur_c])
            cnt += area[cur_r][cur_c]

print(cnt)
# while(cnt < total):
#     # for row in area:
#     #     for item in row:
#     #         print(item,end=' ')
#     #     print()
#     # print("==================")


#     r,c = cur_r + dr[dir_num], cur_c + dc[dir_num]
#     if r < 0 or r >= N or c < 0 or c >= M or (area[r][c] != 0):
#         dir_num = (dir_num-1+4)%4
    
#     cnt += 1
#     cur_r,cur_c = cur_r + dr[dir_num], cur_c + dc[dir_num]
#     area[cur_r][cur_c] = cnt






# for row in area:
#     for item in row:
#         print(item,end=' ')
#     print()