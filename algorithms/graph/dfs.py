"""
DFS - Depth First Search implementation.

Application: Find all nodes reachable by a source. Used for plenty of
algorithms like topological sort, finding conected components of a graph and
topological sort.

Time Complexity: O(V + E):  We visit each node once and check all edges

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
1
6
0 1
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
def dfs(node, parent, graph, parents, start, end, time):
    """
    I recuservly perform dfs.

    :param node: current node
    :param parent: parent node of current nome
    :param graph: graph
    :param parents: nodes parents in dfs tree
    :param start: start time of each node
    :param end: end time of each node
    :param time: current time

    :returns: nothing
    """
    # node already visited: return current time
    if parents[node] != -1:
        return time

    # set start time of current node
    time += 1
    start[node] = time
    parents[node] = parent

    # visit each node neighbour
    for neighbour in graph[node]:
        time = dfs(neighbour, node, graph, parents, start, end, time)

    # set end time
    time += 1
    end[node] = time

    # return time
    return time


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

    # initialize parent of dfs tree list
    parents = [-1] * nodes

    # initialize start times
    start = [-1] * nodes

    # initialize start times
    end = [-1] * nodes

    dfs(source, None, graph, parents, start, end, 0)

    # print distance and parent of each node
    for node in range(nodes):
        print('---------------')
        print(f'Nó {node} - Inicio: {start[node]}')
        print(f'Nó {node} - Fim: {end[node]}')
        print(f'Nó {node} - Pai: {parents[node]}')
    print('---------------')
