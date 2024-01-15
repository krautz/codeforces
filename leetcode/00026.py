# https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1147391669/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        largest_number = nums[0]
        index = 1
        swap_index = None
        while index < len(nums):
            if nums[index] == largest_number and not swap_index:
                swap_index = index
            if nums[index] != largest_number:
                largest_number = nums[index]
                if swap_index:
                    swap = nums[index]
                    nums[index] = nums[swap_index]
                    nums[swap_index] = swap
                    swap_index += 1
            index += 1


        return swap_index if swap_index else len(nums)
