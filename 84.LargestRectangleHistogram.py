"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.




Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].




The largest rectangle is shown in the shaded area, which has area = 10 unit.
"""

class Solution:
    def largestRectangleArea(self, heights: 'List[int]') -> 'int':
        stack = []
        i = 0
        max_area = 0
        while i < len(heights):
            # print("stack:", stack)
            if not stack or heights[stack[-1]] < heights[i]:
                stack.append(i)
                i += 1
            else:
                peak = stack.pop()
                if not stack:
                    area = heights[peak] * i
                else:
                    area = heights[peak] * (i - stack[-1] - 1)
                max_area = max(max_area, area)
        while stack:
            peak = stack.pop()
            if not stack:
                area = heights[peak] * i
            else:
                area = heights[peak] * (i - stack[-1] - 1)
            max_area = max(max_area, area)
        return max_area


heights = [3, 1, 3, 2, 2]
print(Solution().largestRectangleArea(heights))
