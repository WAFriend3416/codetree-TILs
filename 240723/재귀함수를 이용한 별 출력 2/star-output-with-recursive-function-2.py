def printStar_rec(N):
    if N == 0:
        return
    
    print("* "*N)
    printStar_rec(N-1)
    print("* "*N)

printStar_rec(int(input()))