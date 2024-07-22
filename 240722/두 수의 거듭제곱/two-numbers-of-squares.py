def return_square_value(a,b):
    result = 1
    for _ in range(b):
        result *= a
    return result

n,m = map(int,input().split())

print(return_square_value(n,m))