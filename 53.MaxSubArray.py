class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum = maxSum = nums[0]

        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum

test = Solution()

nums = [-2,1,-3,4,-1,2,1,-5,4]
x = test.maxSubArray(nums)
print(x)