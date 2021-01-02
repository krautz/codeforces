"""
Quick Sort algorithm.

Time Complexity:
    Worst: O(n^2)
    Average: O(n * log(n))

Space Complexity: O(n)
"""

def swap(list, i, j):
    swap = list[j]
    list[j] = list[i]
    list[i] = swap

def quicksort(list, begin, end):

    # empty sublist: return
    if begin > end:
        return

    # one element in sublist: return
    if begin == end:
        return

    # quick sort current list
    i = begin
    j = begin
    while i != end:

        # current element smaller than pivot: put it before pivot
        if list[i] <= list[end]:
            swap(list, i, j)
            j += 1

        # move in the list
        i += 1

    # put pivot in right place
    swap(list, j, end)

    # divide step
    quicksort(list, begin, j - 1)
    quicksort(list, j + 1, end)


if __name__ == '__main__':

    # get input list
    list = list(map(int, input('Insert list to be ordered\n').split()))

    # sort list
    quicksort(list, 0, len(list) - 1)

    # print sorted list
    print(list)
