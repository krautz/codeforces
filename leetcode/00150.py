# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=daily-question&envId=2024-01-30

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)
            elif token == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif token == "*":
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)
            elif token == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))
            else:
                stack.append(int(token))
        return stack[0]
    def evalRPN_n2(self, tokens: List[str]) -> int:
        while len(tokens) != 1:
            for index in range(len(tokens)):
                if tokens[index + 2] == "+":
                    tokens = tokens[:index] + [int(tokens[index]) + int(tokens[index + 1])] + tokens[index + 3:]
                    break
                if tokens[index + 2] == "-":
                    tokens = tokens[:index] + [int(tokens[index]) - int(tokens[index + 1])] + tokens[index + 3:]
                    break
                if tokens[index + 2] == "/":
                    tokens = tokens[:index] + [int(int(tokens[index]) / int(tokens[index + 1]))] + tokens[index + 3:]
                    break
                if tokens[index + 2] == "*":
                    tokens = tokens[:index] + [int(tokens[index]) * int(tokens[index + 1])] + tokens[index + 3:]
                    break
        return int(tokens[0])
