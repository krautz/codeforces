# https://leetcode.com/problems/binary-subarrays-with-sum/description/?envType=daily-question&envId=2024-03-14

from typing import List

class Solution:
    def solve_goal_0(self, nums: List[int]):
        window_count = 0
        consecutive_zeroes_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                consecutive_zeroes_count += 1
                window_count += consecutive_zeroes_count
            else:
                consecutive_zeroes_count = 0
        return window_count

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # edge case: goal is 0
        if goal == 0:
            return self.solve_goal_0(nums)

        ones_index = []
        for i in range(len(nums)):
            if nums[i] == 1:
                ones_index.append(i)

        count = 0
        for left_index in range(len(ones_index) - goal + 1):
            right_index = left_index + goal - 1

            left_zeroes_count = 0
            if left_index == 0:
                left_zeroes_count = ones_index[left_index]
            else:
                left_zeroes_count = ones_index[left_index] - ones_index[left_index - 1] - 1

            right_zeroes_count = 0
            if right_index == len(ones_index) - 1:
                right_zeroes_count = len(nums) - 1 - ones_index[right_index]
            else:
                right_zeroes_count = ones_index[right_index + 1] - ones_index[right_index] - 1

            count += 1 + left_zeroes_count + right_zeroes_count + (left_zeroes_count * right_zeroes_count)

        return count

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # edge case: goal is 0
        if goal == 0:
            return self.solve_goal_0(nums)

        ones_index = [-1]
        for i in range(len(nums)):
            if nums[i] == 1:
                ones_index.append(i)
        ones_index.append(len(nums))

        count = 0
        for left_index in range(1, len(ones_index) - goal):
            right_index = left_index + goal - 1

            left_zeroes_count = ones_index[left_index] - ones_index[left_index - 1] - 1
            right_zeroes_count = ones_index[right_index + 1] - ones_index[right_index] - 1

            count += 1 + left_zeroes_count + right_zeroes_count + (left_zeroes_count * right_zeroes_count)

        return count
