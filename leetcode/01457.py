# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/?envType=daily-question&envId=2024-01-24

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def is_pseudo_palindromic(self):
        odd = False
        for digit_count in self.digit_count.values():
            if digit_count % 2 == 1:
                if odd is True:
                    return False
                odd = True
        return True

    def recursion(self, node):
        if node == None:
            return 0

        self.digit_count[node.val] += 1

        if node.left == None and node.right == None:
            if self.is_pseudo_palindromic():
                self.digit_count[node.val] -= 1
                return 1
            self.digit_count[node.val] -= 1
            return 0

        left = self.recursion(node.left)
        right = self.recursion(node.right)

        self.digit_count[node.val] -= 1
        return left + right


    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.digit_count = {digit: 0 for digit in range(1, 10)}
        return self.recursion(root)
