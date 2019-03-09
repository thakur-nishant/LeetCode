"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        result = len(nums) + 1
        total = 0
        window = []
        for i in range(len(nums)):
            window.append(nums[i])
            total += nums[i]
            while total >= s:
                result = min(result, len(window))
                total -= window.pop(0)
        if result == len(nums) + 1:
            return 0

        return result

