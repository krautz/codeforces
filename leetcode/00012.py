# https://leetcode.com/problems/integer-to-roman/submissions/1146336558/
class Solution:
    def intToRoman(self, num: int) -> str:
        output = ""
        while num != 0:
            if num - 1000 >= 0:
                output += "M"
                num -= 1000
                continue
            if num - 900 >= 0:
                output += "CM"
                num -= 900
                continue
            if num - 500 >= 0:
                output += "D"
                num -= 500
                continue
            if num - 400 >= 0:
                output += "CD"
                num -= 400
                continue
            if num - 100 >= 0:
                output += "C"
                num -= 100
                continue
            if num - 90 >= 0:
                output += "XC"
                num -= 90
                continue
            if num - 50 >= 0:
                output += "L"
                num -= 50
                continue
            if num - 40 >= 0:
                output += "XL"
                num -= 40
                continue
            if num - 10 >= 0:
                output += "X"
                num -= 10
                continue
            if num - 9 >= 0:
                output += "IX"
                num -= 9
                continue
            if num - 5 >= 0:
                output += "V"
                num -= 5
                continue
            if num - 4 >= 0:
                output += "IV"
                num -= 4
                continue
            output += "I"
            num -= 1
        return output
