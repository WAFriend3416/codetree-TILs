# 클래스 생성
class WeatherData:
    def __init__(self,date,days,weather):
        self.date = date
        self.days = days
        self.weather = weather

# n개의 데이터 받기
n = int(input())
Dataset = []
Dataset_rain = []
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
end_date = "2100-12-31"

for _ in range(n):
    date,days,weather = map(str,input().split())
    for i in range(7):
        if days_of_week[i] == days:
            days = i
            break
    Dataset.append(WeatherData(date,days,weather))

# 가장 근 시일내에 비가 오는 날 찾기
for i in range(n):
    if Dataset[i].weather == "Rain":
        Dataset_rain.append(Dataset[i])

li = sorted(Dataset_rain,key=lambda x: x.date)

li_days = []

for i in range(0,len(li)):
    for j in range(i,len(li)):
        if li[i].date == li[j].date:
            li_days.append(li[i])

li_days = sorted(li_days,key=lambda x: x.days)


print(li_days[0].date,days_of_week[li_days[0].days],li_days[0].weather)