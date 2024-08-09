#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

li = list(map(int,input().split()))

days = 0
for i in range(li[0],li[2]):
    days += num_of_days[i]

print(days - li[1] + li[3]+1)