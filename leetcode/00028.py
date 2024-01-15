# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_index = 0
        for haystack_index in range(len(haystack)):
            if haystack[haystack_index] == needle[needle_index]:
                while needle_index != len(needle):
                    if haystack_index + needle_index == len(haystack) or haystack[haystack_index + needle_index] != needle[needle_index]:
                        break
                    needle_index += 1
                if needle_index == len(needle):
                    return haystack_index
                needle_index = 0
        return -1
