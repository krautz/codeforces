# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        offset_node = head
        for _ in range(n + 1):
            if offset_node:
                offset_node = offset_node.next
            else:
                return head.next

        current_node = head
        while offset_node:
            current_node = current_node.next
            offset_node = offset_node.next

        if current_node.next:
            current_node.next = current_node.next.next
        else:
            current_node.next = None

        return head

    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current_node = head
        while current_node:
            length += 1
            current_node = current_node.next

        index = length - n - 1
        if index == -1:
            return head.next


        current_node = head
        while index > 0:
            current_node = current_node.next
            index -= 1

        if current_node.next:
            current_node.next = current_node.next.next
        else:
            current_node.next = None
        return head
