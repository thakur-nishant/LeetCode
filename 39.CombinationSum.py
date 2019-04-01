"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        visited = set()
        result = []
        self.dfs_helper(0, [], candidates, target, result, visited)
        return result

    def dfs_helper(self, curr_sum, used_candidates, candidates, target, result, visited):
        if tuple(sorted(used_candidates)) in visited:
            return
        visited.add(tuple(sorted(used_candidates)))
        if curr_sum == target:
            result.append(used_candidates)
        if curr_sum < target:
            for i in candidates:
                self.dfs_helper(curr_sum + i, used_candidates + [i], candidates, target, result, visited)


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        comb = set()
        r = self.getCombinations(candidates, target, [], comb)
        return sorted([list(i) for i in r])

    def getCombinations(self, candidates, target, result, comb):
        for num in candidates:
            if sum(result + [num]) == target:
                comb.add(tuple(sorted(result + [num])))
            elif sum(result + [num]) < target:
                res = self.getCombinations(candidates, target, (result + [num]), comb)
                if res:
                    comb |= res
        return comb


candidates = [1,2]
target = 1

x = Solution().combinationSum(candidates, target)
print(x)
