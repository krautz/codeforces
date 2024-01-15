# https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x *= -1
        output = int(str(x)[::-1])
        output = -output if negative else output
        if not pow(-2, 31) <= output <= pow(2, 31) - 1:
            return 0
        return output

    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x *= -1

        digits = []
        while x != 0:
            digits.append(x % 10)
            x = x // 10

        output = 0
        for idx, digit in enumerate(digits):
            output += digit * pow(10, len(digits) - 1 - idx)

        output = -output if negative else output
        if not pow(-2, 31) <= output <= pow(2, 31) - 1:
            return 0
        return output
