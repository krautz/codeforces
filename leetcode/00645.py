# https://leetcode.com/problems/set-mismatch/description/?envType=daily-question&envId=2024-01-22

from typing import List

class Solution:
    def findErrorNums_hash_map(self, nums: List[int]) -> List[int]:
        nums_count = {n: 0 for n in range(1, len(nums) + 1)}
        for num in nums:
            nums_count[num] += 1
        for num, count in nums_count.items():
            if count == 0:
                missing = num
            if count == 2:
                duplicated = num
        return [duplicated, missing]

    def findErrorNums_sort(self, nums: List[int]) -> List[int]:
        nums.sort()
        missing = None
        duplicated = None
        for index in range(len(nums) - 1):
            if nums[index] == nums[index + 1]:
                duplicated = nums[index]
            if nums[index] + 2 == nums[index + 1]:
                missing = nums[index] + 1
        if missing == None:
            if nums[0] != 1:
                missing = 1
            else:
                missing = nums[-1] + 1
        return [duplicated, missing]
