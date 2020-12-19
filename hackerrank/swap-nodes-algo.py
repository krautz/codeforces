"""
Problem: https://www.hackerrank.com/challenges/swap-nodes-algo/problem
"""

#
# IMPORTS
#
# needed for recursive solution to work
import sys
sys.setrecursionlimit(15000)


#
# CODE
#
def inorderRecursive(indexes, i):
    """
    I print a binary tree in inorder traversal recursively.

    :param indexes: binary tree as a list of indexes
    :param i: current index being visited

    :return: nothing
    """
    # null node: return
    if i == -2:
        return

    # visit sub-left tree, print node and visit sub-right tree
    inorder(indexes, indexes[i][0])
    print(i + 1, end = ' ')
    inorder(indexes, indexes[i][1])


def inorderIterative(indexes):
    """
    I print a binary tree in inorder traversal iteratively.

    :param indexes: binary tree as a list of indexes

    :return: nothing
    """
    # create pile of nodes and append root to it
    nodes = []
    nodes.append(0)
    visited = [False] * 1024

    # while there is nodes to visit
    while len(nodes) > 0:

        # get top of the pile
        node = nodes[-1]

        # non null node and unvisited node: visit node and append its left child
        if indexes[node][0] != -2 and visited[node] == False:
            visited[node] = True
            nodes.append(indexes[node][0])

        # null node or visited node: print node data and append right child
        else:
            print(node + 1, end = ' ')
            nodes.pop()
            if indexes[node][1] != -2:
                nodes.append(indexes[node][1])


def inorderIterative2(indexes):
    """
    I print a binary tree in inorder traversal iteratively without visited list.

    :param indexes: binary tree as a list of indexes

    :return: nothing
    """
    # initialize pile of nodes and set current node as root
    nodes = []
    current = 0

    # print in order
    while True:

        # non null node: enpile current node and move to left child
        if current != -2:
            nodes.append(current)
            current = indexes[current][0]

        # null node with nodes on pile: remove pile top, print it and visit right child
        elif len(nodes) > 0:
            node = nodes.pop()
            print(node + 1, end = ' ')
            current = indexes[node][1]

        # empty pile and null node: stop
        else:
            break


# read number of nodes in tree
n = int(input())

# tree array
indexes = []

# heigh of node of index i
nodeHeight = [0] * n

# nodes in height j
heightNodes = [[0]]
for i in range(n):
    heightNodes.append([])

# build tree
for i in range(n):
    childs = list(map(lambda x: int(x) - 1, input().rstrip().split()))
    indexes.append(childs)
    for child in childs:
        if child != -2:
            nodeHeight[child] = nodeHeight[i] + 1
            heightNodes[nodeHeight[child]].append(child)

# get ammount of queries
queriesCount = int(input())

# execute each query
for _ in range(queriesCount):

    # get query
    query = int(input())

    # find all multiples of the query
    for i in range(n):

        # query multiple: swap nodes
        if (i + 1) % query == 0:
            for node in heightNodes[i]:
                indexes[node].reverse()

    # print answer
    # inorderRecursive(indexes, 0)
    # inorderIterative(indexes)
    inorderIterative2(indexes)
    print()
