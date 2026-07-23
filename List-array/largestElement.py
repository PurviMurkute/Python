list = [3, 78, 45, 90, 23, 67, 12, 111, 1111, 111111, 2222222222]

largest = list[0]
for i in range(1, len(list)):
    if list[i] > largest:
        largest = list[i]

print("The largest element in the list is:", largest)