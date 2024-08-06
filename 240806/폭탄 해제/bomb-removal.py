class Bomb:
    def __init__(self,code,color,second):
        self.code = code
        self.color = color
        self.second = second

cod,col,sec = map(str,input().split())

bb = Bomb(cod,col,sec)

print("code :",bb.code)
print("color :",bb.color)
print("second :",bb.second)