# The ideia of this code is that an element can only be changed to 1 if its
# row and columns only contains 0s, so, when it is changed to one, none of the
# elements on this column or row can be changed to 1, thus, it invalidates
# both the row and the colum.
#
# With that said, the ideia then is to count the number of rows and columns with
# zeros, and the minumum of those two are the number of plays that can be made.

# read number of test cases
testCases = int(input())

# apply logic for each test case
while testCases > 0:

    # read number of rows and columns
    row, column = list(map(int, input().split()))

    # allocate space for the grid
    grid = []
    for i in range(row):
        grid.append(list(map(int, input().split())))

    # count number of rows with only zeros
    rowZeros = 0
    for i in range(row):

        found = False
        for j in range(column):

            if grid[i][j] == 1:
                found = True
                break

        if found is False:
            rowZeros += 1

    # count number of columns with only zeros
    columnZeros = 0
    for j in range(column):

        found = False
        for i in range(row):

            if grid[i][j] == 1:
                found = True
                break

        if found is False:
            columnZeros += 1

    # get minimum of them
    minimum = min(rowZeros, columnZeros)

    # print response based on number of possible plays
    if minimum % 2 == 0:
        print('Vivek')
    else:
        print('Ashish')

    testCases -= 1
