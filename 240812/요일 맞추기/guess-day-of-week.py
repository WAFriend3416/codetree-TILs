#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
list_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

m1,d1,m2,d2 = map(int,input().split())

num1 = 0
num2 = 0

cnt = 0
while(cnt != m1):
    num1 += num_of_days[cnt]
    cnt += 1
num1 += d1

cnt = 0
while(cnt != m2):
    num2 += num_of_days[cnt]
    cnt += 1
num2 += d2

if num1 == num2:
    print('Mon')
# elif num1 > num2:
#     print(list_days[(num2-num1)%7])
else:
    print(list_days[(num2-num1)%7])