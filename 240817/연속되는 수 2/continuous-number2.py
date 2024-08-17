def find_max_consecutive(numbers):
    if not numbers:
        return 0
    
    max_count = 1
    current_count = 1
    
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i-1]:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 1
    
    return max_count

# 입력 받기
input_numbers = []
n = int(input())
for _ in range(n):
    input_numbers.append(int(input()))

# 결과 출력
print(find_max_consecutive(input_numbers))