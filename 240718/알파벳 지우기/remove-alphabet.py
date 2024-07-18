n1 = list(input())
n2 = list(input())

total = 0
number = []
for i in n1:
    if i.isdigit():
        number.append(i)
number = ''.join(number)
total = total + int(number)

number = []
for i in n2:
    if i.isdigit():
        number.append(i)

number = ''.join(number)
total = total + int(number)

print(total)