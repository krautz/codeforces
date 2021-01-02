"""
Min Heap implementation.

Complete (or almost) tree where the parent node is always smaller than its
childs.

Represented by a list. Given a node in the position i:
Parent is  in position (i - 1) // 2
Left child is in position (2 * i) + 1
Right child is in position (2 * i) + 2

Operations:
Build: O(n * log(n))
Insert element: O(log(n))
Remove min: O(log(n))
Update value: O(n) (find element -> O(n), change key O(log(n)))

Space complexity: O(n)

Applications:
Heap sort
Keep track of minimum element of a list
"""
class MinHeap():

    def __init__(self, list = []):
        """
        I initialize an empty min heap.

        :param list: list to initialize heap

        :returns: nothing
        """
        # initialize empty heap
        self.heap = []

        # initialize heap with provided list
        for element in list:
            self.add(element)


    def swap(self, i, j):
        """
        I swap two elements of the heap.

        :param i: index of first element
        :param j: index of second element

        :returns: nothing
        """
        swap = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = swap


    def getChilds(self, index):
        """
        I get the index of the childs of a node.

        :param index: index of the element to get childs from
        :param j: index of second element

        :returns: index, left child and right child indexes
        """
        return index, (2 * index) + 1, (2 * index) + 2


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
            self.swap(parentIndex, index)

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
        index, leftChild, rightChild = self.getChilds(0)
        while (leftChild < self.size() and \
              self.heap[index] > self.heap[leftChild]) or \
              (rightChild < self.size() and \
              self.heap[index] > self.heap[rightChild]):

                # swap smallest child with parent
                if rightChild == len(self.heap) or \
                   self.heap[leftChild] < self.heap[rightChild]:

                    # swap with left child and set current node as left child
                    self.swap(index, leftChild)
                    index, leftChild, rightChild = self.getChilds(leftChild)

                else:
                    # swap with right child and set current node as right child
                    self.swap(index, rightChild)
                    index, leftChild, rightChild = self.getChilds(rightChild)

        # return removed node
        return removed


def heapsort(list):

    # turn list into a min heap
    heap = MinHeap(list)

    # remove smallest element from heap and add to result
    result = []
    while heap.size() > 0:
        result.append(heap.remove())

    # return ordered list
    return result


if __name__ == '__main__':

    # get input list
    list = list(map(int, input('Insert list to be ordered\n').split()))

    # print sorted list
    print(heapsort(list))
