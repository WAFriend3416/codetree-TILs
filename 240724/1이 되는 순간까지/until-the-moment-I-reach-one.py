def func(N):
    if N == 1:
        return 0
    
    if N % 2 == 0:
        N = N // 2
    else:
        N = N // 3
    
    return func(N) + 1
    

print(func(int(input())))