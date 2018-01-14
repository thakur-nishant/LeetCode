"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively.
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1.clear()
            # print("In-funct:", nums1)
            for i in range(len(nums2)):
                (nums1.insert(i, nums2[i]))
        elif n == 0:
            pass
        else:
            arr = []
            i = 0
            j = 0

            while i < m and j < n:
                if nums1[i] < nums2[j]:
                    arr.append(nums1[i])
                    i += 1
                else:
                    arr.append(nums2[j])
                    j += 1

            while i < m:
                arr.append(nums1[i])
                i += 1

            while j < n:
                arr.append(nums2[j])
                j += 1

            nums1.clear()
            # print("In-funct:", nums1)
            for i in range(len(arr)):
                (nums1.insert(i,arr[i]))
            # print("In-funct:", nums1)


def main():
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    # nums1 = [1, 2, 3, 4, 6, 8, 9, 10, 13]
    # nums2 = [2, 3, 5, 7, 9]
    # m = 9
    # n = 5
    print("1In-main:", nums1)
    Solution().merge(nums1, m, nums2, n)
    print("2In-main:", nums1)


if __name__ == '__main__':
    main()

