n,m = map(int,input().split()) # n: 격자 크기 m:점의 개수
li = []

answer  =[
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    li.append(list(map(int,input().split())))

for row in li:
    answer[row[0]-1][row[1]-1] = row[0]*row[1]

for row in answer:
    for item in row:
        print(item,end=' ')
    print()