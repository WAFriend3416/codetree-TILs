def check_func(num):
    if(num%2 != 0):
        return False
    else:
        if(((num%10) + (num//10))%5 == 0):
            return True
        else:
            return False

n = int(input())

if(check_func(n)):
    print("Yes")
else:
    print("No")