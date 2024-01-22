# https://leetcode.com/problems/house-robber/?envType=daily-question&envId=2024-01-22

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if nums[-2] < nums[-1]:
            nums[-2] = nums[-1]

        for i in range(len(nums) - 3, -1, -1):
            if nums[i] + nums[i + 2] > nums[i + 1]:
                nums[i] += nums[i + 2]
            else:
                nums[i] = nums[i + 1]

        return nums[0]
