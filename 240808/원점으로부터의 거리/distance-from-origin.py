class Position:
    def __init__(self,index,x,y,res=0):
        self.index = index
        self.x = x  
        self.y = y
        self.res = res

Poss = []

def cal_distance(x,y):
    return abs(0-x) + abs(0-y)


n = int(input())
for i in range(1,n+1):
    x,y = map(int,input().split())
    postion = Position(i,x,y,cal_distance(x,y))
    Poss.append(postion)

Poss.sort(key=lambda x : x.res)

for postion in Poss:
    print(postion.index)