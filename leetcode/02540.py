# https://leetcode.com/problems/minimum-common-value/description/?envType=daily-question&envId=2024-03-09

from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        pointer1 = 0
        pointer2 = 0

        while pointer1 < len(nums1) and pointer2 < len(nums2):
            if nums1[pointer1] == nums2[pointer2]:
                return nums1[pointer1]

            if nums1[pointer1] < nums2[pointer2]:
                pointer1 += 1
            else:
                pointer2 += 1

        return -1

    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = set(nums1)
        nums2 = set(nums2)
        intersec = nums1.intersection(nums2)
        if intersec:
            return min(intersec)
        return -1
