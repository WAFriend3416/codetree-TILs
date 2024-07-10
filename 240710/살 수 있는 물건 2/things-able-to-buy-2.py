n = int(input())

if(n < 500):
    print('no')
elif(n >= 500 and n < 1000):
    print('pen')
elif(n >= 1000 and n < 3000):
    print('mask')
else:
    print('book')