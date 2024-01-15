# https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def go_down(self, current_index: int, num_rows: int, current_row: int):
        return current_index + ((num_rows - current_row) - 1) + ((num_rows - current_row) - 2) + 1

    def go_up(self, current_index: int, current_row: int):
        return current_index + current_row + (current_row - 1) + 1

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        output = ""
        # first row
        index = 0
        while index < len(s):
            output += s[index]
            index = self.go_down(index, numRows, 0)

        # middle rows
        for current_row in range(1, numRows-1):
            operation = "down"
            index = current_row
            while index < len(s):
                output += s[index]
                if operation == "down":
                    index = self.go_down(index, numRows, current_row)
                    operation = "up"
                elif operation == "up":
                    index = self.go_up(index, current_row)
                    operation = "down"

        # last row
        index = numRows - 1
        while index < len(s):
            output += s[index]
            index = self.go_up(index, numRows - 1)

        return output
