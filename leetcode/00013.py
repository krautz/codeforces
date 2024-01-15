# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        idx = 0
        while idx != len(s):
            if idx <= len(s) - 2:
                double_option = s[idx] + s[idx + 1]
                if double_option == "CM":
                    output += 900
                    idx += 2
                    continue
                if double_option == "CD":
                    output += 400
                    idx += 2
                    continue
                if double_option == "XC":
                    output += 90
                    idx += 2
                    continue
                if double_option == "XL":
                    output += 40
                    idx += 2
                    continue
                if double_option == "IX":
                    output += 9
                    idx += 2
                    continue
                if double_option == "IV":
                    output += 4
                    idx += 2
                    continue
            if s[idx] == "M":
                output += 1000
                idx += 1
                continue
            if s[idx] == "D":
                output += 500
                idx += 1
                continue
            if s[idx] == "C":
                output += 100
                idx += 1
                continue
            if s[idx] == "L":
                output += 50
                idx += 1
                continue
            if s[idx] == "X":
                output += 10
                idx += 1
                continue
            if s[idx] == "V":
                output += 5
                idx += 1
                continue
            output += 1
            idx += 1

        return output
