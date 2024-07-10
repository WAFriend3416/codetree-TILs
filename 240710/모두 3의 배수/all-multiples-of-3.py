total = 0
for i in range(5):
    n = int(input())
    total = total + n

if(total%3):
    print(0)
else:
    print(1)