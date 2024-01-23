# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/?envType=daily-question&envId=2024-01-23

from typing import List

class Solution:
    def has_duplicated_chars(self, string: str):
        chars = set(string)
        return len(chars) != len(string)

    def any_char_already_in_response(self, string: str, seen_chars: set[str]):
        return len(set(string) - seen_chars) != len(string)

    def recursive(self, current_index: str, arr: List[str], seen_chars: set[str]):
        if current_index == len(arr):
            return 0
        
        # current item has duplciated strings -> skip
        if self.has_duplicated_chars(arr[current_index]):
            return self.recursive(current_index + 1, arr, seen_chars)

        # any character in current item already present in response -> skip
        if self.any_char_already_in_response(arr[current_index], seen_chars):
            return self.recursive(current_index + 1, arr, seen_chars)
        
        # compute longest string including current item
        seen_chars = seen_chars | set(arr[current_index])
        include_me = len(arr[current_index]) + self.recursive(current_index + 1, arr, seen_chars)

        # compute longest string skiping current item
        seen_chars = seen_chars - set(arr[current_index])
        skip_me = self.recursive(current_index + 1, arr, seen_chars)

        return skip_me if skip_me > include_me else include_me

    def maxLength(self, arr: List[str]) -> int:
        max_found = 0
        for index in range(len(arr)):
            length = self.recursive(index, arr, set())
            if length > max_found:
                max_found = length
        return max_found
        