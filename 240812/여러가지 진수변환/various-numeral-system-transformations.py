n,m = map(int,input().split())
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