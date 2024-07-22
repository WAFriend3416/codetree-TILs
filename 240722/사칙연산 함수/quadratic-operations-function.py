def calculator(li):
    lis = li
    lis[0] = int(lis[0])
    lis[2] = int(lis[2])
    
    if lis[1] == '+':
        return lis[0] + lis[2]
    elif lis[1] == '-':
        return lis[0] - lis[2]
    elif lis[1] == '/':
        return int(lis[0] / lis[2])
    elif lis[1] == '*':
        return lis[0] * lis[2]
    else:
        return 'False'
        
li = list(map(str,input().split()))


if calculator(li) == 'False':
    print('False')
else:
    print(li[0],li[1],li[2],'=',calculator(li))