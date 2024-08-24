x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

N = int(input())

for _ in range(N):
    direction,distance = map(str,input().split())
    distance = int(distance)
    if direction == 'N':
        x, y = x + dx[3]*distance, y + dy[3]*distance
    elif direction == 'S':
        x, y = x + dx[1]*distance, y + dy[1]*distance
    elif direction == 'E':
        x, y = x + dx[0]*distance, y + dy[0]*distance
    else:
        x, y = x + dx[2]*distance, y + dy[2]*distance


print(x,y)