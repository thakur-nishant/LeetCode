"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""


# Bruit force solution- genereate all permutations and return the Kth result
class Solution1:
    def getPermutation(self, n: int, k: int) -> str:
        arr = [i for i in range(1, n + 1)]
        result = []

        for i in range(n):
            self.helper([arr[i]], arr[:i] + arr[i + 1:], result)

        return ''.join([str(x) for x in result[k - 1]])

    def helper(self, pre, arr, result):
        if pre in result:
            return
        if not arr:
            result.append(pre)
            return
        for i in range(len(arr)):
            self.helper(pre + [arr[i]], arr[:i] + arr[i + 1:], result)


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = [i for i in range(1, n + 1)]
        factorial = [1]
        for i in range(1, n + 1):
            factorial.append(i * factorial[-1])

        k -= 1
        result = ""
        for i in range(1, n + 1):
            index = k // factorial[n - i]
            result += str(arr[index])
            arr.pop(index)
            k -= factorial[n - i] * index

        return result


