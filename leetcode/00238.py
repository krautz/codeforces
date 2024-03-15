# https://leetcode.com/problems/product-of-array-except-self/description/?envType=daily-question&envId=2024-03-15

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # This is time O(n), but space O(n) as well
        left_mul = [1]
        for i in range(1, len(nums)):
            left_mul.append(left_mul[i - 1] * nums[i - 1])

        right_mul = [1]
        for i in range(len(nums) - 2, -1, -1):
            right_mul.append(right_mul[len(nums) - 2 - i] * nums[i + 1])
        right_mul.reverse()

        answer = []
        for i in range(len(nums)):
            answer.append(left_mul[i] * right_mul[i])
        return answer

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # This is time O(n), and space O(1)
        answer = [1] * len(nums)

        acc = 1
        for i in range(1, len(nums)):
            acc *= nums[i - 1]
            answer[i] *= acc

        acc = 1
        for i in range(len(nums) - 2, -1, -1):
            acc *= nums[i + 1]
            answer[i] *= acc

        return answer
