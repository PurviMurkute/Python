nums = [3, 7]
def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max = 0

        for i in range(n):
            if nums[i] > nums[max]:
                max = i

        sec_max = 0 if max != 0 else 1

        for i in range(n):
            if nums[i] > nums[sec_max] and i != max:
                sec_max = i

        max_product = ((nums[max]-1) * (nums[sec_max]-1))

        return max_product

print(maxProduct(0, nums))  # Output: 12