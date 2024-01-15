
# https://leetcode.com/problems/generate-parentheses/description/

from typing import List

class Solution:
    def recursion(self, n_open, n_close, current_stack, simplified_stack):
        if n_open < 0 or n_close < 0 or (n_open == 0 and n_close == 0 and simplified_stack != ""):
            return []
        if n_open == 0 and n_close == 0 and simplified_stack == "":
            return [current_stack]

        open_result = self.recursion(n_open - 1, n_close, current_stack + "(", simplified_stack + "(")

        if len(simplified_stack) > 0 and simplified_stack[-1] == "(":
            close_simplified_stack = simplified_stack[:-1]
        else:
            close_simplified_stack = simplified_stack + ")"
        close_result = self.recursion(n_open, n_close - 1, current_stack + ")", close_simplified_stack)

        return open_result + close_result

    def generateParenthesis(self, n: int) -> List[str]:
        return self.recursion(n, n, "", "")
