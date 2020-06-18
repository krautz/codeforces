# we must perform a rotation in a first array A in order to obtain the most
# number of elements pairing (in the same position) on an array B.
# For that matter, we compute how much we need to rotate the array for each
# elemnt to match arrays A and B. After that, get the number of rotation that
# which will lead to most elements paired.

# get size of arrays
size = int(input())

# get elements in array A and B
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# add a tuple of element position to each element
for i in range(size):
    A[i] = (A[i], i)
    B[i] = (B[i], i)

# sort both arrays by ther elements
A.sort(key = lambda x: x[0])
B.sort(key = lambda x: x[0])

# initilize array of rotations
rotations = [0] * size

# compute rotations difference
for i in range(size):
    diff = A[i][1] - B[i][1]

    # rotation is to the left -> turn it to the right
    if diff < 0:
        diff = size + diff

    # increase matching elements on this rotation size
    rotations[diff] += 1

# print maximum number of elements paired
print(max(rotations))
