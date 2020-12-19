# The ideia is that no bad guys can leave the maze and all good guys must.
# Since each person can move in N, E, S, W, we need to "trap" bad guys in
# order to not let them escape the maze. Once this is done, if all good guys
# can escape, then we're safe, otherwise it does not have solution. To see if
# all good guys can escape, we see via dfs if all good guys are reacheable
# trough the exit of the maze


#
# GLOBALS
#
GOOD = 0


# recursive method to check if someone can escape a maze or not
def dfs(maze, row, column, visited, i, j):

    global GOOD

    # out of boundary -> return
    if i == -1 or j == -1 or i == row or j == column:
        return

    # already visited place -> return
    if visited[i][j] == 1:
        return

    # reached a wall -> visit and return
    if maze[i][j] == '#':
        return

    # mark the place as visited
    visited[i][j] = 1

    # base case: reached exit -> visit and increase count
    if maze[i][j] == 'G':
        GOOD += 1

    # dfs north
    dfs(maze, row, column, visited, i - 1, j)

    # dfs west
    dfs(maze, row, column, visited, i, j - 1)

    # dfs south
    dfs(maze, row, column, visited, i + 1, j)

    # dfs east
    dfs(maze, row, column, visited, i, j + 1)


# get number of test cases
testCases = int(input())

# for each test case
while testCases > 0:

    # get maze dimensions
    row, column = list(map(int, input().split()))

    # read maze
    maze = []
    visited = []
    for i in range(row):
        maze.append(list(map(lambda i:i, input())))
        visited.append([0] * column)

    # trap bad guys and count good guys
    good = 0
    GOOD = 0
    fail = False
    for i in range(row):
        for j in range(column):

            # bad guy: trap it
            if maze[i][j] == 'B':

                # north block
                if i > 0 and maze[i - 1][j] == '.':
                    maze[i - 1][j] = '#'

                # east block
                if j < column - 1 and maze[i][j + 1] == '.':
                    maze[i][j + 1] = '#'

                # south block
                if i < row - 1 and maze[i + 1][j] == '.':
                    maze[i + 1][j] = '#'

                # west block
                if j > 0 and maze[i][j - 1] == '.':
                    maze[i][j - 1] = '#'

                # good guy neighbour: fail
                if (i > 0 and maze[i - 1][j] == 'G') or\
                   (j < column - 1 and maze[i][j + 1] == 'G') or\
                   (i < row - 1 and maze[i + 1][j] == 'G') or\
                   (j > 0 and maze[i][j - 1] == 'G'):
                    fail = True

            # good guy -> increase the good guys count
            elif maze[i][j] == 'G':
                good += 1

    # get number of good guys reachable by exit
    dfs(maze, row, column, visited, row - 1, column - 1)

    # print response
    if fail is True or GOOD != good:
        print('No')
    else:
        print('Yes')

    # decrease test cases count
    testCases -= 1
