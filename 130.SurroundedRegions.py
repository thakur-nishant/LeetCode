"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not any(board):
            return
        log = []
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and board[i][j] == 'O':
                    log.append((i, j))
        while log:
            x, y = log.pop()
            board[x][y] = 'V'

            if x > 0 and board[x - 1][y] == 'O':
                log.append((x - 1, y))
            if y > 0 and board[x][y - 1] == 'O':
                log.append((x, y - 1))
            if x < m - 1 and board[x + 1][y] == 'O':
                log.append((x + 1, y))
            if y < n - 1 and board[x][y + 1] == 'O':
                log.append((x, y + 1))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'V':
                    board[i][j] = 'O'

