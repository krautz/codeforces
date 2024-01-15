# https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == ")" and len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            elif char == "]" and len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            elif char == "}" and len(stack) > 0 and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(char)

        if len(stack) == 0:
            return True
        return False
