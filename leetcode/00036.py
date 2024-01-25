# https://leetcode.com/problems/valid-sudoku/description/

from typing import List

class Solution:
    def validate_row(self, matrix, row_index):
        unique_digits = set()
        for column_index in range(9):
            digit = matrix[row_index][column_index]
            if digit != ".":
                if digit in unique_digits:
                    return False
                unique_digits.add(digit)
        return True

    def validate_column(self, matrix, column_index):
        unique_digits = set()
        for row_index in range(9):
            digit = matrix[row_index][column_index]
            if digit != ".":
                if digit in unique_digits:
                    return False
                unique_digits.add(digit)
        return True

    def validate_sub_boxes(self, matrix, start_row_index, start_column_index):
        unique_digits = set()
        for row_index in range(start_row_index, start_row_index + 3):
            for column_index in range(start_column_index, start_column_index + 3):
                digit = matrix[row_index][column_index]
                if digit != ".":
                    if digit in unique_digits:
                        return False
                    unique_digits.add(digit)
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for index in range(9):
            value = self.validate_row(board, index)
            if value is False:
                return value
            value = self.validate_column(board, index)
            if value is False:
                return value

        for row_index in range(0, 9, 3):
            for column_index in range(0, 9, 3):
                value = self.validate_sub_boxes(board, row_index, column_index)
                if value is False:
                    return value

        return True
