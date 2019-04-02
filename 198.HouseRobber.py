"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

"""


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        last = [nums[0], nums[1], nums[2] + nums[0]]
        for i in range(3, len(nums)):
            pre_max = max(last[0], last[1])
            last.pop(0)
            last.append(nums[i] + pre_max)
        # print(last)
        return max(last[1], last[2])


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        log = [0] * len(nums)
        result = 0
        for i in range(len(nums)):
            if i - 3 >= 0:
                log[i] = max(log[i - 2], log[i - 3])
            elif i - 2 >= 0:
                log[i] = log[i - 2]

            log[i] += nums[i]
            result = max(result, log[i])

        return result

