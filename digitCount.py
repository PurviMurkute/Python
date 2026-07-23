num = int(input("Enter a number: "))

print(num // 10)
print(len(str(num)))

count = 0
if len(str(num)) == 1:
    count = num

else:
    while num > 0:
        last = num % 10
        count += last
        num = num // 10

print("Number of digits:", count)