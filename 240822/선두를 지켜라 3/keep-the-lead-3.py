MAX_T = 1000000

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
pos_a, pos_b = [0] * (MAX_T + 1), [0] * (MAX_T + 1)

# A가 매 초마다 서있는 위치를 기록
time_a = 1
for _ in range(n):
    v, t = tuple(map(int, input().split()))
    for _ in range(t):
        pos_a[time_a] = pos_a[time_a - 1] + v
        time_a += 1

# B가 매 초마다 서있는 위치를 기록
time_b = 1
for _ in range(m):
    v, t = tuple(map(int, input().split()))
    for _ in range(t):
        pos_b[time_b] = pos_b[time_b - 1] + v
        time_b += 1

# A와 B 중 더 앞서 있는 경우를 확인합니다.
# A가 리더면 1, B가 리더면 2로 관리합니다.
ans = []

for i in range(0, time_a):
    if pos_a[i] > pos_b[i]:
        ans.append('a')
    elif pos_a[i] < pos_b[i]:
        ans.append('b')
    else:
        ans.append('ab')

#print(ans)
cnt = 0
for k in range(1,len(ans)):
    if ans[k-1] != ans[k]:
        cnt += 1

#['b', 'b', 'ab', 'ab', 'a', 'ab', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']

        
print(cnt)