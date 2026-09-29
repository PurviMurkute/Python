list = [12, 21, 1, 67, 56, 899, 788, 90, 1000, 10000]

second_largest = list[-1]
largest = list[0]

for i in range(1, len(list)):
    if list[i] > largest:
        largest = list[i]

for i in range(1, len(list)):
    if list[i] > second_largest and list[i] < largest:
        second_largest = list[i]

print("The second largest element in the list is:", second_largest)