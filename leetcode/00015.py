# https://leetcode.com/problems/3sum/description/
from typing import List
class Solution:
    def find_next_left_idx(self, idx, nums):
        next_idx = idx + 1
        while next_idx != len(nums) and nums[idx] == nums[next_idx]:
            next_idx += 1
        return next_idx

    def find_next_right_idx(self, idx, nums):
        next_idx = idx - 1
        while next_idx != -1 and nums[idx] == nums[next_idx]:
            next_idx -= 1
        return next_idx

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        idx = 0
        while idx < len(nums) - 2:
            left_idx = idx + 1
            right_idx = len(nums) - 1
            while left_idx < right_idx:
                if nums[idx] + nums[left_idx] + nums[right_idx] == 0:
                    output.append([nums[idx], nums[left_idx], nums[right_idx]])
                    left_idx = self.find_next_left_idx(left_idx, nums)
                    right_idx = self.find_next_right_idx(right_idx, nums)
                    continue
                if nums[idx] + nums[left_idx] + nums[right_idx] > 0:
                    right_idx = self.find_next_right_idx(right_idx, nums)
                    continue
                if nums[idx] + nums[left_idx] + nums[right_idx] < 0:
                    left_idx = self.find_next_left_idx(left_idx, nums)
                    continue
            idx = self.find_next_left_idx(idx, nums)
        return output
