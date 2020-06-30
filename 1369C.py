testCases = int(input())

while testCases > 0:

    nNumbers, nFriends = list(map(int, input().split()))

    numbers = list(map(int, input().split()))
    numbers.sort()

    friends = list(map(int, input().split()))
    friends.sort()

    smallest = 0
    biggest = nNumbers - 1
    sum = 0
    for friend in friends:

        if friend >= 3:
            break

        if friend == 1:
            sum += 2 * numbers[biggest]
            biggest -= 1

        if friend == 2:
            sum += numbers[biggest]
            biggest -= 1
            sum += numbers[biggest]
            biggest -= 1

    friends.reverse()

    for friend in friends:

        if friend <= 2:
            break

        sum += numbers[biggest] + numbers[smallest]
        biggest -= 1
        smallest += friend - 1

    print(sum)
    testCases -= 1;
