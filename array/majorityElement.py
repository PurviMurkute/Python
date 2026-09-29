list = [1, 1, 2, 1, 3, 5, 1]

print(7//2)

def majorityEle(arr):
    n = len(arr)
    seen = {}
    uniqueArr = set(arr)

    for i in range(n):
        if arr[i] in seen:
            seen[arr[i]] += 1
        else:
            seen[arr[i]] = 1

    for num in uniqueArr:
        if seen[num] > n//2:
            return num
    return -1

print(majorityEle(list))