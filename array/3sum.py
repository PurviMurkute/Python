def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()

        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.add((nums[i], nums[j], nums[k]))

        return [list(x) for x in result]

print(threeSum([-1,0,1,2,-1,-4]))

# -4, -1, -1, 0, 1, 2