list = [1,2,3,4,5,6,7]

def revArr(arr, st, e):
    while st < e:
        temp = arr[st]
        arr[st] = arr[e]
        arr[e] = temp

        st += 1
        e -= 1

def right_rotate(arr, d):
    n = len(arr)
    d = d%n
    if d==0:
        return

    revArr(arr, 0, n-1)
    print(arr)
    revArr(arr, 0, d-1)
    print(arr)
    revArr(arr, d, n-1)
    print(arr)

    return arr
    
print(right_rotate(list, 3))