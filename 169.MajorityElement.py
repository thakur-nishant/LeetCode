"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

            if count[i] > n / 2:
                return i

