"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        n = len(height)
        result = 0
        while i < n - 1:
            j = i + 1
            while j < n and height[j] < height[i]:
                j += 1
            if j == n:
                j = i + height[i+1:].index(max(height[i+1:])) + 1
            
            min_height = min(height[i], height[j])
            for k in range(i+1, j):
                    diff = min_height - height[k]
                    if diff > 0:
                        result += diff
            i = j

        return result


height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [2,8,5,5,6,1,7,4,5]
x = Solution().trap(height)
print(x)