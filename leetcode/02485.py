# https://leetcode.com/problems/find-the-pivot-integer/description/?envType=daily-question&envId=2024-03-13

class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1, n + 1):
            if sum(range(i + 1)) == sum(range(i, n + 1)):
                return i
        return -1

    def pivotInteger(self, n: int) -> int:
        left = 1
        right = sum(range(n + 1))
        for i in range(1, n + 1):
            if left == right:
                return i
            left += i + 1
            right -= i
        return -1
