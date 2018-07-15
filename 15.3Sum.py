"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        for i in range(len(nums)-2):
            check = {}
            for j in range(i+1,len(nums)):
                if nums[j] in check:
                    result.add(tuple(sorted([nums[i], nums[j], check[nums[j]]])))
                else:
                    check[0 - nums[i] - nums[j]] = nums[j]
        result = sorted([list(x) for x in result])

        return result


nums = [0,0,0]
x = Solution().threeSum(nums)
print(x)