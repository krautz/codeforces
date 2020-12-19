"""
Problem: https://www.hackerrank.com/challenges/contacts/problem
"""

#
# CODE
#
class Node:

    def __init__(self, info):
        """
        I initialize myself.

        :param info: node info

        :returns: nothing
        """
        self.info = info
        self.leaves = 1
        self.childs = []


class Trie:

    def __init__(self):
        """
        I initialize myself.

        :returns: nothing
        """
        self.childs = []


    def addNode(self, name):
        """
        I add a name to the trie.

        :param name: name to be added

        :returns: nothing
        """
        # initialize level with root trie node
        level = self

        # parse each name letter
        for letter in name:

            # check if letter exists in current level
            found = False
            for node in level.childs:

                # letter already present in a node: increment its leaves and descend level
                if node.info == letter:
                    node.leaves += 1
                    level = node
                    found = True
                    break

            # letter not found in this level: create a node for it and descend level
            if found == False:
                node = Node(letter)
                level.childs.append(node)
                level = node

    def get(self, name):
        """
        I get ammount of strings in trie starting with name

        :param name: name to search for in trie

        :returns: ammount of words starting with name
        """
        level = self

        for letter in name:

            found = False
            for node in level.childs:

                if node.info == letter:
                    level = node
                    found = True
                    break

            if found == False:
                return 0

        return level.leaves


def realTrie():
    """
    I solve the problem using a real trie.

    :returns nothing
    """
    # read number of operations
    operations = int(input())

    # initialize empty trie
    trie = Trie()

    # execute each operation
    for _ in range(operations):

        # read operation and name
        operation, name = input().split()

        # add operation: populate trie
        if operation == 'add':
            trie.addNode(name)

        # find operation: print ammount on trie
        else:
            print(trie.get(name))


def fakeTrie():
    """
    I solve the problem using a hash map.

    :returns: nothing
    """
    # read number of operations
    operations = int(input())

    # initialize empty fake trie
    trie = dict()

    # execute each operation
    for _ in range(operations):

        # read operation and name
        operation, name = input().split()

        # add operation: populate trie
        if operation == 'add':

            # add each substring to trie
            for i in range(1, len(name) + 1):
                trie[name[:i]] = trie.get(name[:i], 0) + 1

        # find operation: print ammount on trie
        else:
            print(trie.get(name, 0))

realTrie()
