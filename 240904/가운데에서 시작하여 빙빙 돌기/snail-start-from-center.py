N = int(input())

    # 주의! 좌표 이동에 따라서 달라질 수 있음.
    # x ,y <-> row, column
    # E S W N
dr = [0,1,0,-1]
dc = [1,0,-1,0]

area = [
    [0 for _ in range(N)] for _ in range(N)
]

total = N * N

r, c = N-1,N-1
dir_num = 2 # to W

cnt = total
area[r][c] = total
cur_r,cur_c = N-1,N-1


while(cnt > 1):
    # for row in area:
    #     for item in row:
    #         print(item,end=' ')
    #     print()
    # print("==================")


    r,c = cur_r + dr[dir_num], cur_c + dc[dir_num]
    if r < 0 or r >= N or c < 0 or c >= N or (area[r][c] != 0):
        dir_num = (dir_num+1)%4
    
    cnt -= 1
    cur_r,cur_c = cur_r + dr[dir_num], cur_c + dc[dir_num]
    area[cur_r][cur_c] = cnt


for row in area:
    for item in row:
        print(item,end=' ')
    print()