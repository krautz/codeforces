# https://leetcode.com/problems/count-elements-with-maximum-frequency/description/?envType=daily-question&envId=2024-03-08

from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequency_by_num = {}
        for num in nums:
            if num not in frequency_by_num:
                frequency_by_num[num] = 0
            frequency_by_num[num] += 1

        counter = 0
        max_frequency = max(frequency_by_num.values())
        for frequency in frequency_by_num.values():
            if frequency == max_frequency:
                counter += 1

        return counter * max_frequency
