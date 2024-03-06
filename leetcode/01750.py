# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description/?envType=daily-question&envId=2024-03-06

class Solution:
    def minimumLength(self, s: str) -> int:
        start = 0
        end = len(s) - 1
        while start < end:

            # check if suffix is equal to prefix
            # if not, return
            start_character = s[start]
            end_character = s[end]
            if start_character != end_character:
                return end - start + 1

            # find all characters that are the same at the start and "remove" them
            while start + 1 < len(s) and s[start] == s[start + 1]:
                start = start + 1
            start = start + 1

            # find all characters that are the same at the end and "remove" them
            while end - 1 >= 0 and s[end] == s[end - 1]:
                end = end - 1
            end = end - 1

        if start == end:
            return 1
        return 0
