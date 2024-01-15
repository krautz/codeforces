# https://leetcode.com/problems/swap-nodes-in-pairs/description/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = head.next

        first_node = head
        second_node = head.next
        third_node = head.next.next

        first_node.next = third_node
        second_node.next = first_node

        current_node = head
        while current_node and current_node.next and current_node.next.next:
            first_node = current_node
            second_node = current_node.next
            third_node = current_node.next.next
            fourth_node = current_node.next.next.next

            second_node.next = fourth_node
            third_node.next = second_node
            first_node.next = third_node

            current_node = current_node.next.next

        return new_head
