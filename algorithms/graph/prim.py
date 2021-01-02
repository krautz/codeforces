"""
Prim's minimum spanning tree implementation.

Application: Graph algorithm to find minimum spanning tree.

Time Complexity: O(E * log(V)):
    1 - We need to build the heap with all vertices -> O(V * log(V))
    2 - We relax all edges -> O(E * log(V))
    3 - We remove each vertex from the heap -> O(V * log(V))

Space complexity: O(V + E)

Graph is undirected and represented by an adjacency list: each node identifier
is a key of a dictonary and its value is the adjacency list of that node.

Algorithm: We start from the source and relax all the edges that it has. We
store the value of the smallest edge to each node in a min heap. We always
remove the smallest element from the heap. It represents the smallest edge
to reach that node, as any other path will have a higher edge sum value, as any
other path already has a higher value and a path can only increase to reach the
target node. When the heap is empty, or its top value is infinite, then we have
reached all nodes that are reacheable by the source.

Problem to get input from:
https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/

Input:
n -> number of nodes (starting from 0)
s -> source node (0 <= s < n)
e -> number of edges
e next lines with a b d -> edge connecting node a to b with distance d.
0 <= a and b < n

Example (from link):
9
0
14
0 1 4
0 7 8
1 7 11
1 2 8
7 8 7
7 6 1
2 8 2
8 6 6
6 5 2
2 3 7
2 5 4
3 5 14
3 4 9
5 4 10
"""

#
# IMPORTS
#
import math


#
# CODE
#

class MinHeap():

    def __init__(self, list = []):
        """
        I initialize an empty min heap.
        Each element is a tuple with (id, shortestdistance) of a node

        :param list: list to initialize heap

        :returns: nothing
        """
        # initialize empty heap
        self.heap = []

        # initialize empty dict to store each node's position in heap list
        self.position = dict()

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
        # update their position
        iId = self.heap[i][0]
        jId = self.heap[j][0]
        self.position[iId] = j
        self.position[jId] = i

        # swap elements
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


    def add(self, element):
        """
        I add an elemente to the min heap.

        :param element: element to be add, tuple of node id and distance.

        :returns: nothing
        """
        # add element to the heap
        self.heap.append(element)
        self.position[element[0]] = len(self.heap) - 1

        # get index of added element and parent of added element
        index = len(self.heap) - 1
        parentIndex = (index - 1) // 2

        # swap parents and childs while needed
        while index >= 1 and self.heap[parentIndex][1] > self.heap[index][1]:

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
            del self.position[removed[0]]

        # empty heap: return None
        else:
            return None

        # heap with one element: remove it and return
        if len(self.heap) == 1:
            self.heap.pop()
            return removed

        # put last element on the begining of the heap
        self.heap[0] = self.heap.pop()
        self.position[self.heap[0][0]] = 0

        # descend new root while needed
        index, leftChild, rightChild = self.getChilds(0)
        while (leftChild < len(self.heap) and \
              self.heap[index][1] > self.heap[leftChild][1]) or \
              (rightChild < len(self.heap) and \
              self.heap[index][1] > self.heap[rightChild][1]):

                # swap smallest child with parent
                if rightChild == len(self.heap) or \
                   self.heap[leftChild][1] < self.heap[rightChild][1]:

                    # swap with left child
                    self.swap(index, leftChild)

                    # update indexes
                    index, leftChild, rightChild = self.getChilds(leftChild)

                else:

                    # swap with left child
                    self.swap(index, rightChild)

                    # update indexes
                    index, leftChild, rightChild = self.getChilds(rightChild)

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
        # get element and its parent indexes
        index = self.position[element]
        parentIndex = (index - 1) // 2

        # update its cost
        self.heap[index] = (element, cost)

        # swap parents and childs while needed
        while index >= 1 and self.heap[parentIndex][1] > self.heap[index][1]:

            # swap parent and child
            self.swap(parentIndex, index)

            # update parent and child indexes
            index = parentIndex
            parentIndex = (index - 1) // 2


def relax(finished, distances, parents, heap, source, target, distance):
    """
    I relax a node given an edge.

    :param finished: array indicating if a node is already in the spanning tree
    :param distances: array with smallest distances from source to each node
    :param parents: smallest path tree
    :param heap: heap with smallest distances to each node from source
    :param source: source node id
    :param target: target node id
    :param distance: edge cost from source to target

    :returns: nothing
    """
    # the current edge is smaller than the current samallest to target: update
    if finished[target] == False and distances[target] > distance:
        distances[target] = distance
        parents[target] = source
        heap.decreaseKey(target, distance)


if __name__ == '__main__':

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

    # initialized nodes that are already in the spanning tree
    finished = [False] * nodes
    finished[source] = True

    # initialize cut nodes
    cut = MinHeap()
    for node in range(nodes):
        cut.add((node, distances[node]))

    # execute djikstra
    while cut.size() > 0 and cut.top() != math.inf:

        # get node with smallest distance to source
        node = cut.remove()
        finished[node[0]] = True

        # relax each edge of node
        for edge in graph[node[0]]:
            relax(finished, distances, parents, cut, node[0], edge[0], edge[1])

    # print distance and parent of each node
    for node in range(nodes):
        print('---------------')
        print(f'Nó {node} - Menor aresta: {distances[node]}')
        print(f'Nó {node} - Pai: {parents[node]}')
    print('---------------')
