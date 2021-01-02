"""
Merge Sort algorithm.

Time Complexity: O(n * log(n))

Space Complexity: O(n)
"""

def mergesort(list, begin, end):

    # empty sublist: return empty list
    if begin > end:
        return []

    # one element in sublist: return list with this element
    if begin == end:
        return [list[begin]]

    # divide step
    middle = (begin + end) // 2
    left = mergesort(list, begin, middle)
    right = mergesort(list, middle + 1, end)

    # conquer step
    result = []
    i = 0
    j = 0
    while i < len(left) or j < len(right):

        # right list already consumed: add left element to result
        if j == len(right):
            result.append(left[i])
            i += 1

        # left list already consumed: add right element to result
        elif i == len(left):
            result.append(right[j])
            j += 1

        # both lists still have elements: add the smaller one
        elif left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result


if __name__ == '__main__':

    # get input list
    list = list(map(int, input('Insert list to be ordered\n').split()))

    # print sorted list
    print(mergesort(list, 0, len(list) - 1))
