def square(N):
    if N < 10:
        return N**2
    
    return square(N//10) + (N%10)**2

print(square(int(input())))