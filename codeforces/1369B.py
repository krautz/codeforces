# TLE -> check cpp version

testCases = int(input())

while testCases > 0:

    size = int(input())

    string = input()

    solution = ''

    one = False
    zero = False
    pos = None
    for i in range(size - 1, -1, -1):

        if string[i] == '1' and one == False and zero == False:
            solution = '1' + solution

        if string[i] == '0' and one == False and zero == False:
            zero = True
            pos = i

        if string[i] == '1' and one == False and zero == True:
            one = True

        if string[i] == '0' and one == True and zero == True:
            string = string[:i + 1] + '0' + string[i + 2:]
            pos = i + 1
            one = False

    if one == False and zero == True:
        solution = string[:pos + 1] + solution

    elif one == True and zero == True:
        solution = '0' + solution

    print(solution)
    testCases -= 1
