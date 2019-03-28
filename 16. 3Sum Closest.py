"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

# O(n^3) solution
import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_dist = sys.maxsize
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    # print(nums[i]+nums[j]+nums[k],nums[i],nums[j],nums[k])
                    curr_sum = nums[i] + nums[j] + nums[k]
                    if abs(curr_sum - target) < min_dist:
                        min_dist = abs(curr_sum - target)
                        result = curr_sum
        return result

# O(n^2) solution

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_dist = sys.maxsize
        nums = sorted(nums)
        for i in range(len(nums)):
            low = i + 1
            high = len(nums) - 1

            while low < high:
                curr_sum = nums[i] + nums[low] + nums[high]
                if curr_sum == target:
                    return curr_sum
                if curr_sum > target:
                    high -= 1
                if curr_sum < target:
                    low += 1
                if abs(target - curr_sum) < min_dist:
                    min_dist = abs(target - curr_sum)
                    result = curr_sum

        return result



