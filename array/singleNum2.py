def singleNumber(nums):
    seen = {}

    for num in nums:
        seen[num] = seen.get(num, 0) + 1

        print(seen)

    for num in seen:
        if seen[num] == 1:
            return num

print(singleNumber([2,2,3,2]))