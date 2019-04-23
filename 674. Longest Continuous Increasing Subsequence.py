"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.
Note: Length of the array will not exceed 10,000.
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

