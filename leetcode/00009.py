# https://leetcode.com/problems/palindrome-number/submissions/1146310966/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        digits = []
        while x != 0:
            digits.append(x % 10)
            x = x // 10

        for idx in range(len(digits) // 2):
            if digits[idx] != digits[len(digits) - idx - 1]:
                return False
        return True

