def check_list(n,m):
    for i in range(0,n-m+1):
        if li1[i:i+m] == li2:
            return True
    return False
    

n,m = map(int,input().split())

li1 = list(map(int,input().split()))
li2 = list(map(int,input().split()))

if check_list(n,m):
    print('Yes')
else:
    print('No')