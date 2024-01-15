# https://leetcode.com/problems/remove-element/description/

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        index = 0
        swap_index = len(nums) - 1
        while index <= swap_index:
            if nums[index] == val:
                swap = nums[index]
                nums[index] = nums[swap_index]
                nums[swap_index] = swap
                swap_index -= 1
            else:
                index += 1
        return swap_index + 1
