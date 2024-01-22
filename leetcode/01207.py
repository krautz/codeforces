# https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=daily-question&envId=2024-01-22

from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = {}
        for item in arr:
            if item not in occurrences:
                occurrences[item] = 1
            else:
                occurrences[item] += 1
        
        return len(occurrences.values()) == len(set(occurrences.values()))
        