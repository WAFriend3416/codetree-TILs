N = int(input())

people_in_room = []

for _ in range(N):
    people_in_room.append(int(input()))

answer = 10000000
#1번 방부터 최소거리 찾기
for i in range(N):
    total = 0
    for j in range(N):
        cnt = 0
        search_num = i
        while(search_num != j):
            if search_num == 4:
                search_num = 0
            else:
                search_num += 1
            cnt += 1
        total += cnt*people_in_room[j]
        # if i == 1:
        #     print(cnt,people_in_room[j])
    if answer >= total:
        answer = total

print(answer)