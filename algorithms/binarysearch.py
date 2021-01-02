"""
Binary Search implementation.

Application: Find an element in a list

Time Complexity:
    1 - Nonsorted list: O(n * log(n)): We sort the list and perform the search
    2 - Sorted list: O(log(n)): We just perform the search

Space complexity: O(n)

Algorithm: We sort the list, we check if the element is in the middle of the
list. If it is, we return it. If not, if the searched element is smaller than
the middle we search on the left portion of the list, otherwise we search on
the right portion of the list.

Input:
list elements
element to search

Example:
10 2 1 5 4 8 7 9 6 3
2
"""
#
# CODE
#
def binarySearch(list, start, end, value):
    """
    I recuservly perform dfs.

    :param list: list to search element on
    :param start: first index to search on
    :param end: last index to search on
    :param value: value to serch on

    :returns: index of value if it exists. None otherwise
    """
    # start bigger than end: value not found
    if start > end:
        return None

    # start smaller than end: get middle position
    middle = (start + end) // 2

    # value being searched is in the middle: return it
    if list[middle] == value:
        return middle

    # element is bigger than middle position: serach on right portion
    elif list[middle] < value:
        return binarySearch(list, middle + 1, end, value)

    # element is smaller than middle position: serach on left portion
    else:
        return binarySearch(list, start, middle - 1, value)


if __name__ == '__main__':

    # read input
    list = list(map(int, input().split()))
    value = int(input())

    # sort list
    list.sort()

    # print result
    print('Sorted list: ', list)
    print('Position of element: ', binarySearch(list, 0, len(list) - 1, value))
