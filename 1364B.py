# To find the biggest difference, we must retrieve the extremes of each
# ascending and descinding sequences

# read test cases
testCases = int(input())

while testCases > 0:

    # get size of permutation
    size = int(input())

    # get permutation
    permutation = list(map(int, input().split()))

    # start subsequence with first element of permutation
    subsequence = [permutation[0]]

    # get if added element of subsequence is bigger then its following element
    if permutation[0] > permutation[1]:
        operation = 'bigger'
    else:
        operation = 'smaller'

    # iterate over permutation
    for i in range(1, size - 1):

        # operation remains the same -> skip to next element
        if (operation == 'bigger' and permutation[i] > permutation [i + 1]) or (operation == 'smaller' and permutation[i] < permutation [i + 1]):
            continue

        # add element to subsequence since it has biggest diff on ascending or
        # descinding sequence
        subsequence.append(permutation[i])

        # update next operation
        if operation == 'bigger':
            operation = 'smaller'
        else:
            operation = 'bigger'

    # add last element of sequence
    subsequence.append(permutation[-1])

    # print response
    print(len(subsequence))
    for i in range(len(subsequence)):
        if i == len(subsequence) - 1:
            print(str(subsequence[i]))
        else:
            print(str(subsequence[i]) + ' ', end = '')

    # decrement test cases
    testCases -= 1
