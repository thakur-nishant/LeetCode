class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        string = ""
        for i in range(len(s)):
            if s[i].isalnum():
                string += str(s[i].lower())

        n = len(string)
        flag = True
        for i in range(n // 2):
            if string[i] != string[n - i - 1]:
                flag = False
                break

        return flag


test = Solution()

s = "A man, a plan, a canal: Panama"
x = test.isPalindrome(s)
print(x)
