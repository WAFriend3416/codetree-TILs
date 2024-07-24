def sum_evenodd(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    return sum_evenodd(N-2) + N

print(sum_evenodd(int(input())))