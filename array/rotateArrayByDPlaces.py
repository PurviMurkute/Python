list = [1, 2, 3, 4, 5]

def rotate_array_by_d(arr, d):
    temp = arr[:d]
    for i in range(d, len(arr)):
        arr[i - d] = arr[i]
    for i in range(0, d):
        arr[len(arr) - d + i] = temp[i]
    return arr

print(rotate_array_by_d(list, 2))