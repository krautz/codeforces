"""
AVL - Balanced Binary Search Tree implementation.

Application: Find elements in reasonable time.

Time Complexity:
    Add element: O(log(n))
    Delete element: O(log(n))
    Update value of en element: O(log(n))
    Build: O(n * log(n))

Space complexity: O(n)

Algorithm: Build a balanced binary search tree.
Binary: each node has at most two childrens.
Search: If the value of a node is smaller or equal to its parent, it must be a
left child, otherwise a right child.
Balanced: The height diference between the left child sub tree and right child
sub tree can be at most 1. If it is equal to 2, we must perform rotations to
rebalence the tree.

Problem to get input from:
https://www.geeksforgeeks.org/avl-tree-set-1-insertion/

Input:
op -> number of operations to perform
elements -> initial tree elements
op lines with:
'add' value
'remove' value
'update' value newValue


Examples:

Updating root on rotations:
    Simple left rotation:
        0
        1 2 3
    Double left rotation:
        0
        1 3 2
    Simple right rotation:
        0
        3 2 1
    Double right rotation:
        0
        3 1 2

Updating only childs on rotations:
    Simple left rotation:
        0
        2 1 3 4 5
    Double left rotation:
        0
        4 1 5 3 2
    Simple right rotation:
        0
        4 3 5 2 1
    Double right rotation:
        0
        2 1 5 3 4

Two rotations on diferent nodes upon addition:
    0
    1 2 3 4 5 6

Node removal:
    Root removal:
        3
        2 1 3
        remove 2
        remove 1
        remove 3
    Subistitute being direct node being removed left child:
        1
        3 2 4 1
        remove 3
    Subistitute being direct node being removed right child:
        1
        2 1 3 4
        remove 2
    Leaf removal without rotation:
        1
        2 1 3
        remove 1
    Leaf removal resulting rotation:
        1
        2 1 3 4
        remove 1
    Subistitute on left being a leaf:
        1
        3 1 4 2
        remove 1
    Subistitute on left not being a leaf:
        1
        5 2 6 1 4 7 3
        remove 2
    Subistitute on right being a leaf:
        1
        2 1 4 3
        remove 4
    Subistitute on right not being a leaf:
        1
        3 2 6 1 4 7 5
        remove 6
Geral:
    10
    1 2 3 4 5 6 7 8 9 10
    remove 8
    find 8
    find 10
    update 10 15
    find 10
    find 15
    add 13
    find 13
    remove 4
    add 4

    10
    10 9 8 7 6 5 4 3 2 1
    remove 2
    find 2
    find 1
    update 1 15
    find 1
    find 15
    add 13
    find 13
    remove 4
    add 4

    1
    5 3 10 2 4 7 11 1 6 9 12 8
    remove 10
"""

#
# CODE
#
class Node():
    """
    I am a tree node.
    """

    def __init__(self, value, parent = None):
        """
        I initialize a leaf node.

        :param value: node value
        :param parent: parent of the node being created

        :returns: nothing
        """
        # initialize new node
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
        self.height = 1


    @property
    def balanceFactor(self):
        """
        I compute the balance factor.

        :returns: balance factor
        """
        leftHeight = self.left.height if self.left != None else 0
        rightHeight = self.right.height if self.right != None else 0
        return rightHeight - leftHeight


    def updateHeight(self):
        """
        I update the node height.

        :returns: nothing
        """
        leftHeight = self.left.height if self.left != None else 0
        rightHeight = self.right.height if self.right != None else 0
        self.height = max(rightHeight, leftHeight) + 1


class Tree():
    """
    I am a balanced binary search tree.
    """

    def __init__(self):
        """
        I initialize an empty tree.

        :returns: nothing
        """
        self.root = None


    def inorder(self):
        """
        I print the tree in an inorder traversal.

        :returns: nothing
        """
        # start current node as root
        current = self.root

        # start emtpy node stack
        stack = []

        # inform tree height
        if self.root != None:
            print('Tree Height: ', self.root.height)
        else:
            print('Tree Height: ', 0)
        print('Inorder traversal: ', end = '')

        # while there is a current node and stack has nodes: print in order
        while current != None or len(stack) > 0:

            # current is not None: add it to stack and go to its left child
            if current != None:
                stack.append(current)
                current = current.left

            # current is None: print stack top and go to its right child
            else:
                node = stack.pop()
                print(node.value, end = ' ')
                current = node.right

        # print new line
        print()


    def add(self, value):
        """
        I add a node to the tree.

        :param value: value to be added

        :returns: nothing
        """
        # no root node: add node as root
        if self.root == None:
            self.root = Node(value, None)
            return

        # root already exists: find place of node to be added
        node = self.root
        while True:

            # left child: check if is already a leaf or not
            if value <= node.value:

                # current node is a leaf: add new node as left child
                if node.left == None:
                    node.left = Node(value, node)
                    self.rebalance(node)
                    break

                # current node is not a leaf: descend to left child
                node = node.left

            # right child: check if is already a leaf or not
            else:

                # current node is a leaf: add new node as right child
                if node.right == None:
                    node.right = Node(value, node)
                    self.rebalance(node)
                    break

                # current node is not a leaf: descend to right child
                node = node.right


    def find(self, value):
        """
        I find an element and return its node.

        :pram value: value to be found

        :returns: node with value or None on value not found
        """
        # initialize node as root
        node = self.root

        # find value
        while node != None:

            # value found: return node
            if node.value == value:
                return node

            # value is smaller than node: search in left sub tree
            elif node.value > value:
                node = node.left

            # value is bigger than node: search in right sub tree
            else:
                node = node.right

        # value not found: return None
        return None


    def remove(self, value):
        """
        I remove a node from the tree.

        :param value: value to be removed

        :returns: nothing
        """
        # find node to be removed
        node = self.find(value)

        # value does not exist: abort
        if node == None:
            print('Removal failure: Node with value ', value, ' not found')
            return

        # value exists: find best substitute candidate
        # node to be removed is a leaf: remove it
        if node.left == None and node.right == None:
            parent = node.parent
            self.updateNodeParentChild(node, None)

        # node to be removed has left child: find left child most right node
        elif node.left != None:

            # find substitute
            substitute = node.left
            while substitute.right != None:
                substitute = substitute.right

            # update node value to substitute value
            node.value = substitute.value

            # update substitute's parent child, and this child's parent
            parent = substitute.parent
            if parent == node:
                node.left = substitute.left
            else:
                parent.right = substitute.left
            if substitute.left != None:
                substitute.left.parent = parent

        # node to be removed has only right child: find right child most left nd
        else:

            # find substitute
            substitute = node.right
            while substitute.left != None:
                substitute = substitute.left

            # update node value to substitute value
            node.value = substitute.value

            # update substitute's parent child, and this child's parent
            parent = substitute.parent
            if parent == node:
                node.right = substitute.right
            else:
                parent.left = substitute.right
            if substitute.right != None:
                substitute.right.parent = parent

        # value updated and node removed: rebalance tree
        self.rebalance(parent)


    def update(self, value, newValue):
        """
        I update the value of a node.

        :param value: value to be updated
        :param newValue: node new value

        :returns: nothing
        """
        # get node to be updated
        node = self.find(value)

        # node not found: abort
        if node == None:
            print('Node update from ', value, ' to ', newValue, ' failed: ',
                  'Node with value ', value, ' not found')
            return

        # node found: update it
        self.remove(value)
        self.add(newValue)


    def updateNodeParentChild(self, node, newChild):
        """
        I update the parent's child of a node.

        :pram node: node to have its parent's child node updated
        :param newChild: parent's node child new node

        :returns: nothing
        """
        # get node's parent
        parent = node.parent

        # node is root: set new child as new root
        if parent == None:
            self.root = newChild

        # node is not root and node is left child of parent: update parent l ch
        elif parent.left == node:
            parent.left = newChild

        # node is not root and node is right child of parent: update parent r ch
        else:
            parent.right = newChild


    def rotateRight(self, node):
        """
        I rotate a node to its right.

        :param node: node to be rotated

        :returns: nothing
        """
        # get left child of node
        child = node.left

        # update parent's new child
        self.updateNodeParentChild(node, child)

        # update parents
        child.parent = node.parent
        node.parent = child

        # update childs
        node.left = child.right
        child.right = node
        if node.left != None:
            node.left.parent = node

        # update heights
        node.updateHeight()
        child.updateHeight()


    def rotateLeft(self, node):
        """
        I rotate a node to its left.

        :param node: node to be rotated

        :returns: nothing
        """
        # get right child of node
        child = node.right

        # update parent's new child
        self.updateNodeParentChild(node, child)

        # update parents
        child.parent = node.parent
        node.parent = child

        # update childs
        node.right = child.left
        child.left = node
        if node.right != None:
            node.right.parent = node

        # update heights
        node.updateHeight()
        child.updateHeight()


    def rebalance(self, node):
        """
        I rebalance the tree.

        :param node: node to start rebalance from

        :returns: nothing
        """
        # perform rebalance until root
        while node != None:

            # compute node height
            node.updateHeight()

            # store node's parent
            parent = node.parent

            # node balance factor is 2: rotate it properly
            if node.balanceFactor == 2:

                # right child of node has positive BF: rotate node left
                if node.right.balanceFactor == 1:
                    self.rotateLeft(node)

                # right child of node has negative BF: double rotate node left
                else:
                    self.rotateRight(node.right)
                    self.rotateLeft(node)

            # node balance factor is -2: rotate it properly
            elif node.balanceFactor == -2:

                # left child of node has negative BF: rotate node right
                if node.left.balanceFactor == -1:
                    self.rotateRight(node)

                # left child of node has positive BF: double rotate node right
                else:
                    self.rotateLeft(node.left)
                    self.rotateRight(node)

            # ascend to parent and rebalance it
            node = parent


if __name__ == '__main__':

    # read input
    operations = int(input())
    elements = list(map(int, input().split()))

    # build tree
    tree = Tree()
    for element in elements:
        tree.add(element)

    # perform operations
    for _ in range(operations):

        # read operation input
        operationInput = input().split()

        # add operation: add element
        if operationInput[0] == 'add':
            tree.add(int(operationInput[1]))

        # remove operation: remove element
        elif operationInput[0] == 'remove':
            tree.remove(int(operationInput[1]))

        # find operation: find element
        elif operationInput[0] == 'find':
            node = tree.find(int(operationInput[1]))
            print('Found' if node else 'Not found')

        # update operation: update element
        elif operationInput[0] == 'update':
            tree.update(int(operationInput[1]), int(operationInput[2]))

        # invalid operation: inform
        else:
            print('Invalid operation: ', operationInput[0])

    # print tree in order
    tree.inorder()
