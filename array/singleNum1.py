def singleNumber(nums):
    seen = {}

    for num in nums:
        if num not in seen:
            seen[num] = 1
        else:
            seen[num] += 1

    for num in seen:
        if seen[num] == 1:
            return num

print(singleNumber([2,2,3,2]))