def cal_min(DAY,HOUR,MIN):
    DAY = (day - 11) * 24 * 60
    HOUR = (hour - 11) * 60
    MIN = mint - 11

    print(DAY + HOUR + MIN)

day,hour,mint = map(int,input().split())

if day < 11:
    print(-1)
else:
    if hour < 11:
        print(-1)
    else:
        if hour >= 11 and mint < 11:
            print(-1)

        else:
            cal_min(day,hour,mint)