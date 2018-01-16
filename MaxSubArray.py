import sys
class Solution:

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        low, high, max_sum  = self.findMaxSubArray(nums, 0, n-1)
        # print(low, high, max_sum)

        return max_sum

    def findMaxSubArray(self, nums, low, high):
        if low == high:
            return (low, high, nums[low])
        else:
            mid = (low + high) // 2;

            leftl, lefth, left_sum = self.findMaxSubArray(nums, low, mid)
            rightl, righth, right_sum = self.findMaxSubArray(nums, mid + 1, high)
            crossl, crossh, cross_sum = self.findMaxCrossSubArray(nums, low, mid, high)

            if left_sum >= right_sum and left_sum >= cross_sum:
                return (leftl, lefth, left_sum)
            if right_sum >= left_sum and right_sum >= cross_sum:
                return (rightl, righth, right_sum)
            else:
                return (crossl, crossh, cross_sum)


    def findMaxCrossSubArray(self, nums, low, mid, high):
        left_sum = -sys.maxsize
        sum = 0
        for i in range(mid, -1, -1):
            sum = sum + nums[i]
            if sum > left_sum:
                left_sum = sum
                max_left = i

        right_sum = -sys.maxsize
        sum = 0
        for j in range(mid+1, high+1):
            sum = sum + nums[j]
            if sum > right_sum:
                right_sum = sum
                max_right = j

        return (max_left, max_right, left_sum + right_sum)



test = Solution()

nums = [-2,1,-3,4,-1,2,1,-5,4]
x = test.maxSubArray(nums)
print(x)