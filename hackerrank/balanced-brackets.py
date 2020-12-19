"""
Problem: https://www.hackerrank.com/challenges/balanced-brackets/problem
"""

#
# CODE
#

# read ammount of test cases
testCases = int(input())

# solve each test case
for _ in range(testCases):

    # get brackets string
    text = input()

    # initialize empty pile to store
    pile = []

    # analyze each brackets string character
    for i in range(len(text)):

        # pile non empty: check for a match
        if len(pile) > 0:

            # pile top matches with current bracket character: remove pile top
            if (pile[-1] == '(' and text[i] == ')') or \
               (pile[-1] == '{' and text[i] == '}') or \
               (pile[-1] == '[' and text[i] == ']'):
                pile.pop()

            # pile top does not math with current bracket character: stack up curent bracket chracter
            else:
                pile.append(text[i])

        # empty pile: stack up curent bracket chracter
        else:
            pile.append(text[i])

    # empty pile: valid brackets string
    if (len(pile) == 0):
        print('YES')

    # non empty pile: invalid brackets string
    else:
        print('NO')
