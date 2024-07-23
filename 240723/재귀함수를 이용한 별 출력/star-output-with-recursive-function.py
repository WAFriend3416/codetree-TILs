def printStar(N):
    if N == 0:
        return
    printStar(N-1)
    print('*'*N)

n = int(input())

printStar(n)