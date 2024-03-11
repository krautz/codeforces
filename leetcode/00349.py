# https://leetcode.com/problems/intersection-of-two-arrays/description/?envType=daily-question&envId=2024-03-11

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for num in nums1:
            if num in nums2 and num not in output:
                output.append(num)
        return output

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1.intersection(nums2))
