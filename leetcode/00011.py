# https://leetcode.com/problems/container-with-most-water/submissions/1146330421/
from typing import List
class Solution:
    def compute_volume(self, height: List[int], left_index: int, right_index: int):
        return min(height[left_index], height[right_index]) * (right_index - left_index)
    def maxArea(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height) - 1
        max_volume = min(height[left_index], height[right_index]) * (right_index - left_index)
        while left_index != right_index:
            volume = self.compute_volume(height, left_index, right_index)
            max_volume = max_volume if max_volume > volume else volume
            if height[left_index] < height[right_index]:
                left_index += 1
            else:
                right_index -= 1
        return max_volume
