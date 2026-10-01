def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                print(digits)
            else:
                digits[i] += 1
                return digits

        res = [0] * (len(digits) + 1)
        print(res)
        res[0] = 1
        print(res)
        return res

print(plusOne([9]))