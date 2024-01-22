# https://leetcode.com/problems/climbing-stairs/description/?envType=daily-question&envId=2024-01-22

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        next_step_options = 2
        next_next_step_options = 1
        for step in range(2, n):
            current = next_step_options + next_next_step_options
            next_next_step_options = next_step_options
            next_step_options = current
        return current