"""
Problem: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

Input:
n
s
e
a b d

n -> number of nodes (starting from 0)
s -> source node (0 <= s < n)
e -> number of edges
e next lines with a b d -> edge connecting node a to b with distance d.
0 <= a and b < n
"""

#
# IMPORTS
#
import math


#
# CODE
#

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

        :param element: element to be add, tuple of node id and distance.

        :returns: nothing
        """
        # add element to the heap
        self.heap.append(element)

        # get index of added element and parent of added element
        index = len(self.heap) - 1
        parentIndex = (index - 1) // 2

        # swap parents and childs while needed
        while index >= 1 and self.heap[parentIndex][1] > self.heap[index][1]:

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
              self.heap[index][1] > self.heap[leftChild][1]) or \
              (rightChild < len(self.heap) and \
              self.heap[index][1] > self.heap[rightChild][1]):

                # swap smallest child with parent
                if rightChild == len(self.heap) or \
                   self.heap[leftChild][1] < self.heap[rightChild][1]:

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


    def decreaseKey(self, element, cost):
        """
        I decrease the value of an element.

        :param element: element to have its key decreased
        :param cost: new element cost

        :returns: nothing
        """
        # find desired element
        for node in range(len(self.heap)):

            # found node: decrease its key
            if self.heap[node][0] == element:

                # update its cost
                self.heap[node] = (element, cost)

                # get index of added element and parent of added element
                index = node
                parentIndex = (index - 1) // 2

                # swap parents and childs while needed
                while index >= 1 and self.heap[parentIndex][1] > self.heap[index][1]:

                    # swap parent and child
                    swap = self.heap[parentIndex]
                    self.heap[parentIndex] = self.heap[index]
                    self.heap[index] = swap

                    # update parent and child indexes
                    index = parentIndex
                    parentIndex = (index - 1) // 2


def relax(distances, parents, heap, source, target, distance):
    """
    I relax a node given an edge.

    :param distances: array with smallest distances from source to each node
    :param parents: smallest path tree
    :param heap: heap with smallest distances to each node from source
    :param source: source node
    :param target: target node
    :param distance: edge cost from source to target

    :returns: nothing
    """
    # the current edge offers a better path to target: update it
    if distances[target] > distances[source] + distance:
        distances[target] = distances[source] + distance
        parents[target] = source
        heap.decreaseKey(target, distances[target])


# read input
nodes = int(input())
source = int(input())
edges = int(input())

# build empty graph as adjacency list
graph = []
for _ in range(nodes):
    graph.append([])

# populate graph
for _ in range(edges):
    a, b, distance  = map(int, input().split())
    graph[a].append((b, distance))
    graph[b].append((a, distance))

# initialize distances from source list
distances = [math.inf] * nodes
distances[source] = 0

# initialize parent of shortest path tree list
parents = [-1] * nodes
parents[source] = None

# initialize cut nodes
cut = MinHeap()
for node in range(nodes):
    cut.add((node, distances[node]))

print(cut.heap)

# execute djikstra
while cut.size() > 0:

    # get node with smallest distance to source
    node = cut.remove()

    # relax each edge of node
    for edge in graph[node[0]]:
        relax(distances, parents, cut, node[0], edge[0], edge[1])

# print distance and parent of each node
for node in range(nodes):
    print('---------------')
    print(f'Nó {node} - Distancia: {distances[node]}')
    print(f'Nó {node} - Pai: {parents[node]}')
print('---------------')
