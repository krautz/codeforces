"""
Heap Sort algorithm using heapq from standard library.

Time Complexity: O(n * log(n))

Space Complexity: O(n)
"""
import heapq

def heapsort(list):

    # turn element into a min heap
    heapq.heapify(list)

    # remove smallest element from heap and add to result
    result = []
    while len(list) > 0:
        result.append(heapq.heappop(list))

    # return ordered list
    return result

if __name__ == '__main__':

    # get input list
    list = list(map(int, input('Insert list to be ordered\n').split()))

    # print sorted list
    print(heapsort(list))
