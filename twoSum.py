arr = [2, 3, 5, 7, 11]

def two_sum(arr, target):
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return [i, j]
        
    return None

print(two_sum(arr, 10))  # Output: [0, 3] (2 + 7 = 9)