# https://leetcode.com/problems/longest-common-prefix/
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx = 0
        while True:
            if len(strs[0]) == idx:
                return strs[0][:idx]
            char = strs[0][idx]
            for word in strs:
                if len(word) == idx or word[idx] != char:
                    return strs[0][:idx]
            idx += 1
