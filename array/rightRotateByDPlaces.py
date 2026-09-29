list = [1, 2, 3, 4, 5]

def right_rotate(arr, d):
    n = len(arr)
    d = d % n  # Handle cases where d is greater than n
    temp = arr[n-d:n]  # Store the last d elements
    for i in range(d, n):
        arr[i] = arr[i+d+1]
    for i in range(0, d):
        arr[i] = temp[i]
    return arr

print(right_rotate(list, 2))  # Output: [6, 7]