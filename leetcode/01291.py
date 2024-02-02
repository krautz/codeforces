# https://leetcode.com/problems/sequential-digits/?envType=daily-question&envId=2024-02-02

from typing import List

class Solution:
    def get_first_sequential_digits_for_length(self, length: int) -> List[int]:
        return [digit for digit in range(1, length + 1)]

    def increment_digits(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            return self.get_first_sequential_digits_for_length(len(digits) + 1)
        return [digit + 1 for digit in digits]

    def get_low_first_sequential_digits(self, low: int) -> List[int]:
        digits = self.get_first_sequential_digits_for_length(len(str(low)))
        while self.convert_digits_into_number(digits) < low:
            digits = self.increment_digits(digits)
        return digits

    def convert_digits_into_number(self, digits: List[int]) -> int:
        number = 0
        for index, digit in enumerate(digits):
            power = len(digits) - index - 1
            number += digit * pow(10, power)
        return number

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = self.get_low_first_sequential_digits(low)
        answer = []

        while self.convert_digits_into_number(digits) <= high:
            answer.append(self.convert_digits_into_number(digits))
            digits = self.increment_digits(digits)

        return answer
