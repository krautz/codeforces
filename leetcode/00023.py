# https://leetcode.com/problems/merge-k-sorted-lists/description/

from typing import Callable, TypeVar, List, Optional

Item = TypeVar("Item")


class MinHeap():
    def __init__(self, attr_getter: Callable = lambda x: x):
        self.attr_getter = attr_getter

    def heapify(self, items: list[Item]) -> list[Item]:
        heap = []
        for item in items:
            self.push(heap, item)
        return heap

    def _swap(self, heap: list[Item], i: int, j: int):
        swap = heap[i]
        heap[i] = heap[j]
        heap[j] = swap

    def _get_left_child_index(self, index: int) -> int:
        return (2 * index) + 1

    def _get_right_child_index(self, index: int) -> int:
        return (2 * index) + 2

    def _get_parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def push(self, heap: list[Item], item: Item):
        # add element to the heap
        heap.append(item)

        # get index of added element and parent of added element
        current_index = len(heap) - 1
        parent_index = self._get_parent_index(current_index)

        # swap current item with his parent while needed
        while current_index >= 1 and self.attr_getter(heap[parent_index]) > self.attr_getter(heap[current_index]):

            # swap current item with parent item
            self._swap(heap, parent_index, current_index)

            # update current item index and parent item index
            current_index = parent_index
            parent_index = self._get_parent_index(current_index)


    def pop(self, heap: list[Item]) -> Item:
        # get top element
        if len(heap) > 1:
            top = heap[0]
        elif len(heap) == 1:
            return heap.pop()
        else:
            return None

        # put last element on the begining of the heap
        heap[0] = heap.pop()

        # descend new root while needed
        current_index = 0
        left_child_index = self._get_left_child_index(current_index)
        right_child_index = self._get_right_child_index(current_index)
        while (
            (
                left_child_index < len(heap)
                and self.attr_getter(heap[current_index]) > self.attr_getter(heap[left_child_index])
            ) or (
                right_child_index < len(heap)
                and self.attr_getter(heap[current_index]) > self.attr_getter(heap[right_child_index])
            )
        ):

                # no right child or left child bigger than right one
                if (
                    right_child_index >= len(heap)
                    or self.attr_getter(heap[left_child_index]) < self.attr_getter(heap[right_child_index])
                ):
                    self._swap(heap, current_index, left_child_index)
                    current_index = left_child_index
                    left_child_index = self._get_left_child_index(current_index)
                    right_child_index = self._get_right_child_index(current_index)
                else:
                    self._swap(heap, current_index, right_child_index)
                    current_index = right_child_index
                    left_child_index = self._get_left_child_index(current_index)
                    right_child_index = self._get_right_child_index(current_index)

        # return top node
        return top


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heapq = MinHeap(lambda node: node.val)

        heap = heapq.heapify([head for head in lists if head])

        if not heap:
            return None

        head = heapq.pop(heap)
        if head.next:
            heapq.push(heap, head.next)

        current_node = head
        while heap:
            next_node = heapq.pop(heap)
            if next_node.next:
                heapq.push(heap, next_node.next)
            current_node.next = next_node
            current_node = next_node

        return head
