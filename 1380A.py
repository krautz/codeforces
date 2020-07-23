# The ideia is, from left to right, find the smallest element in descending
# order. After this element, find the biggest in the following ascending order.
# If after the ascending order there is a smaller element then him, then just
# found the sollution.

# get number of test cases
testCases = int(input())

# for each test
while testCases > 0:

    # read number of elements in this test case and the elements
    size = int(input())
    elements = list(map(int, input().split()))

    # initialize indexes
    i = 0
    j = -1

    # set flags to each step
    smallestLeft = False
    biggestMiddle = False

    # transverse through array
    for m in range(size):

        # smallest left element not found yet
        if smallestLeft == False:

            # current element is smallest than the smallest found: update it
            if elements[m] < elements[i]:
                i = m

            # current element is bigger than the smallest: set biggest middle
            if elements[m] > elements[i]:
                j = m
                smallestLeft = True

            # element used, get next one
            continue

        # biggest middle element found
        if biggestMiddle == False:

            # current element is bigger than the biggest: set biggest middle
            if elements[m] > elements[j]:
                j = m

            # current element is smaller than the biggest found: print response
            if elements[m] < elements[j]:
                print('YES')
                print(i + 1, j + 1 , m + 1)
                biggestMiddle = True
                break

            # element used, get next one
            continue

    # no answer found: print no
    if biggestMiddle == False:
        print('NO')


    # decrement test cases
    testCases -= 1
