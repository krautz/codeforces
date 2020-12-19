testCases = int(input())

while testCases > 0:
    n = int(input())

    if n % 4 == 0:
        print('YES')
    else:
        print('NO')

    testCases -= 1
