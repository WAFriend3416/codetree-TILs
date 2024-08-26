x,y = 0,0 #초기위치
dx,dy = [1, 0, -1, 0],[0, -1, 0, 1] # E , S , W, N

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
y,x = int(nx)-1,int(ny)-1

#print(x,y,D)

for _ in range(t):
    if D =='L': # W
        cur_x ,cur_y =x+dx[2],y+dy[2]
        if in_range(cur_x ,cur_y):
            x,y = cur_x ,cur_y
        else:
            D = 'R'
    elif D == 'R': # E
        cur_x ,cur_y =x+dx[0],y+dy[0]
        if in_range(cur_x ,cur_y):
            x,y = cur_x ,cur_y
        else:
            D = 'L'

    elif D =='U': # N
        cur_x ,cur_y =x+dx[3],y+dy[3]
        if in_range(cur_x ,cur_y):
            x,y = cur_x ,cur_y
        else:
            D = 'D'
    elif D =='D': # S
        cur_x ,cur_y =x+dx[1],y+dy[1]
        if in_range(cur_x ,cur_y):
            x,y = cur_x ,cur_y
        else:
            D = 'U'
    #print(x,y,D)

print(y+1,x+1)