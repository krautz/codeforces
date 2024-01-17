# https://leetcode.com/problems/next-permutation/

from typing import List

class Solution:


    def swap(self, i, j, nums):
        storage = nums[i]
        nums[i] = nums[j]
        nums[j] = storage


    def reverse(self, start_index, end_index, nums):
        while start_index < end_index:
            self.swap(start_index, end_index, nums)
            start_index += 1
            end_index -= 1


    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = len(nums) - 2
        while index >= 0:
            after_me_smaller_bigger_than_me_index = -1
            after_me_smaller_bigger_than_me = 101
            for next_index in range(index + 1, len(nums)):
                if nums[next_index] > nums[index] and nums[next_index] <= after_me_smaller_bigger_than_me:
                    after_me_smaller_bigger_than_me = nums[next_index]
                    after_me_smaller_bigger_than_me_index = next_index
            if after_me_smaller_bigger_than_me_index != -1:
                self.swap(index, after_me_smaller_bigger_than_me_index, nums)
                self.reverse(index + 1, len(nums) - 1, nums)
                break
            index -= 1


        if index == -1:
            self.reverse(0, len(nums) - 1, nums)
