list = [1, 2, 3, 4, 5]

def rotate_array_by_one(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
    arr[-1] = temp
    return arr

print(rotate_array_by_one(list))