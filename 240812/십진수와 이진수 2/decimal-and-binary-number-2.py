binary = list(map(int,input()))
num = 0

for i in range(len(binary)):
    num = num * 2 + binary[i]

n = num*17
digits = []
while True:
    if n < 2:
        digits.append(n)
        break

    digits.append(n % 2)
    n //= 2

# print binary number
for digit in digits[::-1]:
    print(digit, end="")