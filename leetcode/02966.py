# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/?envType=daily-question&envId=2024-02-01

from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        answer = [nums[i:i+3] for i in range(0, len(nums), 3)]
        for item in answer:
            if item[1] - item[0] > k or item[2] - item[0] > k or item[2] - item[1] > k:
                return []
        return answer
