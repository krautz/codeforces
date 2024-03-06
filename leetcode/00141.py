# https://leetcode.com/problems/linked-list-cycle/?envType=daily-question&envId=2024-03-06


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def advance_two(self, node: ListNode) -> Optional[ListNode]:
        next_node = node.next
        if next_node:
            return next_node.next
        return next_node
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        one_by_one = head
        two_by_two = head.next if head else None
        while two_by_two:
            if one_by_one == two_by_two:
                return True
            one_by_one = one_by_one.next
            two_by_two = self.advance_two(two_by_two)
        return False
