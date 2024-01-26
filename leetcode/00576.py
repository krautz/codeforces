# https://leetcode.com/problems/out-of-boundary-paths/description/?envType=daily-question&envId=2024-01-26

from collections import defaultdict

class Solution:
    def recursion(self, m, n, moves, i, j):
        if moves == -1:
            return 0
        if i < 0 or i == m or j < 0 or j == n:
            return 1
        if self.memoization[i][j][moves] != -1:
            return self.memoization[i][j][moves]

        up = self.recursion(m, n, moves - 1, i - 1, j)
        down = self.recursion(m, n, moves - 1, i + 1, j)
        left = self.recursion(m, n, moves - 1, i, j - 1)
        right = self.recursion(m, n, moves - 1, i, j + 1)

        self.memoization[i][j][moves] = up + down + left + right
        return self.memoization[i][j][moves]

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.memoization = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: -1)))
        return self.recursion(m, n, maxMove, startRow, startColumn) % 1000000007
