# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
from typing import List
class Solution:
    def get_new_output(self, outputs, char_options):
        new_outputs = []
        for output in outputs:
            for char in char_options:
                new_outputs.append(output + char)
        return new_outputs

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        outputs = [""]
        for digit in digits:
            if digit == "2":
                outputs = self.get_new_output(outputs, "abc")
            if digit == "3":
                outputs = self.get_new_output(outputs, "def")
            if digit == "4":
                outputs = self.get_new_output(outputs, "ghi")
            if digit == "5":
                outputs = self.get_new_output(outputs, "jkl")
            if digit == "6":
                outputs = self.get_new_output(outputs, "mno")
            if digit == "7":
                outputs = self.get_new_output(outputs, "pqrs")
            if digit == "8":
                outputs = self.get_new_output(outputs, "tuv")
            if digit == "9":
                outputs = self.get_new_output(outputs, "wxyz")
        return outputs
