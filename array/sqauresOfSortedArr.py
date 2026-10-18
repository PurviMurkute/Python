nums = [-4,-1,0,3,10]

def sortedSquares(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = 0
        right = n-1
        result = [0] * n

        for i in range(n-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                val = nums[left]
                left+=1
            else:
                val = nums[right]
                right-=1

            print(val, ": ", val*val)
            print(result)
                
            result[i] = val*val

        return result

print(sortedSquares(nums))  # Output: [0, 1, 9, 16, 100]