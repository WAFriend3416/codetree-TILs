def printHW(n):
    if n == 0:
        return
    
    printHW(n-1)
    print("HelloWorld")

n = int(input())

printHW(n)