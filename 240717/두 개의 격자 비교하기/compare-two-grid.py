matr1 = []
matr2 = []
matr3 = []

n,m = map(int,input().split())

for i in range(n):
    li = []
    li = list(map(int,input().split()))
    matr1.append(li)

for j in range(n):
    li = []
    li = list(map(int,input().split()))
    matr2.append(li)

for t in range(0,n):
    row = []
    for k in range(0,m):
        if matr1[t][k] == matr2[t][k]:
            row.append(0)    
        else:
            row.append(1)
    matr3.append(row)
i=0
j=0
for i in range(0,n):
    for j in range(0,m):
        print(matr3[i][j],end=' ')
    print()