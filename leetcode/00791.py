# https://leetcode.com/problems/custom-sort-string/description/?envType=daily-question&envId=2024-03-11

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_occurrences = {}
        order_set = set(order)
        output = ""
        for char in s:
            if char not in order_set:
                output += char
                continue
            if char not in char_occurrences:
                char_occurrences[char] = 0
            char_occurrences[char] += 1

        for char in order:
            if char in char_occurrences:
                output += char * char_occurrences[char]

        return output
