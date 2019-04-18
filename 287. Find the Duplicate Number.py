"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]

        :rtype: int
        """
        anchor = i = 0
        result = 0
        while i < len(nums):
            if i + 1 < len(nums):
                result = max(result, i - anchor + 1)
                if nums[i] >= nums[i + 1]:
                    anchor = i + 1
            i += 1
        return max(result, i - anchor)


class Solution(object):
    def findLengthOfLCIS(self, nums):
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]: anchor = i
            ans = max(ans, i - anchor + 1)
        return ans
