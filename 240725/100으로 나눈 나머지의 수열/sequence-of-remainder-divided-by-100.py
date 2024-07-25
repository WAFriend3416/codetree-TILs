n = int(input())
cnt = 1

def dvi100(N):
    if N == 1:
        return 2
    elif N == 2:
        return 4
    else:
        return (dvi100(N-2)*dvi100(N-1)) % 100

print(dvi100(n))