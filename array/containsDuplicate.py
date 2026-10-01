def containsDuplicate(nums):
    seen = {}

    for num in nums:
        if num in seen:
            return True
        seen[num] = num

    return False

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))