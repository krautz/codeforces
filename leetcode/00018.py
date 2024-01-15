# https://leetcode.com/problems/4sum/submissions/1146386113/
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

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []
        idx = 0
        while idx < len(nums) - 3:
            idx_2 = idx + 1
            while idx_2 < len(nums) - 2:
                left_idx = idx_2 + 1
                right_idx = len(nums) - 1
                while left_idx < right_idx:
                    num_sum = nums[idx] + nums[idx_2] + nums[left_idx] + nums[right_idx]
                    if num_sum == target:
                        output.append([nums[idx], nums[idx_2], nums[left_idx], nums[right_idx]])
                        left_idx = self.find_next_left_idx(left_idx, nums)
                        right_idx = self.find_next_right_idx(right_idx, nums)
                        continue
                    if num_sum - target > 0:
                        right_idx = self.find_next_right_idx(right_idx, nums)
                        continue
                    if num_sum - target < 0:
                        left_idx = self.find_next_left_idx(left_idx, nums)
                        continue
                idx_2 = self.find_next_left_idx(idx_2, nums)
            idx = self.find_next_left_idx(idx, nums)
        return output
