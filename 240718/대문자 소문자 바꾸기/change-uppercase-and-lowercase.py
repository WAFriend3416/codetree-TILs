n = list(input())

for i in range(len(n)):
    if ord(n[i]) >= 97 and ord(n[i]) <= 122: #소문자
        n[i] = chr(ord(n[i])-32)
    else:
        n[i] = chr(ord(n[i])+32)

n = ''.join(n)

print(n)