class command:
    def __init__(self,code,place,time):
        self.code = code
        self.place = place
        self.time = time

code , place , time = map(str,input().split())
command1 = command(code,place,time)

print("secret code :",command1.code)
print("meeting point :",command1.place)
print("time :",command1.time)