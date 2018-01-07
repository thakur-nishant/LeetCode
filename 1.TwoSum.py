class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        n = len(nums)
        for i in range(n):
            x = target - nums[i]
            if x in dict:
                print([dict[x], i])
                return [dict[x], i]
            else:
                dict[nums[i]] = i


test = Solution()

nums = [2, 7, 11, 15]
tragetsum = 9
test.twoSum(nums, tragetsum)