# elemnts only of different b can change their position, so in a scenario with
# only one b and plenty of a, we can sort all elements of a using the ideia of
# selection sort. Using the same ideia, we can sort all elements with b = 1
# afterwards. The only case were isn't possible to sort is when all elements
# has the same b, in that case they must be already in ascending order.

# get number of test cases
testCases = int(input())

# for each test case
while testCases > 0:

    # read array size
    size = int(input())

    # read both arrays
    elements = list(map(int, input().split()))
    pairity = list(map(int, input().split()))

    # check if parity in unique
    zeroParity = False
    oneParity = False
    for b in pairity:
        if b == 0:
            zeroParity = True
        else:
            oneParity = True

    # both are true (since size >= 1, at least one will be true, so they can't
    #                be here both false)
    if zeroParity == oneParity:
        print('Yes')

    # array only with 0 or 1 -> elements must be sorted
    else:
        ordered = True
        for i in range(size - 1):
            if elements[i] > elements[i + 1]:
                ordered = False
                break

        # print response
        if ordered is True:
            print('Yes')
        else:
            print('No')

    # decrese test cases
    testCases -= 1
