arr = []
total = 0.0
cnt = int(input())
cnt2 = 0

for _ in range(cnt):
    n = list(input())
    arr.append(n)

key = input() 

for row in arr:
    if row[0] == key:       
        cnt2 = cnt2 + 1
        total = total + len(row)

avr = total/cnt2

print(f'{cnt2}',end=' ')
print(f'{avr:.2f}')