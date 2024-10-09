N = int(input())

li = []

for _ in range(N):
    command = input()
    cmd = command.split()[0]
    if cmd =='push_back':
        number = command.split()[1]
        number = int(number)
        li.append(number)
    elif cmd =='pop_back':
        li.pop()
    elif cmd =='get':
        number = command.split()[1]
        number = int(number)
        print(li[number-1])
    elif cmd =='size':
        print(len(li))
    else:
        print('wrong input')