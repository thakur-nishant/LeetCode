#Determine whether an integer is a palindrome. Do this without extra space."""

"""
Solution by converting number to string

class Solution:
    def isPalindrome(self, x):
        flag = True
        x = str(x)
        n = len(x)
        for i in range(n // 2):
            if x[i] != x[n - i - 1]:
                flag = False
        return flag
        
"""
# Solution using logic

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        copyx = x
        temp = 0
        while x > 0:
            temp = temp * 10 + x % 10
            x = x // 10

        if temp == copyx:
            return True

        return False





