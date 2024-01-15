# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        output = ListNode()
        current_output = output
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            current_output.val = l1_val + l2_val + carry
            if current_output.val >= 10:
                current_output.val -= 10
                carry = 1
            else:
                carry = 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if l1 or l2:
                current_output.next = ListNode()
                current_output = current_output.next
        if carry == 1:
            current_output.next = ListNode(val=1)
        return output
