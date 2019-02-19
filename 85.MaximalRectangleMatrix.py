class Solution:
    def maximalRectangle(self, matrix: 'List[List[str]]') -> 'int':
        if not matrix:
            return 0
        result = 0
        currHeights = [0] * len(matrix[0])
        for row in matrix:
            for i in range(len(currHeights)):
                if row[i] == "1":
                    currHeights[i] += 1
                else:
                    currHeights[i] = 0
            currArea = self.largestRectangleArea(currHeights)
            result = max(result, currArea)
        return result

    def largestRectangleArea(self, heights):
        i = 0
        maxArea = 0
        stack = []
        while i < len(heights):
            if not stack or heights[stack[-1]] < heights[i]:
                stack.append(i)
                i += 1
            else:
                peak = stack.pop()
                if not stack:
                    area = heights[peak] * i
                else:
                    area = heights[peak] * (i - stack[-1] - 1)
                maxArea = max(maxArea, area)
        while stack:
            peak = stack.pop()
            if not stack:
                area = heights[peak] * i
            else:
                area = heights[peak] * (i - stack[-1] - 1)
            maxArea = max(maxArea, area)
        return maxArea
