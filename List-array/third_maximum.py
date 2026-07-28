nums = [1, 2, 2, 5, 3, 5]

def third_maximum(nums):
    n = len(nums)

    max_num = float('-inf')
    second_max = float('-inf')
    third_max = float('-inf')

    # Find maximum
    for i in range(n):
        if nums[i] > max_num:
            max_num = nums[i]

    print("The maximum element in the list is:", max_num)

    # Find second distinct maximum
    for i in range(n):
        if nums[i] != max_num and nums[i] > second_max:
            second_max = nums[i]

    print("The second maximum element in the list is:", second_max)

    # Find third distinct maximum
    for i in range(n):
        if nums[i] != max_num and nums[i] != second_max and nums[i] > third_max:
            third_max = nums[i]

    print("The third maximum element in the list is:", third_max)

    # If there are less than 3 distinct numbers
    if third_max == float('-inf'):
        return max_num

    return third_max


print(third_maximum(nums))