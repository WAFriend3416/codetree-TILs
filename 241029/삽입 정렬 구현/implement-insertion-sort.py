def insertion_sort(arr):
    size = len(arr)
    for i in range(1, size):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 테스트
n = int(input())
arr = list(map(int,input().split()))
sorted_arr = insertion_sort(arr)
for i in arr:
    print(i,end=' ')