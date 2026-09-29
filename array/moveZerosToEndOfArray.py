list = [2, 3, 4, 0, 0, 5, 0, 1, 0]

def move_zeros_to_end(arr):
    n = len(arr)
    j = -1
    for i in range(n):
        if arr[i] == 0:
            j = i
            break
    for i in range(j+1, n):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    return arr

print(move_zeros_to_end(list))  # Output: [2, 3, 4, 5, 1, 0, 0, 0, 0]