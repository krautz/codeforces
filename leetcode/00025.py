# https://leetcode.com/problems/reverse-nodes-in-k-group/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def get_k_next_nodes(self, current_node, k):
        group = []
        while current_node and k:
            group.append(current_node)
            current_node = current_node.next
            k -= 1
        return group

    def reverse_group(self, group, k):
        if len(group) != k:
            return

        group.reverse()
        for idx in range(len(group) - 1):
            group[idx].next = group[idx + 1]

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head = head
        for _ in range(k - 1):
            new_head = new_head.next

        groups = []
        current_node = head
        while current_node:
            k_next_nodes = self.get_k_next_nodes(current_node, k)
            groups.append(k_next_nodes)
            current_node = k_next_nodes[-1].next

        for group in groups:
            self.reverse_group(group, k)

        for idx in range(len(groups) - 1):
            groups[idx][-1].next = groups[idx + 1][0]
        groups[-1][-1].next = None

        return new_head


class SolutionWithRecursion:
    def reverse_k_group(self, last_node_previous_group, prev_node, current_node, remaining_k):
        if current_node == None:
            return False

        if remaining_k == 0:
            first_node_of_next_group = current_node.next
            current_node.next = prev_node

            if last_node_previous_group:
                last_node_previous_group.next = current_node

            return first_node_of_next_group

        first_node_of_next_group = self.reverse_k_group(last_node_previous_group, current_node, current_node.next, remaining_k - 1)

        if first_node_of_next_group is not False:
            if not prev_node:
                current_node.next = first_node_of_next_group
            else:
                current_node.next = prev_node

        return first_node_of_next_group

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head = head
        for _ in range(k - 1):
            new_head = new_head.next

        current_node = head
        last_node_previous_group = None
        while current_node:
            result = self.reverse_k_group(last_node_previous_group, None, current_node, k - 1)
            last_node_previous_group = current_node
            current_node = result

        return new_head
