friends = ["Apple", "Banana", "Cherry", 3, False, "Date", "Elderberry"]

print(friends[0])  # Output: Apple

print(friends[2:4])

friends[1] = "Blueberry"  # Change Banana to Blueberry

print(friends)  # Output: ['Apple', 'Blueberry', 'Cherry', 3, False, 'Date', 'Elderberry']

l1 = [1, 67, 87, 6, 34, 23, 45, 90]

l1.sort()
print(l1)

""" l1.reverse()
print(l1) """

l1.append(100)
print(l1)

l1.insert(2, 200)  # Insert 200 at index 2
print(l1)

print(l1.pop())

l1.remove(6)
print(l1)  # Remove the first occurrence of 6