"""
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.



Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3


Note:

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9
"""


class Solution:
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        result = self.check(A, K)
        if result == 50001:
            return -1
        else:
            return result

    def check(self, A, K):
        if len(A) > 1:q
            left = self.check(A[:-1], K)
            right = self.check(A[1:], K)

            if left < right:
                result = left
            else:
                result = right

            if sum(A) >= K:
                temp = len(A)
            else:
                temp = 50001

            if result < temp:
                return result
            else:
                return temp
        else:
            if A[0] >= K:
                return 1
            return 50001

A = [2,2]
K = 4
K = Solution().shortestSubarray(A, K)
print(K)