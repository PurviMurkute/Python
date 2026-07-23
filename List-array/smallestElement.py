list = [12, 21, 1, 67, 56, 899, 788, 90, 0, 1000, 10000]

smallest = list[0]

for i in range(1, len(list)):
    if list[i] < smallest:
        smallest = list[i]

print("The smallest element in the list is:", smallest)