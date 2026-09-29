list = [12, 21, 1, 1, 67, 56, 899, 788, 90, 0, 0, 1000, 10000]

second_smallest = list[-1]
smallest = list[0]

for i in range(1, len(list)):
    if list[i] < smallest:
        smallest = list[i]

for i in range(1, len(list)):
    if list[i] < second_smallest and list[i] > smallest:
        second_smallest = list[i]

print("The second smallest element in the list is:", second_smallest)