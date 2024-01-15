# https://leetcode.com/problems/3sum-closest/description/
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

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        smallest_diff_to_target = 10000 + 3003
        cloasest_sum = None
        idx = 0
        while idx < len(nums) - 2:
            left_idx = idx + 1
            right_idx = len(nums) - 1
            while left_idx < right_idx:
                num_sum = nums[idx] + nums[left_idx] + nums[right_idx]
                if abs(num_sum - target) < smallest_diff_to_target:
                    smallest_diff_to_target = abs(num_sum - target)
                    cloasest_sum = num_sum
                if num_sum == target:
                    break
                if num_sum > target:
                    right_idx = self.find_next_right_idx(right_idx, nums)
                    continue
                if num_sum < target:
                    left_idx = self.find_next_left_idx(left_idx, nums)
                    continue
            idx = self.find_next_left_idx(idx, nums)
        return cloasest_sum
