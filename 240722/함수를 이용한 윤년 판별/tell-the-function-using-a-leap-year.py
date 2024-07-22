def check_year(n):
    if n%4 != 0:
        return False
    elif n%100 == 0 and n%400 != 0:
        return False
    else:
        return True

num = int(input())

if(check_year(num)):
    print("true")
else:
    print("false")