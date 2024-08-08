class Position:
    def __init__(self,index,x):
        self.index = index
        self.x = x  


Poss = []
Poss_org = []
n = int(input())
li_input = list(map(int,input().split()))

for i in range(n):
    pos_org = Position(i+1,li_input[i])
    Poss_org.append(pos_org)
    position=Position(i+1,li_input[i])
    Poss.append(position)


Poss.sort(key=lambda x : x.x)

for pos in Poss_org:
    cnt = 1
    for pos1 in Poss:
        if pos1.x == pos.x and pos1.index == pos.index:
            #print(pos1.x,pos1.index,pos.x,pos.index)
            print(cnt,end=' ')
            break
        cnt += 1