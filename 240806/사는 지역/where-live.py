class Person:
    def __init__(self,name,addr,postion):
        self.name = name
        self.addr = addr
        self.postion = postion
    
n = int(input())


People = []
peo_search = []

for _ in range(n):
    name,addr,postion = map(str,input().split())
    People.append(Person(name,addr,postion))
    peo_search.append(name)

peo_search = sorted(peo_search)

for i  in range(n):
    if peo_search[n-1] == People[i].name:
        print("name",People[i].name)
        print("addr",People[i].addr)
        print("city",People[i].postion)
        break