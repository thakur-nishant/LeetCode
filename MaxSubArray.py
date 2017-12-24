def findSum(nums, low, high):
    if low == high:
        return nums[low]
    else:
        n = high+low
        mid = n//2
        print("Index:",low, mid, high)
        left_sum = findSum(nums, low, mid)
        right_sum = findSum(nums, mid+1, high)
        cross_sum = left_sum + right_sum

        print(left_sum,cross_sum,right_sum)
        return max(left_sum,cross_sum,right_sum)


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        high = len(nums)-1
        max_sum = findSum(nums, 0, high)
        # print(max_sum)
        return max_sum


test = Solution()

nums = [-2,1,-3,4,-1,2,1,-5,4]
x = test.maxSubArray(nums)
print(x)