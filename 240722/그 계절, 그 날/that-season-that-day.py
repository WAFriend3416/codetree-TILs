#1. 윤년 판단(연도)
def check_year(n):
    if n%4 != 0:
        return False
    elif n%100 == 0 and n%400 != 0:
        return False
    else:
        return True

#2. 날짜 존재여부 판단(윤년 여부, 월, 달)
def check_date(cnt,M,D):
    if cnt:
        li_d = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        li_d = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    if D >= 1 and D <= li_d[M]:
        return True
    else:
        return False
    

#3. 계절 판단
def check_season(M):
    if M >= 3 and M <= 5:
        return "Spring"
    elif M >= 6 and M <= 8:
        return "Summer"
    elif M >= 9 and M <= 11:
        return "Fall"
    else:
        return "Winter"


cnt = False # 윤년 여부 True : 윤년 / False : 평년
isDate = False # 날짜 존재여부 True : 있음 / False : 없음

Y,M,D = map(int,input().split())

cnt = check_year(Y)
isDate = check_date(cnt,M,D)

if isDate:
    print(check_season(M))
else:
    print(-1)