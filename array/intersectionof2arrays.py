nums1 = [1,2,1]
nums2 = [2, 2]

def intersect(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        seen = {}
        result = []

        for num in nums1:
            seen[num] = seen.get(num, 0) + 1

        for num in nums2:
              if num in seen and seen[num] > 0:
                    result.append(num)
                    seen[num] -= 1

        return result

print(intersect(nums1, nums2))