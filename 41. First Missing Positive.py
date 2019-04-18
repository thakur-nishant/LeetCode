"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        log = [0] * (len(nums) + 2)
        for num in nums:
            if len(log) > num > 0:
                log[num] = 1

        for i in range(1, len(log)):
            if log[i] == 0:
                return i


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                curr_index = nums[i] - 1
                nums[i], nums[curr_index] = nums[curr_index], nums[i]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1
