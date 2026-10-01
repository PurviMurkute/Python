def containsNearbyDuplicate(nums, k):
    seen = {}

    for i in range(len(nums)):
        print(seen)
        if nums[i] in seen and i - seen[nums[i]] <= k:
            return True
        seen[nums[i]] = i

    return False

print(containsNearbyDuplicate([1,0,1,1], 1))