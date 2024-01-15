# https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(' ')
        end_idx=len(s)
        for idx, digit in enumerate(s):
            if idx == 0 and s[0] in ["+", "-"]:
                continue
            try:
                int(digit)
            except ValueError:
                end_idx = idx
                break
        s = s[:end_idx]

        output = 0
        for idx, digit in enumerate(s):
            if idx == 0 and s[0] in ["+", "-"]:
                continue

            print(digit, len(s) - 1 - idx)
            try:
                output += int(digit) * pow(10, len(s) - 1 - idx)
            except ValueError:
                break

        output = -output if len(s) > 0 and s[0] == "-" else output
        if output > pow(2, 31) - 1:
            return pow(2, 31) - 1
        if output < pow(-2, 31):
            return pow(-2, 31)
        return output
