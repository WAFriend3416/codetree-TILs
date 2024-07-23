def printNum_rec(N):
    if N == 0:
        return
    
    print(N,end=' ')
    printNum_rec(N-1)
    print(N,end=' ')

printNum_rec(int(input()))