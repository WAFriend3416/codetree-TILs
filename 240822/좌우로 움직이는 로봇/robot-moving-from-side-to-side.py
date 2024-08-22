def simulate_movement(moves):
    path = [100]  # Start at position 100000
    for x , direction in moves:
        if direction == 'L':
            path.extend(range(path[-1] - 1, path[-1] - x - 1, -1))
        else:  # direction == 'R'
            path.extend(range(path[-1] + 1, path[-1] + x + 1))
    return path

def find_meeting_point(path_a, path_b):
    cnt = 0
    if len(path_a) > len(path_b):
        small_li = 'b'
        small = len(path_b)
        big_li = 'a'
        big = len(path_a)
    else:
        small_li = 'a'
        small = len(path_a)
        big_li = 'b'
        big = len(path_b)
    
    for i in range(1, small):
        if (path_a[i-1] != path_b[i-1]) and (path_a[i] == path_b[i]):
            #print(i,path_a[i],path_b[i])
            cnt += 1
    
    for j in range(small,big):
        if small_li == 'a':
            if (path_a[small-1] == path_b[j]):
                #print(i,path_a[small-1],path_b[j])
                cnt += 1
        else:
            if (path_b[small-1] == path_a[j]):
                #print(i,path_a[j],path_b[small-1])
                cnt += 1
    return cnt

# Read input
N, M = map(int, input().split())

# Read moves for A and B
moves_a = [input().split() for _ in range(N)]
moves_b = [input().split() for _ in range(M)]

# Convert string numbers to integers
moves_a = [(int(x), d) for x, d in moves_a]
moves_b = [(int(x), d) for x, d in moves_b]

# Simulate movements
path_a = simulate_movement(moves_a)
path_b = simulate_movement(moves_b)

#print(path_a)
#print(path_b)
# Find meeting point
result = find_meeting_point(path_a, path_b)
print(result)

#[100, 99, 98, 97, 98, 99, 100, 101, 102, 101, 102, 103]
#[100, 101, 102, 103, 104, 103, 102, 101, 100, 101, 102, 103, 104, 103, 102]