def print_matrx(n):
    cnt = 1
    for _ in range(n):
        for _ in range(n):
            if(cnt > 9):
                cnt = 1
                print(cnt,end=' ')
                cnt = cnt + 1
            else:
                print(cnt,end=' ')
                cnt = cnt + 1
        print()

n = int(input())

print_matrx(n)