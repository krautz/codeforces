"""
BFS - Breadth First Search implementation.

Application: Find smallest distance from a source node to all nodes. This
distance is in means of ammount of edges consumed

Time Complexity: O(V + E): We visit each node once and check all edges

Space complexity: O(V + E)

Graph is unweighted and directed and represented by an adjacency list: each
node identifier is a key of a dictonary and its value is the adjacency list of
that node.

Algorithm: We visit all unvisited neighbours of the current node (starting with
the source). For the visited node, we add all of its unvisited neighbours in the
end of a queue. The algorithm stops when the queue becomes empty.

Problem to get input from:
https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

Input:
n -> number of nodes (starting from 0)
s -> source node (0 <= s < n)
e -> number of edges
e next lines with a b d -> edge connecting node a to b with distance d.
0 <= a and b < n

Example (from link):
4
2
6
0 11
0 2
1 2
2 0
2 3
3 3
"""
#
# IMPORTS
#
import math


#
# CODE
#
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
        a, b  = map(int, input().split())
        graph[a].append(b)

    # initialize distances from source list
    distances = [math.inf] * nodes
    distances[source] = 0

    # initialize parent of shortest path tree list
    parents = [-1] * nodes
    parents[source] = None

    # initialize queue of nodes to visit
    queue = [source]

    # perform bfs until all reacheable nodes are reached
    while len(queue) > 0:

        # get first element of queue
        node = queue.pop()

        # add each unvisited neighbour to queue
        for neighbour in graph[node]:

            # neighbour already visited: skip it
            if parents[neighbour] != -1:
                continue

            # set neighbour as visited
            distances[neighbour] = distances[node] + 1
            parents[neighbour] = node
            queue.append(neighbour)

    # print distance and parent of each node
    for node in range(nodes):
        print('---------------')
        print(f'Nó {node} - Distancia: {distances[node]}')
        print(f'Nó {node} - Pai: {parents[node]}')
    print('---------------')
