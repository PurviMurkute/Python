list = [3, 3, 3, 3, 3, 6]

def remove_duplicates(arr):
    i = 1 # unique length
    for j in range(1, len(arr)):
        if arr[j] != arr[j-1]:
            arr[i] = arr[j]
            i += 1

    return i, arr

print(remove_duplicates(list))