list = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 6, 6, 7]

def remove_duplicates(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            arr[i + 1] = arr[j]
            i += 1

    return (i+1, arr[:i + 1])  # arr[:i + 1] = arr[0 : i + 1] returns the unique elements in the array


print(remove_duplicates(list))