arr = [1, 2, 2, 1, 1, 2, 3, 2, 3, 3]

arr.sort()

i = 0

for j in range(1, len(arr)):
    if arr[i] != arr[j]:
        i += 1
        arr[i] = arr[j]

arr = arr[:i+1]

print(arr)