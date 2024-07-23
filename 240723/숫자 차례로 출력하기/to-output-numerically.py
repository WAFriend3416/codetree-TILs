def printNum_a(N):
    if N == 0:
        return
    
    printNum_a(N-1)
    print(N,end=' ')
    #printNum(N-1)

def printNum_d(N):
    if N == 0:
        return
    
    #printNum(N-1)
    print(N,end=' ')
    printNum_d(N-1)

a = int(input())

printNum_a(a)
print()
printNum_d(a)