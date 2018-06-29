"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.


Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
"""


class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        rect1_area = (C - A) * (D - B)
        rect2_area = (G - E) * (H - F)

        intersection_x1 = max(A, E)
        intersection_x2 = min(C, G)

        intersection_y1 = max(B, F)
        intersection_y2 = min(D, H)

        intersection_width = intersection_x2 - intersection_x1
        intersection_height = intersection_y2 - intersection_y1

        if intersection_width <= 0 or intersection_height <= 0:
            intersection_area = 0
        else:
            intersection_area = intersection_width * intersection_height

        result = abs(rect1_area) + abs(rect2_area) - abs(intersection_area)

        return result

