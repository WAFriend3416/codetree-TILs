OFFSET = 1000

N,M = map(int,input().split())

A = [0] * (2 * OFFSET + 1)
B = [0] * (2 * OFFSET + 1)

cur = 1000
cnt = 0
for _ in range(N):
    direction, x = map(str,input().split())
    x = int(x)
    if direction == 'L':
        while x >= 1:
            A[cnt] = cur
            cur -= 1
            cnt += 1
            x -= 1
    else:
        while x >= 1:
            A[cnt] = cur
            cur += 1
            cnt += 1
            x -= 1


cur = 1000
cnt = 0
for _ in range(M):
    direction, x = map(str,input().split())
    x = int(x)
    if direction == 'L':
        while x >= 1:
            B[cnt] = cur
            cur -= 1
            cnt += 1
            x -= 1
    else:
        while x >= 1:
            B[cnt] = cur
            cur += 1
            cnt += 1
            x -= 1
# [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1008, 1007, 1006, 1007, 1008, 1009, 1010,
# [1000, 999, 998, 999, 1000, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010,
# print(A[:20])
# print(B[:20])
for i in range(1,2002):
    if A[i] == B[i]:
        print(i)
        break