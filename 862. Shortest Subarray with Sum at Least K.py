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
        n = len(A)
        curr_sum = A[0]
        i = 0
        j = 0
        min_len = n + 1
        while i < n and j < n:
            if curr_sum >= K:
                if min_len >= j - i + 1:
                    min_len = j - i + 1
                curr_sum -= A[i]
                i += 1
            else:
                j += 1
                if j < n:
                    curr_sum += A[j]
                    if curr_sum <= A[j]:
                        i = j
                        curr_sum = A[i]
            if i+1 < n and A[i] < 0:
                curr_sum -= A[i]
                i += 1

            print(i,j,curr_sum)

        if min_len == n + 1:
            return -1
        return min_len

# A = [84,-37,32,40,95]
# K = 167
A = [-34,37,51,3,-12,-50,51,100,-47,99,34,14,-13,89,31,-14,-44,23,-38,6]
K = 151
x = Solution().shortestSubarray(A, K)
print("##########")
print(x)