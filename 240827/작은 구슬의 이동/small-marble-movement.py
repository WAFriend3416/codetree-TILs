x,y = 0,0 #초기위치
dx,dy = [0, 0, -1, 1],[-1, 1, 0, 0] # L, R, U, D

def in_range(x,y):
    if (x < N and x >= 0) and (y < N and y >=0 ):
        return True
    else:
        return False

N,t = map(int,input().split())

area = [
    [0 for _ in range(N)] for _ in range(N) 
]

nx,ny,D = map(str,input().split())
x,y = int(nx)-1,int(ny)-1

#print('strat:',x,y,D)

for i in range(t):
    if D =='L': 
        cur_x ,cur_y =x+dx[0],y+dy[0]
        if in_range(cur_x ,cur_y):
            x,y = cur_x ,cur_y
        else:
            D = 'R'
    elif D == 'R': 
        cur_x ,cur_y =x+dx[1],y+dy[1]
        if in_range(cur_x ,cur_y):
            x,y = cur_x ,cur_y
        else:
            D = 'L'

    elif D =='U': 
        cur_x ,cur_y =x+dx[2],y+dy[2]
        if in_range(cur_x ,cur_y):
            x,y = cur_x ,cur_y
        else:
            D = 'D'
    elif D =='D': 
        cur_x ,cur_y =x+dx[3],y+dy[3]
        if in_range(cur_x ,cur_y):
            x,y = cur_x ,cur_y
        else:
            D = 'U'
    #print(f'step:{i}',x,y,D)

print(x+1,y+1)