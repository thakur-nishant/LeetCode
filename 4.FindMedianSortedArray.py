"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return float(0)
        nums = []
        i = 0
        j = 0
        m = len(nums1)
        n = len(nums2)

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        while i < m:
            nums.append(nums1[i])
            i += 1

        while j < n:
            nums.append(nums2[j])
            j += 1

        l = len(nums)
        mid = l // 2
        if l % 2 == 0:
            median = (nums[mid - 1] + nums[mid]) / 2
        else:
            median = nums[mid]
        print(median)
        return float(median)


test = Solution()
test.findMedianSortedArrays([1,2],[3,4])