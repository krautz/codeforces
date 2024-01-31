# https://leetcode.com/problems/daily-temperatures/description/?envType=daily-question&envId=2024-01-31

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for index, temperature in enumerate(temperatures):
            while len(stack) and temperature > stack[-1][0]:
                _, old_index = stack.pop()
                answer[old_index] = index - old_index
            stack.append((temperature, index))

        return answer
