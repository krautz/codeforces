"""
Bellman-Ford implementation.

Application: Graph algorithm to find shortest path from a source node.

Time Complexity: O(V * E): We relax all edges V - 1 times

Space complexity: O(V + E)

Graph is directed and represented by an adjacency list: each node identifier
is a key of a dictonary and its value is the adjacency list of that node.

Restriction: No cicles with negative cost

Algorithm: We relax all edges V - 1 times. With that, on the last time, we
guarantee that the shortest path from the source to the furthest target has
been relaxed in an optimal mode, and we have the shortest path tree

Problem to get input from:
https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/?ref=leftbar-rightbar

Input:
n -> number of nodes (starting from 0)
s -> source node (0 <= s < n)
e -> number of edges
e next lines with a b d -> edge connecting node a to b with distance d.
0 <= a and b < n

Example (from link):
5
0
8
0 1 -1
0 2 4
1 2 3
1 3 2
1 4 2
3 2 5
3 1 1
4 3 -3
"""

#
# IMPORTS
#
import math


#
# CODE
#
def relax(distances, parents, source, target, distance):
    """
    I relax a node given an edge.

    :param distances: array with smallest distances from source to each node
    :param parents: smallest path tree
    :param source: source node id
    :param target: target node id
    :param distance: edge cost from source to target

    :returns: nothing
    """
    # the current edge offers a better path to target: update it
    if distances[target] > distances[source] + distance:
        distances[target] = distances[source] + distance
        parents[target] = source


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

    # initialize distances from source list
    distances = [math.inf] * nodes
    distances[source] = 0

    # initialize parent of shortest path tree list
    parents = [-1] * nodes
    parents[source] = None

    # execute bellman ford
    for _ in range(nodes - 1):
        for node in range(nodes):
            for edge in graph[node]:
                relax(distances, parents, node, edge[0], edge[1])

    # check consistency (negative cicles)
    for node in range(nodes):
        for edge in graph[node]:

            # relax each edge and see if the result changes
            initialCost = distances[edge[0]]
            relax(distances, parents, node, edge[0], edge[1])
            finalCost = distances[edge[0]]

            # relax decreased distance: negative cicle, abort
            if initialCost != finalCost:
                print('Infinite negative cicle detected. Aborting')
                exit()

    # print distance and parent of each node
    for node in range(nodes):
        print('---------------')
        print(f'Nó {node} - Distancia: {distances[node]}')
        print(f'Nó {node} - Pai: {parents[node]}')
    print('---------------')
