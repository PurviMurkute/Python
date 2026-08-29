""" num = "1210"

print(num[3]) """

def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        original = x
        rev = 0
        
        while x > 0:
            last = x % 10
            rev = (rev * 10) + last
            x = x // 10
        
        if rev == original:
            return True
        
        return False

print(isPalindrome(121))