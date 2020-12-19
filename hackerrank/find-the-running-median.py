"""
Problem: https://www.hackerrank.com/challenges/find-the-running-median/problem
"""

#
# CODE
#
class MaxHeap():

    def __init__(self):
        """
        I initialize an empty max heap.

        :returns: nothing
        """
        self.heap = []

    def add(self, element):
        """
        I add an elemente to the max heap.

        :param element: element to be add.

        :returns: nothing
        """
        # add element to the heap
        self.heap.append(element)

        # get index of added element and parent of added element
        index = len(self.heap) - 1
        parentIndex = (index - 1) // 2

        # swap parents and childs while needed
        while index >= 1 and self.heap[parentIndex] < self.heap[index]:

            # swap parent and child
            swap = self.heap[parentIndex]
            self.heap[parentIndex] = self.heap[index]
            self.heap[index] = swap

            # update parent and child indexes
            index = parentIndex
            parentIndex = (index - 1) // 2


    def remove(self):
        """
        I remove an elemente of max heap.

        :returns: removed element or None on empty heap
        """
        # non empty heap: get first element
        if len(self.heap) > 0:
            removed = self.heap[0]

        # empty heap: return None
        else:
            return None

        # heap with one element: remove it and return
        if len(self.heap) == 1:
            return self.heap.pop()

        # put last element on the begining of the heap
        self.heap[0] = self.heap.pop()

        # descend new root while needed
        index = 0
        leftChild = (2 * index) + 1
        rightChild = (2 * index) + 2
        while (leftChild < len(self.heap) and \
              self.heap[index] < self.heap[leftChild]) or \
              (rightChild < len(self.heap) and \
              self.heap[index] < self.heap[rightChild]):

                # swap smallest child with parent
                if rightChild == len(self.heap) or \
                   self.heap[leftChild] > self.heap[rightChild]:

                    # swap with left child
                    swap = self.heap[index]
                    self.heap[index] = self.heap[leftChild]
                    self.heap[leftChild] = swap

                    # update indexes
                    index = leftChild
                    leftChild = (2 * index) + 1
                    rightChild = (2 * index) + 2

                else:

                    # swap with right child
                    swap = self.heap[index]
                    self.heap[index] = self.heap[rightChild]
                    self.heap[rightChild] = swap

                    # update indexes
                    index = rightChild
                    leftChild = (2 * index) + 1
                    rightChild = (2 * index) + 2

        # return removed node
        return removed


    def size(self):
        """
        I return the size of the heap.

        :returns: size of the heap
        """
        return len(self.heap)


    def top(self):
        """
        I return the top element of the heap.

        :returns: top element of the heap or None on empty heap
        """
        if len(self.heap) > 0:
            return self.heap[0]

        return None


class MinHeap():

    def __init__(self):
        """
        I initialize an empty min heap.

        :returns: nothing
        """
        self.heap = []

    def add(self, element):
        """
        I add an elemente to the min heap.

        :param element: element to be add.

        :returns: nothing
        """
        # add element to the heap
        self.heap.append(element)

        # get index of added element and parent of added element
        index = len(self.heap) - 1
        parentIndex = (index - 1) // 2

        # swap parents and childs while needed
        while index >= 1 and self.heap[parentIndex] > self.heap[index]:

            # swap parent and child
            swap = self.heap[parentIndex]
            self.heap[parentIndex] = self.heap[index]
            self.heap[index] = swap

            # update parent and child indexes
            index = parentIndex
            parentIndex = (index - 1) // 2


    def remove(self):
        """
        I remove an elemente of min heap.

        :returns: removed element or None on empty heap
        """
        # non empty heap: get first element
        if len(self.heap) > 0:
            removed = self.heap[0]

        # empty heap: return None
        else:
            return None

        # heap with one element: remove it and return
        if len(self.heap) == 1:
            return self.heap.pop()

        # put last element on the begining of the heap
        self.heap[0] = self.heap.pop()

        # descend new root while needed
        index = 0
        leftChild = (2 * index) + 1
        rightChild = (2 * index) + 2
        while (leftChild < len(self.heap) and \
              self.heap[index] > self.heap[leftChild]) or \
              (rightChild < len(self.heap) and \
              self.heap[index] > self.heap[rightChild]):

                # swap smallest child with parent
                if rightChild == len(self.heap) or \
                   self.heap[leftChild] < self.heap[rightChild]:

                    # swap with left child
                    swap = self.heap[index]
                    self.heap[index] = self.heap[leftChild]
                    self.heap[leftChild] = swap

                    # update indexes
                    index = leftChild
                    leftChild = (2 * index) + 1
                    rightChild = (2 * index) + 2

                else:

                    # swap with right child
                    swap = self.heap[index]
                    self.heap[index] = self.heap[rightChild]
                    self.heap[rightChild] = swap

                    # update indexes
                    index = rightChild
                    leftChild = (2 * index) + 1
                    rightChild = (2 * index) + 2

        # return removed node
        return removed


    def size(self):
        """
        I return the size of the heap.

        :returns: size of the heap
        """
        return len(self.heap)


    def top(self):
        """
        I return the top element of the heap.

        :returns: top element of the heap or None on empty heap
        """
        if len(self.heap) > 0:
            return self.heap[0]

        return None


# read ammount of elements to be added
ammount = int(input())

# initialize maxheap to store "bigger of smallest" elements
maxHeap = MaxHeap()

# initialize minheap to store "samllest of biggest" elements
minHeap = MinHeap()

# print('------------')

for _ in range(ammount):

    # get new element
    element = int(input())

    # add element to proper heap
    smallestOfBiggest = minHeap.top()
    if smallestOfBiggest != None and element >= smallestOfBiggest:
        minHeap.add(element)
    else:
        maxHeap.add(element)

    # balance heaps
    minSize = minHeap.size()
    maxSize = maxHeap.size()
    if minSize - maxSize  == 2:
        balance = minHeap.remove()
        maxHeap.add(balance)
        print((minHeap.top() + maxHeap.top()) / 2)

    elif maxSize - minSize  == 2:
        balance = maxHeap.remove()
        minHeap.add(balance)
        print((minHeap.top() + maxHeap.top()) / 2)

    elif minSize - maxSize  == 1:
        print(minHeap.top() / 1)

    elif maxSize - minSize == 1:
        print(maxHeap.top() / 1)

    else:
        print((minHeap.top() + maxHeap.top()) / 2)
    #
    # print('smallest of biggest: ', minHeap.heap)
    # print('biggest of smallest: ', maxHeap.heap)
    # print('------------')
