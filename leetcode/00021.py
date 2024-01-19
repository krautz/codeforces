# https://leetcode.com/problems/merge-two-sorted-lists/description/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def get_smallest_node(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            return list1
        return list2

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = self.get_smallest_node(list1, list2)
        if head and head == list1:
            list1 = list1.next
        elif head and head == list2:
            list2 = list2.next

        output = head
        while list1 or list2:
            output.next = self.get_smallest_node(list1, list2)
            output = output.next
            if output == list1:
                list1 = list1.next
            elif output == list2:
                list2 = list2.next

        return head
