# https://leetcode.com/problems/middle-of-the-linked-list/?envType=daily-question&envId=2024-03-08

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def advance_two(self, node: ListNode) -> Optional[ListNode]:
        next_node = node.next
        if next_node:
            return next_node.next
        return next_node

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        one_by_one = head
        two_by_two = head.next
        while two_by_two:
            one_by_one = one_by_one.next
            two_by_two = self.advance_two(two_by_two)
        return one_by_one
