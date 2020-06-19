# TLE test 3
# To find the biggest difference, we must retrieve the extremes of each
# ascending and descinding sequences

# read test cases
testCases = int(input())

while testCases > 0:

    # get n and x
    n, x = list(map(int, input().split()))

    # get array
    elements = list(map(int, input().split()))

    # initilize size of longes sub array
    longest = -1

    for i in range(n):

        sum = elements[i]

        if sum % x != 0 and longest == -1:
            longest = 1

        if n - i <= longest:
            continue

        for j in range(i + 1, n):

            sum += elements[j]

            if sum % x != 0 and (j - i + 1) > longest:
                longest = (j - i + 1)


    print(longest)

    # decrement test cases
    testCases -= 1
