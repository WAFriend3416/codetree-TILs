global cnt = 0

def _3n_1(N):
    cnt = cnt + 1
    if N == 1:
        return
    if N % 2 == 0:
        return _3n_1(N//2)
    else:
        return _3n_1((N*3) + 1)

_3n_1(int(input()))
print(cnt)