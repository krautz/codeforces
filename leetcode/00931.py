# https://leetcode.com/problems/minimum-falling-path-sum/description/?envType=daily-question&envId=2024-01-19

from typing import List

class Solution:
    def go_down(self, row, column, matrix):
        if column == -1 or column == len(matrix):
            return None
        if (row, column) in self.memoized_short_path:
            return self.memoized_short_path[(row, column)]
        if row == len(matrix) - 1:
            return matrix[row][column]

        smallest = (100 * 100) + 1

        left = self.go_down(row + 1, column - 1, matrix)
        if left is not None and left < smallest:
            smallest = left

        middle = self.go_down(row + 1, column, matrix)
        if middle is not None and middle < smallest:
            smallest = middle

        right = self.go_down(row + 1, column + 1, matrix)
        if right is not None and right < smallest:
            smallest = right

        self.memoized_short_path[(row, column)] = smallest + matrix[row][column]
        return self.memoized_short_path[(row, column)]

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        self.memoized_short_path = {}
        smallest = (100 * 100) + 1
        for column in range(len(matrix)):
            column_smallest_path = self.go_down(0, column, matrix)
            if column_smallest_path < smallest:
                smallest = column_smallest_path
        return smallest
