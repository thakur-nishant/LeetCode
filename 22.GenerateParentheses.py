"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        combinations = {0: [""]}
        i = 0
        while i < n:
            possible_combinations = set()
            for pattern in combinations[i]:
                for j in range(len(pattern) + 1):
                    new_pattern = pattern[:j] + "()" + pattern[j:]
                    possible_combinations.add(new_pattern)

            combinations[i + 1] = list(possible_combinations)
            i += 1
        return sorted(combinations[n])

