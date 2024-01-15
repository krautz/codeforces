# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        max_length = 0
        for char in s:
            if char in substring:
                if len(substring) > max_length:
                    max_length = len(substring)
                index = substring.index(char)
                substring = substring[index+1:]
            substring += char
        if len(substring) > max_length:
            max_length = len(substring)
        return max_length
