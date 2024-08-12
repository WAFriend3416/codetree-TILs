n,m = map(int,input().split())
binary = list(map(int,input()))
num = 0

for i in range(len(binary)):
    num = num * n + binary[i]
##

n = num
digits = []
while True:
    if n < m:
        digits.append(n)
        break

    digits.append(n % m)
    n //= m

# print binary number
for digit in digits[::-1]:
    print(digit, end="")