"""
Topological Sort implementation.

Application: Sort events when one event takes precedence over others

Time Complexity: O(V * E):  We visit each node once and check all edges

Space complexity: O(V * E)

Graph is unweighted and directed and represented by an adjacency list: each
node identifier is a key of a dictonary and its value is the adjacency list of
that node.

Algorithm: We visit all unvisited neighbours of the current node (starting with
the source). For the visited node, we add all of its unvisited neighbours in the
end of a queue. The algorithm stops when the queue becomes empty.

Problem to get input from:
https://www.geeksforgeeks.org/topological-sorting/

Input:
n -> number of nodes (starting from 0)
e -> number of edges
e next lines with a b d -> edge connecting node a to b with distance d.
0 <= a and b < n

Example (from link):
6
6
2 3
3 1
4 0
4 1
5 0
5 2
"""
#
# IMPORTS
#
import math


#
# CODE
#
def dfs(node, graph, visited, allVisited, result):
    """
    I recuservly perform dfs.

    :param node: current node
    :param graph: graph
    :param visited: nodes already visited in this traversal
    :param allVisited: node visited in any traversal
    :param result: topological sort result

    :returns: nothing
    """
    # node already visited in some traversal: cicle detected. abort
    if visited[node] == True:
        print('Graph is not acyclic')
        exit()

    # node already visited by any older traversal: ignore it
    if allVisited[node] == True:
        return

    # node not visited: set it as visited
    allVisited[node] = True
    visited[node] = True

    # visit each node neighbour
    for neighbour in graph[node]:
        dfs(neighbour, graph, visited, allVisited, result)

    # append node to result
    result.append(node)


if __name__ == '__main__':

    # read input
    nodes = int(input())
    edges = int(input())

    # build empty graph as adjacency list
    graph = []
    for _ in range(nodes):
        graph.append([])

    # populate graph
    for _ in range(edges):
        a, b  = map(int, input().split())
        graph[a].append(b)

    # initialize all nodes visited by dfs
    visited = [False] * nodes

    # initialize topological sort result
    result = []

    # perform topological sort
    for node in range(nodes):

        # node not yet visited: dfs it
        if visited[node] == False:
            dfs(node, graph, [False] * nodes, visited, result)

    # print topological sort of nodes
    result.reverse()
    print(result)
