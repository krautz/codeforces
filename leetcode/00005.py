# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def is_palindrome(self, s: str, i: int, j: int):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    def longestPalindrome(self, s: str) -> str:
        longest_substring = ""
        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                if j - i + 1 <= len(longest_substring):
                    break
                if self.is_palindrome(s, i, j):
                    longest_substring = s[i:j+1]
        return longest_substring
