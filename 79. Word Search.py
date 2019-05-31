"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not any(board) or not word:
            return False

        def dfs(i, j, k, visited):
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and not visited[i][j] and board[i][j] == word[k]:
                if k == len(word) - 1:
                    return True
                visited[i][j] = 1
                down = dfs(i + 1, j, k + 1, visited)
                up = dfs(i - 1, j, k + 1, visited)
                right = dfs(i, j + 1, k + 1, visited)
                left = dfs(i, j - 1, k + 1, visited)
                if down or up or right or left:
                    return True
                visited[i][j] = 0
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = [[0] * len(board[0]) for _ in range(len(board))]
                    if dfs(i, j, 0, visited):
                        return True
        return False

