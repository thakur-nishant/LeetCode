class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s.isspace():
            return 0
        string = s.split()
        # print(string[-1])
        return len(string[-1])