def check_dateIn2012(M,D):
    if M == 2:
        if D >= 1 and D <= 28:
            return True
        else:
            return False
    else:
        if M % 2 ==0 and M < 13:
            if D >= 1 and D <= 30:
                return True
        elif M % 2 and M < 13:
            if D >= 1 and D <= 31:
                return True
        else:
            return False

m,d = map(int,input().split())

if check_dateIn2012(m,d):
    print("Yes")
else:
    print("No")