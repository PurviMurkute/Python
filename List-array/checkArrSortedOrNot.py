list = [1, 2, 2, 3, 4, 4, 5]
list2 = [5, 4, 3, 2, 1, 3]

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] <= arr[i + 1]:
            continue
        else:
            return f"The array is not sorted {arr}."
    return f"The array is sorted {arr}."


print(is_sorted(list))
print(is_sorted(list2))