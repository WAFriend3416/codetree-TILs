SIZE = int(input())

matrix = []

def in_ranged(dx,dy):
    if (dx >= 0 and dx < SIZE) and (dy >= 0 and dy < SIZE):
        return True # in matrix
    else:
        return False # not in matrix


for _ in range(SIZE):
    matrix.append(list(map(int,input().split())))

x,y = 0,0
cnt = 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1] 
    # E, S, W, N  시계방향

for i in range(SIZE):
    for j in range(SIZE):
        cnt_in = 0
        for k in range(4):
            if in_ranged(i+dx[k],j+dy[k]) and matrix[i+dx[k]][j+dy[k]]:
                cnt_in += 1
        if cnt_in >= 3:
            cnt += 1
print(cnt)